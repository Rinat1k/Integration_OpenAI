import openai
from my_moduls.config_handler import ConfigHandler
config_handler = ConfigHandler()
openai.api_key = config_handler.get_value(["api_keys", "openAI", "key"])

if __name__ == '__main__':
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Придумай идею для ресторона шеф"},
        ]
    )
    reply = response.choices[0].message.content
    print(reply)