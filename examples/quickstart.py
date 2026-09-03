#!/usr/bin/env python3
"""
Quick start guide for Agent-Reach.

This script demonstrates the simplest way to get started with Agent-Reach.
"""

from agent_reach.core import AgentReach


def main():
    """Quick start example."""
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║         Agent-Reach Quick Start Guide                       ║
║                                                              ║
║  Give your AI Agent eyes to see the entire internet!        ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Initialize Agent-Reach
    print("📦 Initializing Agent-Reach...")
    ar = AgentReach()
    
    # Setup
    print("⚙️  Running setup...")
    ar.setup(system=False)
    
    # Run diagnostics
    print("\n🔍 Checking available platforms...\n")
    ar.doctor()
    
    # Show usage instructions
    print("""
╔══════════════════════════════════════════════════════════════╗
║  WHAT'S NEXT?                                               ║
╚══════════════════════════════════════════════════════════════╝

1. ZERO-CONFIG PLATFORMS (No authentication needed):
   ✓ Read any website
   ✓ Get YouTube transcripts
   ✓ Parse RSS feeds
   ✓ Query GitHub public repositories

2. REQUIRES CONFIGURATION:
   • Twitter/X - Set up authentication token
   • Reddit - Configure login credentials
   • XiaoHongShu (小红书) - Browser login
   • Facebook/Instagram - Desktop browser login

3. TRY IT WITH YOUR AI AGENT:
   Tell Claude, Cursor, or Windsurf:
   "帮我安装 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md"

4. UPDATE ANYTIME:
   "帮我更新 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md"

5. DIAGNOSTICS:
   Run: agent-reach doctor

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For more examples, see:
  • examples/sample_usage.py
  • examples/advanced_usage.py

Documentation: https://github.com/emil13-ecomcrz/Agent-Reach
    """)


if __name__ == "__main__":
    main()
