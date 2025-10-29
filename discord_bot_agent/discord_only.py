from dotenv import load_dotenv
from openai import OpenAI
import discord
import os
import asyncio

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY environment variable not set")

oa_client = OpenAI(api_key=OPENAI_API_KEY)

async def call_openai(question: str) -> str:
    def _sync_call(q: str):
        response = oa_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"Responda a seguinte pergunta como um pirata: {q}"}
            ]
        )
        return response.choices[0].message.content

    return await asyncio.to_thread(_sync_call, question)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello')

    if message.content.startswith('$question'):
        print(f"Message: {message.content}")
        message_content = message.content.split("$question", 1)[1].strip()
        print(f"Question: {message_content}")
        try:
            response = await call_openai(message_content)
        except Exception as e:
            print("OpenAI error:", e)
            await message.channel.send("Erro ao chamar o OpenAI.")
            return
        print(f"Assistant: {response}")
        await message.channel.send(response)

token = os.getenv('DISCORD_TOKEN')
if not token:
    raise RuntimeError("DISCORD_TOKEN environment variable not set")

client.run(token)
