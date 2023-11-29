from pathlib import Path

import openai
from my_moduls.config_handler import ConfigHandler

config_handler = ConfigHandler()
openai.api_key = config_handler.get_value(["api_keys", "openAI", "key"])


class Generator:
    @staticmethod
    def get_idea(idea):
        return openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Сгенерируй пожалуйста идею '{idea}'"},
            ]
        ).choices[0].message.content

    @staticmethod
    def get_image(prompt):
        return openai.images.generate(
            model="dall-e-3",
            prompt=f"{prompt}",
            size="1024x1024",
            quality="standard",
            n=1,
        ).data[0].url

    @staticmethod
    def rephrase_and_vocalize(base_phrase):
        result_of_rephrase = Generator.get_rephrase(base_phrase)
        Generator.get_audio_from_text(result_of_rephrase)

    @staticmethod
    def get_audio_from_text(text):
        speech_file_path = Path(__file__).parent / "speech.mp3"
        response = openai.audio.speech.create(
            model="tts-1-hd",
            voice="nova",
            input=text,
        )
        response.stream_to_file(speech_file_path)

    @staticmethod
    def get_rephrase(base_phrase):
        return openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Перефразируй пожалуйста '{base_phrase}'"},
            ]
        ).choices[0].message.content
