import os
import subprocess

# Clone a git repository into dest if it does not already exist
def clone_repo(url, dest):
    if not os.path.exists(dest):
        subprocess.run(["git", "clone", url, dest], check=True)

# Repositories to clone for various integrations
repos = {
    "gdrive-chatgpt": "https://github.com/fonckchain/gdrive-chatgpt.git",
    "chatgpt-gdrive-integration": "https://github.com/robson-koji/ChatGPT-GDrive-Integration.git",
    # Additional repos for more resources and features
    "sheetgpt": "https://github.com/umaxfun/sheetgpt.git",
    "gpt-google-sheets": "https://github.com/MoritzLaurer/gpt-google-sheets.git",
}

# Clone each repository and install its Python dependencies if a requirements file exists
for name, url in repos.items():
    clone_repo(url, name)
    req_file = os.path.join(name, "requirements.txt")
    if os.path.exists(req_file):
        subprocess.run(["pip", "install", "-r", req_file], check=True)

print("Repositories cloned and dependencies installed.")
print("Please set OPENAI_API_KEY, GOOGLE_API_KEY, and GDRIVE_FOLDER_ID as environment variables where applicable.")
