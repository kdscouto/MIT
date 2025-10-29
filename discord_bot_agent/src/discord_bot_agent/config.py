"""Configurações do agente Discord."""
from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class DiscordSettings:
    """Configurações necessárias para conectar ao Discord."""

    token: str
    default_channel_id: int | None = None


def load_settings() -> DiscordSettings:
    """Carrega as configurações a partir do arquivo `.env` ou variáveis de ambiente."""
    load_dotenv()

    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError(
            "Variável de ambiente DISCORD_TOKEN não definida. "
            "Crie um arquivo .env ou defina a variável antes de executar o agente."
        )

    channel_id_raw = os.getenv("DISCORD_DEFAULT_CHANNEL_ID")
    channel_id = int(channel_id_raw) if channel_id_raw else None

    return DiscordSettings(token=token, default_channel_id=channel_id)

