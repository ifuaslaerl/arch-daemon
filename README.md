# Arch Daemon - Python Discord Bot

<p align="center">
  <a href="https://discord.gg/xj6y5ZaTMr"><img src="https://img.shields.io/discord/1358456011316396295?logo=discord"></a>
  <a href="https://github.com/kkrypt0nn/Python-Discord-Bot-Template/commits/main"><img src="https://img.shields.io/github/last-commit/kkrypt0nn/Python-Discord-Bot-Template"></a>
  <a href="https://github.com/kkrypt0nn/Python-Discord-Bot-Template/blob/main/LICENSE.md"><img src="https://img.shields.io/github/license/kkrypt0nn/Python-Discord-Bot-Template"></a>
  <a href="https://github.com/kkrypt0nn/Python-Discord-Bot-Template"><img src="https://img.shields.io/github/languages/code-size/kkrypt0nn/Python-Discord-Bot-Template"></a>
  <a href="https://conventionalcommits.org/en/v1.0.0/"><img src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white"></a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

This repository is built upon the **Python Discord Bot Template** created by Krypton, providing a solid foundation for a Python-based Discord bot.

This extended version is tailored for learning and supporting self-hosted applications, featuring dedicated tools for Minecraft server management.

If you plan to use this template to make your own template or bot, you **have to**:

- Keep the credits, and a link to this repository in all the files that contains my code
- Keep the same license for unchanged code

See [the license file](LICENSE.md) for more information.

---

## 🚀 Key Features

This bot is built using `discord.py` and uses **Hybrid Commands** (supporting both prefix and slash commands).

### Core Functionality (from original template)

* **Owner Commands:** Synchronize slash commands, load/unload/reload extensions, and bot shutdown (`/sync`, `/load`, etc.).
* **General Commands:** Help menu, latency check (`/ping`), and invite links (`/invite`).
* **Logging:** Comprehensive colored logging to console and persistent logging to a `discord.log` file.

### Custom Extensions (Self-Hosting Support)

* **Minecraft Server Management (`minecraft` cog):**
    * `/status`: Check the online status, player count, and latency of a Minecraft Java server (`mcstatus` dependency).
    * `/mc`: Send commands directly to the server console via RCON (Owner-only command, `aio-mc-rcon` dependency).
* **Discord Log Forwarder:** The `discord_logger.sh` script monitors `discord.log` and pushes new log lines to a configurable Discord Webhook (`WEBHOOK_URL_ENV`).

---

## 🛠️ How to Set Up

To set up the bot, you will need to configure environment variables.

1.  **Rename `.env.example` to `.env`** and replace the placeholders with your actual values.
2.  **Add all required environment variables** to your `.env` file or as system environment variables:

| Variable | Descriptioni |
| :--- | :--- | 
| `TOKEN` | Your Discord Bot Token. |
| `PREFIX` | The prefix for normal commands (e.g., `!` or `$` for fallback). | 
| `INVITE_LINK` | The full invite URL for your bot. |
| `WEBHOOK_URL_ENV` | The Discord Webhook URL for the log forwarder script. | 
| `MC_HOST` | The internal IP or hostname of your Minecraft server. | 
| `MC_PORT` | The port for Minecraft status checks (default: `25565`). | 
| `RCON_PORT` | The port for RCON commands (default: `25575`). | 
| `RCON_PASSWORD` | The RCON password for console access. | 
| `MC_PUBLIC_ADDRESS` | The public address string to show users for joining. | 

---

## ▶️ How to Start

To start the log forwarder, run the script (requires environment variables to be sourced, like via `source .env` or Docker):
    ```
    bash discord_logger.sh
    ```

### Docker

Support to start the bot in a Docker container is included.

1.  Make sure you have [Docker](https://docker.com) installed.
2.  Execute the following command, which will build the image, install dependencies, and run the container using the variables defined in your local `.env` file:
    ```
    docker compose up -d --build
    ```

---

## ℹ️ Disclaimer

Slash commands can take some time to get registered globally. If you want to test a command immediately, you should use the `@app_commands.guilds()` decorator (as explained in the template's original documentation).

When using this code, you confirm that you have read the [LICENSE.md](LICENSE.md) and comprehend that the template creator reserves the right to take down any repository that does not meet the specified requirements, particularly keeping the credits for the original code.

## Built With

- [Python 3.12.9](https://www.python.org/)
- `discord.py==2.6.3`

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details.
