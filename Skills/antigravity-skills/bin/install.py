#!/usr/bin/env python3

import os
import sys
from pathlib import Path

def main():
    print("🚀 Setting up Antigravity Skills...")

    # Determine the script directory
    script_dir = Path(__file__).parent

    # Antigravity global skills path
    antigravity_skills_dir = Path.home() / ".gemini" / "antigravity" / "skills"

    # Create the directory if it doesn't exist
    antigravity_skills_dir.mkdir(parents=True, exist_ok=True)

    # Remove existing symlinks to avoid conflicts
    for item in antigravity_skills_dir.iterdir():
        if item.is_symlink():
            item.unlink()

    # Create symlinks for all skills
    skills_dir = script_dir / ".." / "skills"
    if skills_dir.exists():
        for skill in skills_dir.iterdir():
            if skill.is_dir():
                link_path = antigravity_skills_dir / skill.name
                if link_path.exists():
                    link_path.unlink()
                link_path.symlink_to(skill, target_is_directory=True)

    print("✅ Skills installed successfully!")
    print(f"📍 Skills location: {antigravity_skills_dir}")
    print("")
    print("💡 Your Antigravity LLM will now automatically use relevant skills for prompts.")
    print("   For manual control, use @skill-name in your prompts.")

if __name__ == "__main__":
    main()