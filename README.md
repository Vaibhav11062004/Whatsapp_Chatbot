🧠 Auto Chat Responder Bot using OpenAI + PyAutoGUI

This Python script automates replying to Facebook Messenger messages using OpenAI's GPT model and simulates human-like interaction using pyautogui. It reads the latest message from a specific person, generates a smart response using OpenAI's chat model (gpt-4o), and sends the reply—all automatically.

🔧 Features
🧠 AI-based replies with OpenAI (GPT-4o)

💬 Detects if the last message is from a specific person

🤖 Auto-copies chat content and responds instantly

🖱️ Uses pyautogui for GUI automation (mouse + keyboard)

🧑 Replies as "Vaibhav Chumbalkar" in casual bilingual (Hindi + English) tone

📋 Uses pyperclip for clipboard operations

🚀 How It Works
You provide the target Messenger contact name.

The script checks if the latest message is from them.

If yes, it:

Copies the message using screen automation

Sends the copied message to OpenAI's API

Gets the response and pastes it back into Messenger

📦 Dependencies
pyautogui

time

pyperclip

openai

⚠️ Note
Make sure your screen resolution and coordinates match the ones in the script.

This script uses hard-coded screen coordinates for clicks and drags. You may need to adjust them based on your screen setup.

For safety, avoid pushing your real API key to GitHub. Use environment variables or .env files instead.

📌 Disclaimer
This project is for educational purposes only. Automating interactions on platforms like Messenger may violate their terms of service. Use responsibly.

📸 Preview

![chat replay 2](https://github.com/user-attachments/assets/5c983984-8e91-4285-93be-609ff799bdb7)

