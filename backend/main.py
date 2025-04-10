# author: Giorgio
# date: 23.08.2024
# topic: TikTok-Voice-TTS
# version: 1.3

from codecs import BOM_UTF32
import argparse
# the script in the directory
from tiktok_voice import tts, Voice

def run_tts(text: str, voice_name: str, output_file: str = "output.mp3", play: bool = False):
    voice: Voice | None = Voice.from_string(voice_name)
    if voice is None:
        raise ValueError("No valid voice has been selected")

    tts(text, voice, output_file, play)
