# 🤖 Auto-Reply AI ChatBot

This project is an **automated AI chatbot** that reads messages from your screen, sends them to an AI model for processing, and automatically replies — all using Python, OpenAI, and GUI automation.

## 🚀 Features

- Automatically reads chat messages from screen
- Sends them to a GPT-4o-based AI model
- Replies with AI-generated responses
- Fully automated with mouse/keyboard control
- Runs in a loop, exits safely with `ESC` key

## 🛠️ Requirements

- Python 3.7+
- OpenAI-compatible API (e.g. [GitHub's GPT-4o proxy](https://models.github.ai))
- Python Libraries:
  - `pyautogui`
  - `pyperclip`
  - `openai`
  - `keyboard`

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/auto-reply-chatbot.git
cd auto-reply-chatbot

2. **Install required libraries:**

```bash
pip install pyautogui pyperclip openai keyboard

3. **Set your API key:**

```bash
api_key="api_key_here"
