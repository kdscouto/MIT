# Discord Bot Agent

Projeto Python para criação de um agente que se conecta a um bot do Discord.

## Requisitos

- Python 3.10 ou superior
- Token de bot do Discord

## Configuração

1. Copie o arquivo `.env.example` para `.env` e atualize a variável `DISCORD_TOKEN` com o token do seu bot.
2. Instale as dependências:
   ```bash
   python -m pip install .[dev]
   ```
3. Execute o agente:
   ```bash
   python -m discord_bot_agent
   ```

## Estrutura do projeto

- `pyproject.toml`: configurações do projeto e dependências.
- `src/discord_bot_agent/agent.py`: lógica principal do agente.
- `src/discord_bot_agent/main.py`: ponto de entrada para execução.
- `src/discord_bot_agent/config.py`: gerenciamento de configuração e variáveis de ambiente.

## Desenvolvimento

Com as dependências de desenvolvimento instaladas, você pode executar o Ruff e o MyPy:

```bash
ruff check src
mypy src
```

