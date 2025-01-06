from config import groq_client as client
from telegram_sample_data import generate_sample_telegram_data

telegram_data = generate_sample_telegram_data()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Extract entities from user query.\nRespond with the list of entities only! Nothing else!"
        },
        {
            "role": "user",
            "content": telegram_data[2].text,
        }
    ],
    model="gemma2-9b-it",
    temperature=0,
    max_tokens=128,
)

print(f"Telegram sample data:\n"
      f"- Text: '{telegram_data[2].text}'\n"
      f"- Entities: {', '.join(telegram_data[2].entities)}")
# Telegram sample data:
# - Text: 'Breaking: Major tech conference announces keynote speakers for upcoming AI summit.'
# - Entities: AI summit, tech conference

print("\nExtracted entities by LLM:")
print(chat_completion.choices[0].message.content)
# Extracted entities by LLM:
# tech conference, keynote speakers, AI summit
