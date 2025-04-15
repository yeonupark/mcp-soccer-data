# ⚽️ Soccerdata MCP Server
- **MCP-Soccerdata** is an open-source [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that connects to the **SoccerDataAPI to deliver up-to-date football match information via natural language interactions**. 

- Designed for use with MCP-enabled clients such as Claude Desktop, it allows users to retrieve football data by leveraging large language models (LLMs).

---

## ✨ Features

### 🏟️ Live Football Match Insights
MCP-Soccerdata focuses on delivering real-time information about ongoing football matches around the world. 

> "What football matches are being played right now?"      
> → Returns a list of live matches with detailed breakdowns


### - Match Listings & Basic Info
- Global list of all currently active matches
- Home and away team names
- Kickoff time and match date
- Stadium details
- Current score


### - Match Details
- Match status: scheduled, in progress, or finished
- Goal breakdown: first half, second half, extra time, penalty shootout
- Final result: win, draw, or loss


### - Key Match Events
- Goal events (who scored, when, how)
- Substitutions
- Yellow and red cards
- Penalties


### - Team Lineups
- Starting XI
- Bench players
- Injury status
- Team formation


### - Odds & Betting Information
- Win / Draw / Lose odds
- Over / Under odds
- Handicap betting odds


### - League Metadata
- League name
- Country
- Competition format (e.g., regular season, knockout stage)


> ⚠️ Focused exclusively on **live**, **upcoming**, and **recently finished** matches

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- `uv` package manager
- Soccerdata API account
- MCP-compatible client (e.g., Claude for Desktop)

---

### 1. Clone and Setup

- Clone the repository
```bash
git clone https://github.com/yourusername/mcp-soccer-data.git
cd mcp-soccer-data
```
- Install dependencies
```
uv sync
```

### 2. Get Your API Key and Set Environment

- Create a .env file with your credentials:
```
AUTH_KEY=your_auth_key
```
> Sign up on https://soccerdataapi.com/ and get your own Auth keys.

### 3. Configure MCP Client
- Register this server in your MCP client (e.g., Claude for Desktop).

Edit `~/Library/Application Support/Claude/claude_desktop_config.json:`
```
{
  "mcpServers": {
      "mcp-soccer-data": {
          "command": "/ABSOLUTE/PATH/TO/PARENT/FOLDER/uv",
          "args": [
              "--directory",
              "/ABSOLUTE/PATH/TO/PARENT/FOLDER/src/",
              "run",
              "--env-file",
              "/ABSOLUTE/PATH/TO/PARENT/FOLDER/.env",
              "server.py"
          ]
      }
  }
}
```

---
## 📝 License
- This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.
- Built with [Model Context Protocol](https://modelcontextprotocol.io/introduction)