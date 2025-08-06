# Auto-install scripts and integrations

Este diretório contém scripts e recursos para automatizar a integração entre modelos de linguagem (ChatGPT, Gemini), Siri e serviços de armazenamento (Google Drive, iCloud) no iPadOS 26. Use os scripts para clonar repositórios e instalar dependências. Em seguida, importe os atalhos via iCloud para configurar fluxos poderosos.

## Scripts

### setup.py
Clona e instala automaticamente:
- gdrive-chatgpt: Integra Google Drive com ChatGPT.
- ChatGPT‑GDrive‑Integration: Integração com LangChain e Chroma DB.
- sheetgpt: Funções para usar ChatGPT em Google Sheets.
- gpt-google-sheets: Conecta GPT às planilhas via Apps Script.

Após rodar o script, configure as variáveis de ambiente `OPENAI_API_KEY`, `GOOGLE_API_KEY` e `GDRIVE_FOLDER_ID`.

### Próximos scripts
- **integrate_notes.py** – Conecta anotações e transcrições de áudio com ChatGPT e Gemini.
- **voice_assistant.py** – Cria uma interface de voz personalizada usando a ação “Use Model” no Atalhos.

## Atalhos para importar

Links iCloud dos atalhos recomendados:
- ChatGPT Siri – <https://www.icloud.com/shortcuts/debc9a9029854473b515414cc7766b47>
- Notefy – <https://www.icloud.com/shortcuts/219e814900024849845fd0f7e8d36592>
- Share‑to‑ChatGPT – <https://www.icloud.com/shortcuts/25262952f34544e99b9e6678056c1168>

Copie estes links e abra no Safari do seu iPad para adicionar rapidamente os atalhos. Para atalhos premium como Pro AI ou Apple Intelligence, consulte os tutoriais no RoutineHub.

## Integração com GitHub e Operator

Este projeto serve como base para automações avançadas. Utilize o GPT Operator para executar scripts deste repositório no seu ambiente local ou servidor. Ajuste os scripts conforme necessário para incluir novas integrações (Notion, AirTable, APIs externas). Se tiver código próprio que drible limitações, adapte-o aqui para automatizar ainda mais o seu fluxo.
