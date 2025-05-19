import os
from dotenv import load_dotenv
from huggingface_hub import login
from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel

# Load token
load_dotenv()
token = os.getenv("HUGGINGFACE_TOKEN")
login(token=token)

# Use a compatible, free chat model
model = InferenceClientModel(model="HuggingFaceH4/zephyr-7b-beta")

# Create the agent
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model
)

# Run the agent
agent.run("What's something cool I can cook with eggs and bread?")