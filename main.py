from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

# Constants
API_URL = "https://api.open-meteo.com/v1/forecast"


async def get_weather(latitude: str, longitude: str) -> dict[str, Any] | None:
    """Make a request to the Open Meteo API with proper error handling."""

    # Make the request
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                API_URL,
                params={
                    "latitude": latitude,
                    "longitude": longitude,
                    "timezone": "auto",
                    "current": "temperature_2m,rain,precipitation,wind_speed_10m,wind_direction_10m",
                    "daily": "temperature_2m_max,temperature_2m_min,sunrise,sunset",
                },
                timeout=30.0,
            )
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """
    # Get the forecast URL from the points response
    data = await get_weather(latitude, longitude)

    if not data:
        return "Unable to fetch detailed forecast."

    return data


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
