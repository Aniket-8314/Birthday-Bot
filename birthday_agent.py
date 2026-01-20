import os
import sys
import asyncio
from dotenv import load_dotenv

from droidrun import DroidAgent
from droidrun.config_manager.config_manager import DroidrunConfig, AgentConfig, LoggingConfig
from llama_index.llms.google_genai import GoogleGenAI

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    sys.exit("Error: GOOGLE_API_KEY not found.")

async def main():
    print("--- Starting BirthdayBot Agent ---")
    
    # 1. Setup Configuration
    config = DroidrunConfig(
        agent=AgentConfig(
            max_steps=50,       
            reasoning=True,     
        ),
        logging=LoggingConfig(
            debug=True, 
            save_trajectory="action", 
            rich_text=True
        ),
    )

    # 2. Setup the LLM
    print("Initializing Gemini 2.5 Flash...")
    llm = GoogleGenAI(
        model="models/gemini-2.5-flash",
        api_key=api_key,
        temperature=0.7 
    )

    # 3. Define the Goal
    # LOGIC: Calendar -> Generate Creative Text -> WhatsApp
    goal = (
        "You are a social assistant. Please perform the following tasks: "
        "1. Open the 'Google Calendar' app. "
        "2. Look at today's events. If you see an event titled 'Birthday' (e.g., 'Rahul Birthday'), extract the name. "
        "3. Generate a short, funny birthday wish for that person (e.g., 'Happy Birthday Rahul! Hope you don't debug code today!'). "
        "4. Open 'WhatsApp' and search for that person's name. "
        "5. Send the generated birthday wish to them. "
        "6. Return to the home screen."
    )

    print(f"Goal set: {goal}")

    # 4. Create the Agent
    agent = DroidAgent(
        goal=goal,
        config=config,
        llms=llm,
    )

    # 5. Run it!
    print("Agent is running... (Monitor the emulator)")
    result = await agent.run()

    if result.success:
        print("\nSuccess! Birthday wish sent.")
    else:
        print("\nFailed.")
        print(f"Error: {result.reason}")

if __name__ == "__main__":
    import warnings
    warnings.filterwarnings("ignore", category=FutureWarning)
    asyncio.run(main())