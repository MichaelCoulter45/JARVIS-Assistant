A Python-based Windows deaktop automation application inspired by Marvel's Jarvis. 

Status: Active Development



What is JARVIS-Assistant?

JARVIS-Assistant is a Windows deaktop tool that can understand natural language commands and perform actions on the user's computer. The long term goal is to create a personal assistant capable of interacting with the PC through natural language.


Why I built it:

I was inspired by the Jarvis from Marvel's Ironman series and wanted to make my very own personal AI assistant. This was way before I knew anything about programming, and one of the many reasons why I chose to pursue Computer Science. 


What it can currently do:

JARVIS-Assistant currently understands the user's intent and what action to perform on the user's target. 

User's command --> Detect Intention --> Identify Target --> Find Target --> Dispatch Action --> Computer Action.

ie: "Open Chrome" goes through a pipeline through the AI to figure out what the user's intention is, what the target is, where the target is, and a dispatcher decides what happens to the target. In this case, the target is chrome and the intended action is to open it.


How the architecture works:

User --> Command Input --> Intent Parser --> Intent & Target --> Target Discovery --> Dispatcher --> System Action

The user inputs a command into the program --> The command gets split and parsed into two different sections - Intent and Target --> The program searches the computer's files to find and return the target's path --> the Intent gets passed to the Dispatcher --> The Dispatcher decides what function is called and passes the target to the appropirate function --> The application performs the detected intended action given by the user.


Technologies used: 
- Python
- pathlib -- filesystem & path handling
- subprocess -- launching / interacting with processes
- shutil -- filesystem utilities
- functools -- caching with lru_cache
- os -- windows / system interaction


Example commands:
find, open, launch, execute


Roadmap:
Current:
- Natural language intent parsing
- Target Discovery
- Application Handling
- Filesystem search
- Path caching


Next:
- Better target discovery
- Cache validation
- Discovery Support
- More robust Windows application detection
- Multiple target handling


Future:
- Voice activation
- "Hey Jarvis"
- Voice input and output
- Expand computer interaction


How to run it:
TBD


Development/version history:
v0.01 -- Initial prototype
v0.02 -- 
v0.03 -- current development version


Design Philosophy / Project Goals:
Build a modular desktop assistant that can interpret human commands, determine the user's intended action, locate the relevant target, and interact with the Windows environment.
