// Speclyze Logo Component for Next.js
// Usage: <SpeclyzeLogoFull /> or <SpeclyzeIcon />

export function SpeclyzeLogoFull({ className = "", width = 600, height = 200 }) {
  return (
    <svg 
      width={width} 
      height={height} 
      viewBox="0 0 600 200" 
      xmlns="http://www.w3.org/2000/svg"
      className={className}
    >
      <defs>
        <linearGradient id="leftGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style={{stopColor:"#7C3AED", stopOpacity:1}} />
          <stop offset="100%" style={{stopColor:"#6366F1", stopOpacity:1}} />
        </linearGradient>
        
        <linearGradient id="rightGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style={{stopColor:"#14B8A6", stopOpacity:1}} />
          <stop offset="100%" style={{stopColor:"#06B6D4", stopOpacity:1}} />
        </linearGradient>
        
        <linearGradient id="centerGrad" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" style={{stopColor:"#8B5CF6", stopOpacity:1}} />
          <stop offset="100%" style={{stopColor:"#6366F1", stopOpacity:1}} />
        </linearGradient>
      </defs>
      
      <g transform="translate(20, 40)">
        <path d="M 0,60 L 60,0 L 60,120 Z" fill="url(#leftGrad)" opacity="0.9"/>
        <path d="M 60,0 L 100,60 L 60,120 Z" fill="url(#centerGrad)"/>
        <path d="M 100,60 L 160,0 L 160,120 Z" fill="url(#rightGrad)" opacity="0.9"/>
        <line x1="60" y1="0" x2="60" y2="120" stroke="#fff" strokeWidth="1.5" opacity="0.3"/>
        <line x1="100" y1="60" x2="60" y2="0" stroke="#fff" strokeWidth="1" opacity="0.2"/>
        <line x1="100" y1="60" x2="60" y2="120" stroke="#fff" strokeWidth="1" opacity="0.2"/>
      </g>
      
      <text 
        x="210" 
        y="120" 
        fontFamily="system-ui, -apple-system, sans-serif" 
        fontSize="72" 
        fontWeight="600" 
        fill="#7C3AED" 
        letterSpacing="-2"
      >
        Speclyze
      </text>
    </svg>
  );
}

export function SpeclyzeIcon({ className = "", width = 160, height = 120 }) {
  return (
    <svg 
      width={width} 
      height={height} 
      viewBox="0 0 160 120" 
      xmlns="http://www.w3.org/2000/svg"
      className={className}
    >
      <defs>
        <linearGradient id="leftGradIcon" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style={{stopColor:"#7C3AED", stopOpacity:1}} />
          <stop offset="100%" style={{stopColor:"#6366F1", stopOpacity:1}} />
        </linearGradient>
        
        <linearGradient id="rightGradIcon" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style={{stopColor:"#14B8A6", stopOpacity:1}} />
          <stop offset="100%" style={{stopColor:"#06B6D4", stopOpacity:1}} />
        </linearGradient>
        
        <linearGradient id="centerGradIcon" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" style={{stopColor:"#8B5CF6", stopOpacity:1}} />
          <stop offset="100%" style={{stopColor:"#6366F1", stopOpacity:1}} />
        </linearGradient>
      </defs>
      
      <path d="M 0,60 L 60,0 L 60,120 Z" fill="url(#leftGradIcon)" opacity="0.95"/>
      <path d="M 60,0 L 100,60 L 60,120 Z" fill="url(#centerGradIcon)"/>
      <path d="M 100,60 L 160,0 L 160,120 Z" fill="url(#rightGradIcon)" opacity="0.95"/>
      <line x1="60" y1="0" x2="60" y2="120" stroke="#fff" strokeWidth="2" opacity="0.3"/>
      <line x1="100" y1="60" x2="60" y2="0" stroke="#fff" strokeWidth="1.5" opacity="0.2"/>
      <line x1="100" y1="60" x2="60" y2="120" stroke="#fff" strokeWidth="1.5" opacity="0.2"/>
    </svg>
  );
}

// Usage in your page.tsx:
// import { SpeclyzeLogoFull, SpeclyzeIcon } from '@/components/Logo';
// 
// In header: <SpeclyzeLogoFull width={200} height={67} />
// As favicon: <SpeclyzeIcon width={32} height={24} />
