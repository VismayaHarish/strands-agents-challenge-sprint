import os
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from datetime import datetime
from strands import Agent, tool
from strands_tools import calculator


MODEL = "amazon.nova-pro-v1:0"


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
    model=MODEL,
    tools=[calculator, weather, age_calculator],
    system_prompt="You are a helpful assistant. Use tools when needed and keep answers brief."
)

print("Math test:")
response = agent("What is 42 * 17?")
print(response)

print("\nWeather test:")
response = agent("What's the weather in Chennai?")
print(response)

print("\nAge test:")
response = agent("How old is someone born on 2000-05-15?")
print(response)

print("\nChallenge 2 complete!")