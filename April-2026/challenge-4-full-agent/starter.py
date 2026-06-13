import os
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from datetime import datetime
from strands import Agent, tool
from strands_tools import calculator, mem0_memory


def stream_callback(**kwargs):
    if "data" in kwargs:
        print(kwargs["data"], end="", flush=True)
    elif "current_tool_use" in kwargs and kwargs["current_tool_use"].get("name"):
        print(f"\nUsing tool: {kwargs['current_tool_use']['name']}")


@tool
def weather(city: str) -> str:
    """Get the current weather for a city.
    Args:
        city: The name of the city.
    """
    return f"The weather in {city} is sunny, 28°C."


@tool
def age_calculator(birth_date: str) -> str:
    """Calculate age from a birth date.
    Args:
        birth_date: Date of birth in YYYY-MM-DD format.
    """
    dob = datetime.strptime(birth_date, "%Y-%m-%d").date()
    today = datetime.today().date()
    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    return f"Age: {age} years old."


agent = Agent(
    model="amazon.nova-pro-v1:0",``
    tools=[calculator, weather, age_calculator, mem0_memory],
    callback_handler=stream_callback,
    system_prompt="You are a full AI agent. You can calculate, check weather, calculate age, and remember user preferences. Use tools when needed. Keep answers brief."
)

print("Full Agent Ready! Type 'quit' to exit.")
print("Try: 'What is 365 * 24 and how old is someone born on 2000-01-01?'")
print("Try: 'What's the weather in Delhi?'\n")

while True:
    try:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "q"):
            print("Bye!")
            break

        print("\nAgent: ", end="")
        response = agent(user_input)

        if response:
            print(response)

        print()

    except KeyboardInterrupt:
        print("\nBye!")
        break

print("\nChallenge 4 complete!")