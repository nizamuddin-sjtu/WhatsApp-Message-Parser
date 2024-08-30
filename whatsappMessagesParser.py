#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
from googletrans import Translator
import langid
import tkinter as tk
from tkinter import ttk, scrolledtext

def clean_and_detect_language():
    input_text = text_box.get("1.0", tk.END)
    messages = input_text.splitlines()

    cleaned_messages = []

    for message in messages:
        cleaned_message = clean_message(message)
        lang = detect_language(cleaned_message)

        if cleaned_message:
            cleaned_messages.append((lang, cleaned_message))

    display_results(cleaned_messages)

def clean_message(message):
    # Remove URLs
    message = re.sub(r'https?://\S+|www\.\S+', '', message)

    # Remove emojis
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"
                           u"\U0001F300-\U0001F5FF"
                           u"\U0001F680-\U0001F6FF"
                           u"\U0001F700-\U0001F77F"
                           u"\U0001F780-\U0001F7FF"
                           u"\U0001F800-\U0001F8FF"
                           u"\U0001F900-\U0001F9FF"
                           u"\U0001FA00-\U0001FA6F"
                           u"\U0001FA70-\U0001FAFF"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251" 
                           u"\U0001F004-\U0001F0CF"  # Miscellaneous Symbols and Pictographs
                           "]+", flags=re.UNICODE)
    message = emoji_pattern.sub(r'', message)

    # Convert to lowercase and remove punctuation
    message = re.sub(r'[^\w\s]', '', message.lower())

    return message.strip()

def detect_language(message):
    try:
        lang, _ = langid.classify(message)
        return lang
    except Exception as e:
        print(f"Error detecting language: {e}")
        return "unknown"

def display_results(messages):
    result_window = tk.Toplevel(root)
    result_window.title("Cleaned and Detected Messages")

    text_widget = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=80, height=20, font=("Helvetica", 12))
    text_widget.grid(row=0, column=0, padx=10, pady=10)

    for lang, message in messages:
        text_widget.insert(tk.END, f"{lang}: {message}\n")

# Create the main application window
root = tk.Tk()
root.title("WhatsApp Message Parser")

# Add a label
label = ttk.Label(root, text="Paste your WhatsApp messages below:", font=("Helvetica", 12))
label.pack(pady=10)

# Add a text box for input
text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10, font=("Helvetica", 12))
text_box.pack(pady=10)

# Add a button to process input
process_button = ttk.Button(root, text="Process Messages", command=clean_and_detect_language)
process_button.pack(pady=10)

# Start the main event loop
root.mainloop()


# In[ ]:




