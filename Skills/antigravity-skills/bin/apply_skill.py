#!/usr/bin/env python3

import json
import sys
import re
from pathlib import Path

def load_skills_index():
    """Load skills index from config file."""
    script_dir = Path(__file__).parent.parent
    index_path = script_dir / 'config' / 'skills_index.json'
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Skills index not found at {index_path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {index_path}", file=sys.stderr)
        sys.exit(1)

def find_best_skill(prompt, skills):
    """Find the best matching skill for the given prompt."""
    prompt_lower = prompt.lower().strip()
    if not prompt_lower:
        return None

    best_match = None
    best_score = 0

    for skill in skills:
        description = skill['description'].lower()
        score = 0

        # Extract key phrases from description (quoted parts)
        key_phrases = re.findall(r'"([^"]*)"', description)
        if not key_phrases:
            key_phrases = [description]

        # Score based on key phrases
        for phrase in key_phrases:
            phrase_lower = phrase.lower()
            if phrase_lower in prompt_lower:
                score += len(phrase.split())  # Weight by phrase length

        # Score based on word overlap
        desc_words = set(description.split())
        prompt_words = set(prompt_lower.split())
        overlap = len(desc_words & prompt_words)
        score += overlap * 0.5

        # Bonus for exact matches
        if any(phrase.lower() in prompt_lower for phrase in key_phrases):
            score += 2

        if score > best_score:
            best_score = score
            best_match = skill

    return best_match if best_score > 1 else None  # Require minimum score

def main():
    # Check if input is from stdin or arguments
    if not sys.stdin.isatty():
        # Input from pipe
        prompt = sys.stdin.read().strip()
    elif len(sys.argv) >= 2:
        # Input from arguments
        prompt = ' '.join(sys.argv[1:])
    else:
        print("Usage: python bin/apply_skill.py \"your prompt here\"", file=sys.stderr)
        print("   or: echo \"your prompt\" | python bin/apply_skill.py", file=sys.stderr)
        sys.exit(1)

    if not prompt:
        print("Error: No prompt provided", file=sys.stderr)
        sys.exit(1)

    skills = load_skills_index()
    skill = find_best_skill(prompt, skills)

    if skill:
        enhanced_prompt = f"@{skill['id']} {prompt}"
        print(enhanced_prompt)
    else:
        print(prompt)  # No skill found, return original prompt

if __name__ == "__main__":
    main()