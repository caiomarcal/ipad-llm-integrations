"""
Script to transcribe audio files using Google Speech-to-Text and summarize using ChatGPT.
"""

import os

try:
    import openai
    from google.cloud import speech_v1p1beta1 as speech
except ImportError:
    print("Please install 'openai' and 'google-cloud-speech' packages before running this script.")
    raise

def transcribe_audio(audio_path, language_code="en-US"):
    """Transcribes an audio file to text using Google Cloud Speech-to-Text."""
    client = speech.SpeechClient()
    with open(audio_path, "rb") as f:
        content = f.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code=language_code,
    )
    response = client.recognize(config=config, audio=audio)
    return " ".join([result.alternatives[0].transcript for result in response.results])

def summarize_text(text):
    """Summarizes text using OpenAI's ChatGPT API."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": f"Summarize the following notes:\n\n{text}"}],
        max_tokens=200,
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()

def append_to_file(file_path, summary):
    with open(file_path, "a") as f:
        f.write("\n\nSummary:\n")
        f.write(summary)

def process_audio_file(audio_path, note_path):
    transcript = transcribe_audio(audio_path)
    summary = summarize_text(transcript)
    append_to_file(note_path, summary)
    print(f"Processed {audio_path} and appended summary to {note_path}")

if __name__ == "__main__":
    # Example usage
    AUDIO_FILE = "path/to/audio.wav"
    NOTE_FILE = "path/to/notes.txt"
    process_audio_file(AUDIO_FILE, NOTE_FILE)
