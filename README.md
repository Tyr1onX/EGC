# Everything Gemini Code

![Everything Gemini Code — the performance system for AI agent harnesses](assets/hero.png)

[![Version](https://img.shields.io/badge/version-v2.0.0--rc.1-blue.svg?style=flat-square)]() [![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE) [![Status](https://img.shields.io/badge/status-Production%20Candidate-2ea44f.svg?style=flat-square)]() [![Runtime](https://img.shields.io/badge/runtime-Hardened-2ea44f.svg?style=flat-square)]() [![Platform](https://img.shields.io/badge/platform-Cross--Platform-blue.svg?style=flat-square)]()
[![Gemini Native](https://img.shields.io/badge/engine-Gemini%20Native-1a73e8.svg?style=flat-square)]() [![Claude Bridge](https://img.shields.io/badge/bridge-Claude-d97757.svg?style=flat-square)]() [![OpenAI Bridge](https://img.shields.io/badge/bridge-OpenAI-412991.svg?style=flat-square)]() [![Routing](https://img.shields.io/badge/routing-Multi--Provider-8a2be2.svg?style=flat-square)]()
[![Python](https://img.shields.io/badge/-Python%203.10+-3776AB?style=flat-square&logo=python&logoColor=white)]() [![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)]() [![Tkinter](https://img.shields.io/badge/-Tkinter%20GUI-4B8BBE?style=flat-square&logo=python&logoColor=white)]() [![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)]() [![Linux](https://img.shields.io/badge/-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)]() [![Windows](https://img.shields.io/badge/-Windows-0078D6?style=flat-square&logo=windows&logoColor=white)]() [![macOS](https://img.shields.io/badge/-macOS-000000?style=flat-square&logo=apple&logoColor=white)]() [![Execution Queue](https://img.shields.io/badge/architecture-Execution%20Queue-orange.svg?style=flat-square)]() [![Memory Mesh](https://img.shields.io/badge/architecture-Memory%20Mesh-orange.svg?style=flat-square)]() [![Agent Orchestration](https://img.shields.io/badge/architecture-Agent%20Orchestration-orange.svg?style=flat-square)]()

<div align="center">

</div>

**A professional, cross-platform AI operating system and runtime orchestration fabric for Gemini Code.**

Not just configs. EGC is a massive, production-grade system: skills, memory optimization, execution queues, security scanning, and research-first development. It features a complete control plane, dynamic model routing, and production-ready agents evolved through intensive daily use.

### ⚙️ Technology Surface
**Core Stack:** Python 3.10+, TypeScript, SQLite, Tkinter GUI  
**Intelligence:** Gemini-Native, Dynamic Model Routing, Provider Adapters  
**Orchestration:** Execution Queue, Agent Management, Memory Mesh  
**Deployment:** Cross-Platform (Linux, macOS, Windows), CLI-Native  

### The EGC Control Plane in Action

> *Live Execution: The EGC Control Plane tracking agent orchestration in real-time.*

<div align="center">
  <video src="https://raw.githubusercontent.com/Fmarzochi/everything-gemini/main/assets/demo.mp4" autoplay loop muted playsinline width="100%"></video>
</div>

*(Note: If the video above does not play automatically in your Markdown viewer, you can download `assets/demo.mp4` to view the full control plane showcase.)*

---

## 🚀 Features at a Glance

| Pillar | Description |
|--------|-------------|
| **Gemini-Native Engine** | Built from the ground up for Gemini Code, with fallback bridges for Claude and OpenAI. |
| **Control Plane GUI** | A Tkinter-based dashboard for real-time observability of your agentic workforce. |
| **Agent Orchestration** | 48+ highly specialized cognitive agents ready to execute complex sub-tasks. |
| **Skills System** | 182+ domain-specific workflows covering frontend, backend, security, and deployment. |
| **Dynamic ModelResolver** | Never hardcode a model again. EGC routes to the most capable model based on the task. |
| **Cross-Platform** | Engineered to run seamlessly on Linux, Windows, and macOS. |

---

## 🧠 Why EGC Exists

AI code assistants often degrade into confusing text files and fragmented commands. **Everything Gemini Code (EGC)** fixes this by wrapping the Gemini AI ecosystem in a strict, observable, and professional engineering architecture. It transforms a standard AI assistant into a **managed team of cognitive workers**, monitored via a real-time dashboard.

---

## 🏗️ Architecture Overview

EGC is divided into three primary layers:

1.  **The Cognitive Layer (Agents & Skills)**
    *   **Agents:** The "who". Specialized personas (e.g., `security-reviewer`, `code-architect`) that handle distinct domains.
    *   **Skills:** The "how". Standardized operating procedures (e.g., `django-tdd`, `react-accessibility`) that guide agents to success without hallucinations.
2.  **The Runtime Engine (Orchestrators & Queue)**
    *   **Execution Queue:** Manages task dependencies, preventing race conditions and ensuring deterministic outcomes.
    *   **Memory Mesh:** Context is preserved across sessions. Agents don't forget what was discussed 3 hours ago.
    *   **ModelResolver:** Intelligently selects the best model size (Flash vs. Pro) based on the current workload's token budget and complexity.
3.  **The Control Plane (Dashboard)**
    *   **`egc_dashboard.py`:** A zero-dependency, cross-platform Tkinter GUI that provides a window into the otherwise invisible AI execution loop.

---

## 💻 Full Technology Stack

*   **Core:** Python 3.10+, TypeScript, Bash
*   **Database / State:** SQLite, JSON Registry
*   **Presentation:** Tkinter (GUI), Markdown
*   **AI Providers:** Google Gemini (Primary), Anthropic Claude (Bridge), OpenAI (Bridge)

---

## 📁 Directory Tree

```text
everything-gemini/
├── agents/             # Cognitive worker definitions (e.g., code-architect, security-reviewer)
├── assets/             # Media, banners, and logos (hero.png, demo.mp4, ecc-logo.png)
├── commands/           # CLI slash-command entrypoints for the terminal
├── docs/               # Technical documentation and translations
├── hooks/              # Lifecycle interceptors (PreToolUse, PostToolUse, etc.)
├── rules/              # Language-specific coding standards (Python, TS, Go, etc.)
├── scripts/            # Core orchestration and execution logic
├── skills/             # Domain-specific workflows and knowledge
├── src/                # The Python cognitive core and ModelResolver
└── egc_dashboard.py    # The Control Plane GUI (Start here!)
```

---

## 🛠️ Beginner Installation Guide

Welcome! If you have never used Python, Git, or an AI CLI before, this guide is written specifically for you.

### Phase 1: Environment Setup

**1. Install Python**
You need Python installed on your computer.
*   **Windows:** Download from [python.org](https://www.python.org/downloads/). **CRITICAL:** Check the box that says "Add Python to PATH" during installation.
*   **macOS:** Install via Homebrew: `brew install python` or download from python.org.
*   **Linux:** Open your terminal and run `sudo apt update && sudo apt install python3 python3-venv python3-pip`.

**2. Install Git**
Git downloads the code.
*   Download and install from [git-scm.com](https://git-scm.com/downloads).

**3. Install Gemini CLI**
EGC orchestrates the Gemini CLI. You need Node.js installed to get it.
*   Download Node.js from [nodejs.org](https://nodejs.org/).
*   Open your terminal and run: `npm install -g @google/gemini-cli`

### Phase 2: Project Cloning

Open your terminal (Command Prompt on Windows, Terminal on macOS/Linux) and run:

```bash
# 1. Download the EGC operating system to your computer
git clone https://github.com/Fmarzochi/everything-gemini.git

# 2. Enter the directory
cd everything-gemini
```

### Phase 3: Virtual Environment (Dependency Isolation)

**What is a Virtual Environment?**
A virtual environment (`venv`) acts as a dedicated sandbox for EGC. It ensures that the Python packages EGC needs don't interfere with your computer's global system files, and keeps your installation clean and isolated.

**Why use it?**
If you ever need to uninstall EGC or fix a dependency issue, the virtual environment prevents any risk of breaking other Python projects on your machine.

**Create and Activate the Environment:**

*   **Linux / macOS:**
    ```bash
    # Create the sandbox
    python3 -m venv .venv
    
    # Activate it (You must do this every time you open a new terminal for EGC)
    source .venv/bin/activate
    
    # Install any potential dependencies (if requirements exist)
    pip install -r requirements.txt || true
    ```

*   **Windows:**
    ```powershell
    # Create the sandbox
    python -m venv .venv
    
    # Activate it (You must do this every time you open a new terminal for EGC)
    .\.venv\Scripts\activate
    
    # Install any potential dependencies
    pip install -r requirements.txt || true
    ```

*(Note: When active, you should see `(.venv)` prefixing your terminal prompt.)*

### Phase 4: First Boot (The Dashboard)

EGC is visual. You don't need to memorize commands to start exploring. Ensure your virtual environment is active (from Phase 3), then run:

```bash
# Run the Control Plane Dashboard
python3 egc_dashboard.py
```

*Note for Windows users:* If `python3` doesn't work, try typing `python egc_dashboard.py`.

The EGC Dashboard will open. From here, you can browse every Agent, Skill, Command, and Rule installed on the system, and monitor live execution logs.

---

## ⚡ CLI Execution

Once you are comfortable with the Dashboard, you can start using EGC in your terminal.
Ensure you are inside the `everything-gemini` folder.

```bash
# Start the Gemini CLI
gemini
```

Inside the interactive prompt, you can call EGC commands:
*   `/help` - View available commands.
*   `/plan "Build a secure authentication system"` - Triggers the planner agent.
*   `/security-scan` - Triggers the AgentShield security auditor.

---

## 🌐 Cross-Platform Support

EGC is rigorously tested across all major operating systems.

### Windows
*   **Execution:** Use PowerShell or Command Prompt.
*   **UI:** The Tkinter dashboard works natively without X11 servers.
*   **Paths:** EGC automatically handles Windows `\` path separators internally.

### Linux (Ubuntu/Debian/Arch)
*   **Execution:** Standard bash or zsh.
*   **UI:** Ensure you have Tkinter installed (`sudo apt install python3-tk`).
*   **Paths:** Native Unix paths `/`.

### macOS
*   **Execution:** zsh (default) or bash.
*   **UI:** macOS includes Tkinter with its standard Python distributions.

---

## 🛑 Troubleshooting

**1. The dashboard opens as a blank white/gray screen.**
*   *Fix:* Ensure you are running it exactly as `python3 egc_dashboard.py` from the root of the `everything-gemini` folder. Do not run it from inside another directory.

**2. "gemini: command not found"**
*   *Fix:* You missed installing the Gemini CLI. Run `npm install -g @google/gemini-cli`.

**3. "ModuleNotFoundError: No module named 'tkinter'" (Linux)**
*   *Fix:* Run `sudo apt install python3-tk`.

---

## ❓ FAQ

**Q: Do I need an API key?**
A: Yes. You will need a Google Gemini API key configured for the Gemini CLI to execute AI commands.

**Q: Can I use this for non-Python projects?**
A: Absolutely. EGC is written in Python, but the Agents and Skills can write, review, and test code in TypeScript, Java, Go, Rust, PHP, Swift, and more.

**Q: Is this a replacement for my IDE?**
A: No. EGC runs alongside your IDE (like VS Code or Cursor). It acts as your automated senior engineering team, while you remain the director.

---

## 🤝 Contributing

Contributions are welcome! Please check our `docs/` folder for architectural guidelines before submitting large pull requests.
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <img src="assets/images/ecc-logo.png" width="40" height="40" alt="EGC Logo">
  <br>
  <b>Built with precision by Felipe Marzochi.</b><br>
  <i>Elevating AI orchestration from chatboxes to engineering systems.</i>
</div>
