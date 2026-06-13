from strands import Agent

agent = Agent(
    model="amazon.nova-pro-v1:0",
    tools=[],
    system_prompt="You are a helpful assistant. Be brief."
)

response = agent("Tell me a fun fact about Python programming")

print("Agent:", response)

print("\nChallenge 1 complete!")