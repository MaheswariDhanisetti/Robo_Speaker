# Robo Speaker 0.1

Welcome to Robo Speaker 0.1, a simple and fun Python-based text-to-speech (TTS) application that uses your system's speaker to vocalize any text input through the command line interface (CLI). This project was created by Mahi.

## Project Overview

Robo Speaker 0.1 is a mini project designed to demonstrate basic text-to-speech capabilities using Python. The application listens for user input in the CLI and converts the text into speech, utilizing the system's built-in speaker. It is a straightforward implementation that showcases how to leverage system libraries for speech synthesis.

## Features

- **Text-to-Speech Conversion**: Input any text via the CLI, and Robo Speaker will pronounce it out loud.
- **Easy Exit**: Type 'q' to exit the application gracefully, with a farewell message.

## How It Works
The project uses PowerShell commands to access the Windows Speech API (System.Speech) for speech synthesis. When the user inputs text, the program constructs a command to be executed by PowerShell, which then performs the text-to-speech conversion.
