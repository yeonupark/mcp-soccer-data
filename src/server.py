from mcp.server.fastmcp import FastMCP
import httpx
import os

# Initialize FastMCP server
mcp = FastMCP("soccer-data")

API_END_POINT = "https://api.soccerdataapi.com/"
AUTH_KEY = os.environ.get("AUTH_KEY")

@mcp.tool(
    name="get_livescores",
    description="Get live football scores from SoccerDataAPI",
)
async def get_livescores():
    """
    Get current live football scores using SoccerDataAPI.

    Returns:
        JSON text with live match data.
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(
            API_END_POINT+"livescores/",
            params={"auth_token": AUTH_KEY},
            headers={
                "Content-Type": "application/json",
                "Accept-Encoding": "gzip",
            },
        )

        response.raise_for_status()

        return response.text


if __name__ == "__main__":
    mcp.run()