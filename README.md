# iPadOS 26 LLM and Shortcut Integrations

This repository gathers resources and links to integrate AI models (such as ChatGPT and Gemini) with iPadOS 26 using Apple Shortcuts, Notes and Google Drive. It does not host the third‑party code directly; instead it points to the original projects and tutorials so that you can import the Shortcuts or clone the repositories yourself.

## New features of iPadOS 26 Shortcuts

Apple introduced several new actions in iPadOS 26.  The **Use Model** action allows a Shortcut to call a large language model (local, cloud or ChatGPT).  It includes a *follow‑up* option to continue a conversation and integrates seamlessly with the system【137675515535876†L118-L129】.  Additional actions like **Create Table from Text**, **Adjust Tone**, **Rewrite Text** and **Summarize Text** provide built‑in generative capabilities【23709012036594†L146-L162】.  The Notes app also exposes new actions such as **Add File** and **Append to List**【23709012036594†L171-L198】, making it easy to store model outputs in your notes.

## Shortcuts with GPT

- **ChatGPT Siri** – A Shortcut by *Yue‑Yang* that lets you talk to ChatGPT through Siri.  It supports persistent sessions and can log conversation history to the Notes app.  Install it from the iCloud link on the project page: <https://github.com/Yue‑Yang/ChatGPT‑Siri>.

- **Notefy** – Created by *nicolodiamante*, this Shortcut uses Whisper to transcribe audio and ChatGPT to summarize the content.  It’s ideal for meetings or lectures; the resulting summary is saved to Notes.  See the project page: <https://github.com/nicolodiamante/Notefy>.

- **Share‑to‑ChatGPT** – By *reorx*, this Shortcut adds a Share Sheet action to send selected text or web pages to ChatGPT with custom prompts.  The response is returned and optionally stored in iCloud Drive.  Project page: <https://github.com/reorx/share‑to-chatgpt>.

## Shortcuts with Gemini

- **Gemini API Shortcut Tutorial** – A RoutineHub article explains how to build a Shortcut that calls the Gemini API using the *Get Contents of URL* action.  You’ll need to obtain an API key from ai.google.dev and configure the request body to include your prompt.  Tutorial: <https://routinehub.co/guide/gemini-api-shortcut>.

- **Gemini Pro Chat** – This Shortcut uses a proxy service to connect to Gemini Pro.  It provides a simple interface for asking questions.  See: <https://github.com/ProAI-shortcuts/Gemini-Pro-Chat>.

## Python projects for Google Drive integration

- **gdrive‑chatgpt** – A Python example that uses LangChain to load documents from a Google Drive folder and interact with them via ChatGPT【653901277322383†L234-L248】.  Setup requires Google Drive API credentials and an OpenAI API key.  Repository: <https://github.com/fonckchain/gdrive-chatgpt>.

- **ChatGPT‑GDrive‑Integration** – Another Python project that vectorizes the contents of a Google Drive directory, stores them in a vector database and exposes a Flask API for semantic search【523603751305858†L235-L316】.  Repository: <https://github.com/robson‑koji/ChatGPT-GDrive-Integration>.

## How to import on iPad

For Shortcuts:

1. Make sure **Private Sharing** is enabled in the *Shortcuts* app settings.
2. Open the iCloud link from Safari on your iPad and tap **Add Shortcut**.
3. Configure any required API keys (OpenAI or Gemini) when prompted.

For Python projects:

1. Use an app like Pythonista or Carnets to run Python code on iPad.  Alternatively, run the projects on a separate server and interact via API.
2. Follow the repository instructions to install dependencies, set environment variables (e.g., `OPENAI_API_KEY`, `GDRIVE_FOLDER_ID`) and run the server.

---

This repository provides a curated set of links and documentation rather than duplicating copyrighted code.  Refer to the linked projects for full source code and installation instructions.

