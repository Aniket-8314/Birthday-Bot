# DroidRun-BirthdayBot
An autonomous Android agent built with DroidRun. Checks your calendar for birthdays and sends custom, AI-generated WhatsApp wishes.

> **Droidrun DevSprint 2026 Submission**
> *Automating social connections with Generative AI*

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Framework](https://img.shields.io/badge/Framework-DroidRun-orange)
![AI Model](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-green)

## 📖 Overview
**BirthdayBot** solves the problem of forgetting to message friends on their special day. It combines **Computer Vision** (to read the Calendar UI) with **Generative AI** (to write the message), acting as a fully autonomous agent that manages your social obligations.

## 🚀 Key Features
* **📅 Event Detection:** Scans Google Calendar for daily events marked "Birthday".
* **✍️ Creative Writing:** Uses Gemini to write a unique, context-aware message (no boring "HBD" texts).
* **💬 WhatsApp Automation:** Navigates WhatsApp to find the correct contact and hit send.

## 🛠️ Tech Stack
* **Core Framework:** [DroidRun](https://github.com/droidrun/droidrun)
* **Intelligence:** Google Gemini 2.5 Flash
* **Connectivity:** ADB
* **Language:** Python 3.10+

---

## ⚙️ Setup & Usage

1.  **Add a Test Event:** Open your Calendar and add an event for today named "Yash Birthday".
2.  **Add a Contact:** Ensure you have a WhatsApp conversation with "Yash" (or use your own secondary number for testing).
3.  **Run the Agent:**
    ```bash
    python birthday_agent.py
    ```