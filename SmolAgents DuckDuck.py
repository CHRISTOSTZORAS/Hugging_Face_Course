from huggingface_hub  import login
from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("HUGGINGFACE_TOKEN")
login(token=token)
agent= CodeAgent(tools=[DuckDuckGoSearchTool()],model=InferenceClientModel())
agent.run("Search for the best music recommendations for a party at the Wayne's mansion.")

