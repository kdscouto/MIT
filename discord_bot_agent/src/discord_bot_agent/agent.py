"""Implementação do agente Discord."""
from __future__ import annotations

import logging
from typing import Any

import discord

logger = logging.getLogger(__name__)


class DiscordAgent(discord.Client):
    """Agente que se conecta a um bot do Discord usando a biblioteca discord.py."""

    def __init__(self, *, intents: discord.Intents | None = None) -> None:
        intents = intents or discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

    async def setup_hook(self) -> None:  # type: ignore[override]
        logger.info("Agente Discord inicializado e pronto para conectar.")

    async def on_ready(self) -> None:  # type: ignore[override]
        logger.info("Conectado como %s (ID: %s)", self.user, self.user and self.user.id)

    async def on_message(self, message: discord.Message) -> None:  # type: ignore[override]
        if message.author == self.user:
            return

        logger.debug("Mensagem recebida de %s: %s", message.author, message.content)

        if message.content.startswith("!ping"):
            await self._handle_ping(message)

    async def _handle_ping(self, message: discord.Message) -> None:
        """Responde a comandos simples, como !ping."""
        await message.channel.send("Pong! 🏓")
        logger.info("Resposta enviada para %s", message.author)

    async def send_startup_message(self, channel_id: int) -> None:
        """Envia uma mensagem inicial para um canal específico."""
        channel = self.get_channel(channel_id)
        if channel is None:
            logger.warning("Canal com ID %s não encontrado.", channel_id)
            return

        if isinstance(channel, (discord.TextChannel, discord.Thread)):  # type: ignore[arg-type]
            await channel.send("Agente conectado e pronto para ajudar! 🤖")
            logger.info("Mensagem inicial enviada para o canal %s", channel_id)
        else:
            logger.warning("Canal com ID %s não é um canal de texto.", channel_id)

