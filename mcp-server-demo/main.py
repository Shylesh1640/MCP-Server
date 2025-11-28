from fastmcp import FastMCP

# Create MCP Server (must be global)
mcp = FastMCP("Demo", json_response=True)

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"

@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    styles = {
        "friendly": "Warm, friendly greeting",
        "formal": "Formal, professional greeting",
        "casual": "Casual, relaxed greeting"
    }
    return f"{styles.get(style,'friendly')} for {name}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
