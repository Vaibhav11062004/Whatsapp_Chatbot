import pyautogui
import time
import pyperclip
from openai import OpenAI

# OpenAI API credentials
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key="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",  
)

def is_last_message_from_sender(chat_log, sender_name=input("Enter a Messenger Name: ")):
    """Check if the last message in the chat log is from the specified sender."""
    # Get the last message only
    messages = chat_log.strip().split("/2025] ")[-1]
    return sender_name in messages

pyautogui.click(1436,1044)  # Adjusted click position
time.sleep(1)

while True:
    time.sleep(2)
    pyautogui.moveTo(742,247)  # Adjusted moveTo position  
    pyautogui.dragTo(1679, 959, duration=1, button='left')  # Adjusted dragTo position  
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.click(1664,882)  # Keep as is (adjust if necessary)
    time.sleep(0.5)

    copied_text = pyperclip.paste()
    print("Copied Text:", copied_text)
    
    if is_last_message_from_sender(copied_text):
        # --- Get Response from OpenAI API ---
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": '''You are Vaibhav Chumbalkar, a coder from India who speaks both Hindi and English.
                    Analyze the chat history and respond like Vaibhav Chumbalkar. Keep the conversation short and simple, and don't use too many emojis.
                    Keep answers as short as possible.''',
                },
                {"role": "system", "content": "Do not start like this [1:16 AM, 3/20/2025] .:"},
                {
                    "role": "user",
                    "content": copied_text,
                }
            ],
            model="gpt-4o",
            temperature=1,
            max_tokens=4096,
            top_p=1,
        )
        
        response_text = response.choices[0].message.content
        pyperclip.copy(response_text)
        
        pyautogui.click(1310,975)  # Position of chat input box
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')  # Paste the generated response
        time.sleep(1)
        pyautogui.press('enter')  # Press Enter to send the message

