# Antigravity Skills

A comprehensive collection of modular skills that enhance your Antigravity LLM with professional capabilities across development, design, planning, and more.

## Features

- **59 Specialized Skills** - From UI/UX design to code review, debugging to project planning
- **Automatic Skill Detection** - Intelligently applies the right skill to your prompts
- **One-Click Setup** - Clone and run, fully automated installation
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **Always Up-to-Date** - Skills are included directly, no external dependencies

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/ydv129/rule.git
cd rule
```

### 2. Install Skills

```bash
python Skills/antigravity-skills/bin/install.py
```

This automatically sets up all skills in your Antigravity skills directory (`~/.gemini/antigravity/skills/`). On Windows, files will be copied instead of symlinked due to permission restrictions - this is normal and works perfectly.

**After installation, you can safely remove the cloned `rule` directory if you only need basic skill functionality. However, keep it if you want to use the automatic skill enhancer or update skills later.**

### 3. Start Using Skills

Your Antigravity LLM now has access to all skills! Use them in two ways:

#### Automatic Mode (Recommended)
Pipe your prompts through the skill enhancer:

```bash
echo "Help me design a beautiful poster" | python Skills/antigravity-skills/bin/apply_skill.py
# Output: @canvas-design Help me design a beautiful poster
```

Then copy the enhanced prompt to your Antigravity chat.

#### Manual Mode
Prefix your prompts with the skill name:

```text
@canvas-design Help me design a beautiful poster
```

## How It Works

The skill enhancer analyzes your prompt and automatically detects the most relevant skill based on:
- Keyword matching with skill descriptions
- Phrase recognition from skill capabilities
- Context understanding for optimal skill selection

## Repository Structure

```
antigravity-skills/
├── bin/                    # Python executables
│   ├── install.py         # Automated setup script
│   └── apply_skill.py     # Intelligent skill enhancer
├── config/                # Configuration files
│   └── skills_index.json  # Skills metadata and descriptions
├── skills/                # Skill definitions (59 skills)
│   ├── canvas-design/     # Visual design and art creation
│   ├── brainstorming/     # Project planning and ideation
│   ├── react-best-practices/  # React development
│   └── ...                # 53 more specialized skills
└── README.md              # This documentation
```

## Available Skills

### 🎨 Design & Creative
- **canvas-design** - Create posters, graphics, and visual designs
- **algorithmic-art** - Generate algorithmic and generative art
- **brand-guidelines** - Apply professional brand standards
- **ui-ux-pro-max** - Advanced UI/UX design intelligence
- **web-design-guidelines** - Web interface design standards

### 🛠️ Development & Engineering
- **react-best-practices** - React and Next.js optimization
- **test-driven-development** - TDD methodology
- **systematic-debugging** - Professional debugging techniques
- **receiving-code-review** - Handle code review feedback
- **webapp-testing** - Automated web application testing

### 📊 Data & Office
- **xlsx** - Excel spreadsheet processing
- **docx** - Word document creation and editing
- **pptx** - PowerPoint presentation creation
- **pdf** - PDF processing and manipulation
- **notebooklm** - Google NotebookLM integration

### 🧠 Planning & Architecture
- **brainstorming** - Project ideation and planning
- **writing-plans** - Detailed implementation planning
- **project-development** - Full-stack project architecture
- **executing-plans** - Plan execution with checkpoints
- **verification-before-completion** - Quality assurance

### 🤖 AI & Evaluation
- **advanced-evaluation** - LLM evaluation and model comparison
- **evaluation** - Agent performance assessment
- **context-optimization** - Token and context management
- **memory-systems** - Long-term memory architectures

## Advanced Usage

### Batch Processing
Process multiple prompts:

```bash
cat prompts.txt | python Skills/antigravity-skills/bin/apply_skill.py
```

### Integration with Scripts
Use in your automation workflows:

```bash
#!/bin/bash
PROMPT="Build a React component for user authentication"
ENHANCED=$(echo "$PROMPT" | python Skills/antigravity-skills/bin/apply_skill.py)
# Use $ENHANCED in your Antigravity workflow
```

### Custom Skill Development
Add new skills by:
1. Creating a new directory in `Skills/antigravity-skills/skills/`
2. Adding a `SKILL.md` file with your skill definition
3. Updating `Skills/antigravity-skills/config/skills_index.json` with metadata
4. Running `python Skills/antigravity-skills/bin/install.py` to refresh

## After Installation

### Keeping the Repository
Keep the cloned `rule` directory if you want to:
- Use the automatic skill enhancer: `python Skills/antigravity-skills/bin/apply_skill.py`
- Update skills in the future by pulling latest changes
- Add custom skills or modify existing ones

### Removing the Repository
You can safely remove the cloned `rule` directory after installation if you only need:
- Basic skill functionality in Antigravity
- Manual skill usage with `@skill-name` prompts

**Note**: On Windows, skills are copied (not linked), so removing the source directory won't affect your installed skills.

## Windows Setup

On Windows, use PowerShell or Command Prompt:

```cmd
git clone https://github.com/ydv129/rule.git
cd rule
python Skills/antigravity-skills/bin/install.py
```

For skill enhancement:

```cmd
echo "Help me design a poster" | python Skills/antigravity-skills/bin/apply_skill.py
```

## Troubleshooting

### Skills Not Loading
1. Verify installation: `ls ~/.gemini/antigravity/skills/`
2. Re-run setup: `python Skills/antigravity-skills/bin/install.py`
3. Restart your Antigravity application

### Skill Not Detected
- Try more specific keywords in your prompt
- Use manual mode with `@skill-name`
- Check skill descriptions in `config/skills_index.json`

### Permission Errors
- On Windows, the installer will automatically copy files instead of creating symlinks (this is normal)
- Ensure write access to `~/.gemini/antigravity/skills/`
- Run with appropriate permissions if needed

## Contributing

To add new skills or improve existing ones:

1. Fork the repository
2. Create a feature branch
3. Add your skill in the appropriate category
4. Update the skills index
5. Submit a pull request

## License

This project is provided as-is for personal and professional use.
