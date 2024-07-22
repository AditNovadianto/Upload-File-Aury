import assemblyai as aai
import streamlit as st

# Replace with your API key
aai.settings.api_key = "c2281c3d43304ce9a2d9afe238ae67ff"

# You can also transcribe a local file by passing in a file path
FILE_URL = './files/recording_4.mp3'

config = aai.TranscriptionConfig(speaker_labels=True)

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(
  FILE_URL,
  config=config
)

for utterance in transcript.utterances:
  st.write(f"Speaker {utterance.speaker}: {utterance.text}")
