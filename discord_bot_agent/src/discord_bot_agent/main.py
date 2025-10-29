"""Ponto de entrada para execução do agente Discord."""
from __future__ import annotations

import asyncio
import logging

from .agent import DiscordAgent
from .config import DiscordSettings, load_settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


async def _start_agent(settings: DiscordSettings) -> None:
    """Inicializa o agente com as configurações carregadas."""
    agent = DiscordAgent()
    async with agent:
        await agent.start(settings.token, reconnect=True)


async def _run_with_startup(settings: DiscordSettings) -> None:
    """Executa o agente e envia uma mensagem inicial se configurada."""
    agent = DiscordAgent()

    @agent.event  # type: ignore[misc]
    async def on_ready() -> None:
        logging.getLogger(__name__).info("Agente pronto e conectado.")
        if settings.default_channel_id is not None:
            await agent.send_startup_message(settings.default_channel_id)

    async with agent:
        await agent.start(settings.token, reconnect=True)


def run() -> None:
    """Carrega as configurações e executa o agente."""
    settings = load_settings()

    try:
        if settings.default_channel_id is not None:
            asyncio.run(_run_with_startup(settings))
        else:
            asyncio.run(_start_agent(settings))
    except KeyboardInterrupt:
        logging.getLogger(__name__).info("Execução interrompida pelo usuário.")


if __name__ == "__main__":
    run()

