import openai
openai.api_key = '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'

if __name__ == '__main__':
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Придумай идею для ресторона шеф"},
        ]
    )
    reply = response.choices[0].message.content
    print(reply)