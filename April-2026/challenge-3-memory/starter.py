import os
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from strands import Agent
from strands_tools import mem0_memory

MODEL = "amazon.nova-pro-v1:0"

agent = Agent(
    model=MODEL,
    tools=[mem0_memory],
    system_prompt="Store and recall user preferences and facts."
)

print("Memory Agent Ready!")
print("Try: Remember that my name is Vismaya and I love pasta")
print("Then: What's my name and what food do I like?")
print("Type 'quit' to exit.\n")

while True:
    try:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "q"):
            print("Bye!")
            break

        response = agent(user_input)

        print("Agent:", response)

    except KeyboardInterrupt:
        print("\nBye!")
        break

print("\nChallenge 3 complete!")