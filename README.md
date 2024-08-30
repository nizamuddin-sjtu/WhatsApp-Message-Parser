# WhatsApp-Message-Parser
This repository contains a Python application for cleaning and detecting the language of WhatsApp messages. The application uses a graphical user interface (GUI) built with Tkinter, integrating various text processing techniques to clean and analyze messages.
Features

    Text Cleaning:
        Removes URLs and emojis from messages.
        Converts text to lowercase and removes punctuation for consistent processing.

    Language Detection:
        Utilizes langid to classify the language of each cleaned message.

    User Interface:
        Provides a GUI for users to paste WhatsApp messages, process them, and view the cleaned and language-detected results.

Components

    Text Cleaning:
        URL Removal: Strips out URLs from messages.
        Emoji Removal: Filters out emojis using a regular expression pattern.
        Lowercasing and Punctuation Removal: Converts text to lowercase and removes non-alphanumeric characters.

    Language Detection:
        Uses the langid library to detect the language of the cleaned message.

    GUI:
        Built with Tkinter, the application allows users to input messages, process them, and view results in a new window.

Usage

    Clone the Repository:

    bash

git clone https://github.com/nizamuddin-sjtu/whatsapp-message-parser.git

Install Dependencies: Make sure you have Python installed, then install the required libraries:

bash

pip install googletrans==4.0.0-rc1 langid

Run the Application: Navigate to the project directory and run the application:

bash

python app.py

Input Messages:

    Paste WhatsApp messages into the text box.
    Click "Process Messages" to clean and detect the language of the messages.

View Results:

    Results will be displayed in a new window, showing the detected language and cleaned message.
