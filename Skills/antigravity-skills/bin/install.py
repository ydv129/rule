#!/usr/bin/env python3

import os
import sys
import shutil
from pathlib import Path

def main():
    print("🚀 Setting up Antigravity Skills...")

    # Determine the script directory
    script_dir = Path(__file__).parent

    # Antigravity global skills path
    antigravity_skills_dir = Path.home() / ".gemini" / "antigravity" / "skills"

    # Create the directory if it doesn't exist
    antigravity_skills_dir.mkdir(parents=True, exist_ok=True)

    # Remove existing entries to avoid conflicts
    for item in antigravity_skills_dir.iterdir():
        if item.is_symlink() or item.is_dir():
            if item.is_symlink():
                item.unlink()
            else:
                shutil.rmtree(item)

    # Create links/copies for all skills
    skills_dir = script_dir / ".." / "skills"
    if skills_dir.exists():
        method = "symlinks"
        for skill in skills_dir.iterdir():
            if skill.is_dir():
                target_path = antigravity_skills_dir / skill.name
                try:
                    # Try to create symlink first
                    target_path.symlink_to(skill, target_is_directory=True)
                except (OSError, NotImplementedError):
                    # Fall back to copying on systems that don't support symlinks or require privileges
                    method = "copies"
                    if target_path.exists():
                        shutil.rmtree(target_path)
                    shutil.copytree(skill, target_path)

    print("✅ Skills installed successfully!")
    print(f"📍 Skills location: {antigravity_skills_dir}")
    print(f"📋 Installation method: {method}")
    print("")
    print("💡 Your Antigravity LLM will now automatically use relevant skills for prompts.")
    print("   For manual control, use @skill-name in your prompts.")

if __name__ == "__main__":
    main()