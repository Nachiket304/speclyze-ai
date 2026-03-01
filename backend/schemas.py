from pydantic import BaseModel
from typing import List, Optional

# 1. The new format for a single Step
class TestStep(BaseModel):
    step_number: int
    action: str
    test_data: Optional[str] = ""
    expected_result: str

# 2. The new format for the Test Case
class TestCase(BaseModel):
    tc_no: str
    test_summary: str
    test_description: str
    precondition: str
    steps: List[TestStep]

# 3. Request / Response
class TestGenerationRequest(BaseModel):
    requirement_text: str
    complexity: str = "medium"

class TestGenerationResponse(BaseModel):
    project_name: str
    generated_test_cases: List[TestCase]