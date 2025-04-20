# Weather MCP Server

This is a simple MCP server that fetches weather forecasts from the [Open-meteo](https://open-meteo.com) for a given location.

# Running the server

- Python 3.11 or higher is required.

I am using [uv](https://docs.astral.sh/uv/) (An extremely fast Python package and project manager, written in Rust.)

Install `uv` if not already installed.

```bash
# mac/linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
