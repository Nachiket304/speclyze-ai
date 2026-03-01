import os
import json
import sqlite3
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from anthropic import Anthropic
from schemas import TestGenerationRequest, TestGenerationResponse

# 1. Load Secrets
load_dotenv(override=True)
API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not API_KEY:
    raise ValueError("❌ Missing API Key! Check your .env file.")

print(f"\n=========================================")
print(f"🧠 AI: Online (Claude Opus 4.1)")
print(f"💾 Database: Connected to Local SQLite")
print(f"=========================================\n")

# 2. Initialize AI Client
ai_client = Anthropic(api_key=API_KEY)
app = FastAPI(title="TestGenius AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Initialize Local Database
DB_FILE = "testgenius_memory.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS test_suites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            requirement_text TEXT NOT NULL,
            generated_json TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()  # Run this immediately when the server starts

SYSTEM_PROMPT = """
You are an elite Enterprise QA/SDET Lead.
Your task is to generate comprehensive, edge-case-inclusive manual test cases for a given user story.

You MUST output ONLY valid JSON. Do not include markdown formatting like ```json, and do not include any conversational text.

The JSON must strictly follow this exact structure:
{
  "project_name": "AI Generated Suite",
  "generated_test_cases": [
    {
      "tc_no": "TC-001",
      "test_summary": "Brief summary",
      "test_description": "Detailed description of what is being verified",
      "precondition": "Required state before testing",
      "steps": [
        {
          "step_number": 1,
          "action": "User action",
          "test_data": "Specific data to use (or empty string)",
          "expected_result": "System behavior"
        }
      ]
    }
  ]
}

Rules:
1. Generate at least 3 test cases: One Positive, One Negative, and One Edge Case.
2. Keep the 'test_data' field realistic (e.g., 'testuser@gmail.com', 'invalid_pass!').
3. Do not break the JSON format under any circumstances.
"""

@app.get("/")
def read_root():
    return {"status": "active", "message": "TestGenius AI is online!"}

@app.post("/generate-tests", response_model=TestGenerationResponse)
async def generate_tests(request: TestGenerationRequest):
    print(f"🧠 Asking Claude to analyze: {request.requirement_text[:50]}...")
    
    try:
        # 1. Generate Tests with Claude
        message = ai_client.messages.create(
            model="claude-opus-4-1", 
            max_tokens=2500,
            temperature=0.2,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": f"Generate enterprise test cases for this requirement: {request.requirement_text}"}
            ]
        )
        
        raw_content = message.content[0].text
        
        # Clean markdown if present
        if raw_content.startswith("```json"):
            raw_content = raw_content.replace("```json\n", "").replace("```", "").strip()
        elif raw_content.startswith("```"):
            raw_content = raw_content.replace("```\n", "").replace("```", "").strip()
            
        data = json.loads(raw_content)
        print("✅ Successfully generated AI test cases!")

        # 2. Save to Local SQLite Memory
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            # We save the raw requirement and we convert the JSON dict back to a string to save it
            cursor.execute(
                "INSERT INTO test_suites (requirement_text, generated_json) VALUES (?, ?)",
                (request.requirement_text, json.dumps(data))
            )
            conn.commit()
            conn.close()
            print("💾 Successfully saved to local SQLite database!")
        except Exception as db_err:
            print(f"⚠️ Warning: Could not save to local database: {db_err}")
        
        return data

    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/api/history")
async def get_history():
    print("📂 Fetching test history for the UI...")
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Grab the 10 most recent test suites, ordered by newest first
        cursor.execute('''
            SELECT id, created_at, requirement_text, generated_json 
            FROM test_suites 
            ORDER BY id DESC LIMIT 10
        ''')
        rows = cursor.fetchall()
        conn.close()

        history = []
        for row in rows:
            history.append({
                "id": row[0],
                "created_at": row[1],
                "requirement_text": row[2],
                # We convert the text back into a real JSON object for the frontend
                "generated_json": json.loads(row[3]) 
            })
        
        return {"status": "success", "data": history}

    except Exception as e:
        print(f"❌ Error fetching history: {e}")
        raise HTTPException(status_code=500, detail="Could not fetch history from database.")