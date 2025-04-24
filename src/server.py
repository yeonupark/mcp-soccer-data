from mcp.server.fastmcp import FastMCP
import httpx
import os

mcp = FastMCP("soccer-data")

API_END_POINT = "https://api.soccerdataapi.com/"
AUTH_KEY = os.environ.get("AUTH_KEY")

if not AUTH_KEY:
    raise EnvironmentError("AUTH_KEY is not set in .env")

@mcp.tool()
async def get_livescores():

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