from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI # use langchain_openai if you will -> ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import random

load_dotenv() # load you api key

rand_temp = random.random()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=rand_temp)

@tool
def calculator(numbers: list[float]) -> str:
    """a simple calculator to perform some basic math operations"""
    if len(numbers) == 1:
        return f"it's just that! {numbers[0]}"
    elif len(numbers) == 2:
        return f"the sum of these two numbers are {sum(numbers)}"
    else:
        return f"the sum of all of these numbers are {sum(numbers)}"


@tool
def greet_someone(name: str = "friend") -> str:
    """a tool to great someone that related to the user"""
    prompt = f"Create a greeting statement to the user's friend named {name}, make it formal, polite, and cheerful, and under 25 words."
    return model.invoke(prompt).content

def main():

    tools = [calculator, greet_someone]
    agent_executor = create_react_agent(model, tools)

    print("Welcome to your AI assistant. just ask and I will help you with anything, press q or type quit, to exit")
    print("You can ask me to performe some calculations or chat with me (but don't be annoying)")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ['q', 'quit', 'get out of here']:
            break
        
        print("Assistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages" : [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk['agent']:
                for message in chunk['agent']['messages']:
                    print(message.content, end="")
        print()


if __name__ == "__main__":
    main()