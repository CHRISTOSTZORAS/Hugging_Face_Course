from smolagents import CodeAgent,tool,InferenceClientModel
from huggingface_hub import InferenceClient
@tool
def suggest_menu(occasion:str)->str:
    """
    Suggests a menu based on the occasion
    Args:
        occasion (str): The type of occasion for the party.Allowed values are:
        -"casual": Menu for casual party.
        -"formal": Menu for formal party.
        -"superhero": Menu for superhero party.
        -"custom": Menu for custom party.
    """
    if occasion=="casual":
        return "Pizza,snacks, and drinks."
    elif occasion=="formal":
        return "3-course dinner with wine and dessert."
    elif occasion=="superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."
# ✅ Step 1: Create client with correct model
client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.1")

# ✅ Step 2: Use it in InferenceClientModel explicitly
model = InferenceClientModel(client=client)

# ✅ Step 3: Create agent with this model
agent = CodeAgent(tools=[suggest_menu], model=model)

# ✅ Step 4: Run
output = agent.run("Prepare a formal menu for the party")
print(output)

