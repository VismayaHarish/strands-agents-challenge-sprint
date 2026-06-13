import os
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from strands import Agent
from strands.tools.mcp import MCPClient
from mcp import StdioServerParameters, stdio_client

MODEL = "amazon.nova-pro-v1:0"

aws_docs_mcp = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="awslabs.aws-documentation-mcp-server"
        )
    )
)

with aws_docs_mcp:
    tools = aws_docs_mcp.list_tools_sync()

    agent = Agent(
        model=MODEL,
        tools=tools,
        system_prompt="You are an AWS Documentation Assistant. Use MCP tools to answer AWS questions."
    )

    print("AWS Documentation Assistant Ready!")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["quit", "exit", "q"]:
            break

        response = agent(user_input)

        print("\nAgent:", response)
        print()