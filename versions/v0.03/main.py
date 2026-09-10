# main.py
import subprocess
import shutil
import os
from functools import lru_cache
from pathlib import Path



""" ## Current Known Bugs ##
1. XX user input isn't parsing correctly. Check the two command functions.
2. XX Script crashes when inputting an incorrect command or 'q' for missing values.
3. XX The only command now opens chrome despite naming firefox or others in objects[]
4. XX Currently only hard coded objects are supported. Fix it to make dynamic.
5. Caching is vulnerable to becoming stale if the file is moved, uninstalled, or reinstalled.
"""
###
""" ## Things to do: ##
1. XX Make it so only the first word in user_input is the verb, and the rest is the object.
2. XX Update process_user_input(). 
3. Improve Cache application-path validation.
4. Add any and all drives to the search.
5. Add option to target search a drive/directory.
6. Add more likely directories.
7. Replace lru_cache with a saved to disk cache system.
8. Add layer to Caching system in-case the cache path is no longer existing. ie) reinstall a program
9. XX Make a safe guard for when the user inputs nothing or " ", where user_input[0] doesn't exist.

... After enabling speak to text, Add "Hey Jarvis, ..." for the program to listen to the command, ignoring everything else to prevent accidental commands. 
"""


# Hotkeys
hotkey_quit = 'q'

# Settings
active = True

###############
def toggle_active():
    global active
    active = not active
###############





###################################
###################################
def ask_for_command():
    print(f"\nWhat can I do for you today? [Enter 'Q' to quit.]")
    user_input = input()
    user_input = user_input.strip().split()
    if user_input:
        if user_input[0] == hotkey_quit and len(user_input) == 1:
            return toggle_active()
        
        user_verb, user_object = process_user_input(user_input)
        intent = find_user_intent(user_verb)
        dispatch(intent, user_object)
    else:
        print(f"You didn't enter anything..")
###################################
def process_user_input(user_input):
    """ 
    Returns an action and the target object from the user's input.
    """
    
    # All other words in user's input is the object.
    action, *rest_of_list = user_input
    target_object = " ".join(rest_of_list)
    
    if len(user_input) < 2:
        print(f"What do you mean by '{user_input}'?\n")
        return action, target_object
    
    # end of function
    return action, target_object
###################################
def find_user_intent(user_verb):
    matched_intent = intent_map.get(user_verb, "Unknown Intent")
    # print(f"User Input: {user_verb} -> Matched Intent: {matched_intent}") #  debugging
    return matched_intent
###################################
def dispatch(intent, user_object): 
    if user_object:
        if intent in command_map:
            command_map[intent](user_object)
        else:
            print(f"I don't understand what you're trying to do with {user_object}")
    else:
        print(f"I don't understand what you're trying to do.")
###################################
###################################
@lru_cache
def find_path(user_object): # <---------------------------------------------------------------- Fix this function.
    """Searches some likely directories first, then the whole C drive."""
    likely_directories = ["C:\\Program Files", 
                            "C:\\Program Files (x86)",
                            "C:\\"]
    path = []
    if shutil.which(user_object):
        path.join(shutil.which(user_object))
        
    # Search loop using likely directories and then the whole drive
    for directory in likely_directories:
        print(f"Searching '{directory}' for {user_object}")
        if path:
            break
        for root, dirs, files in os.walk(directory):
            # print(root, dirs, files) # Debugging
            if user_object in files:
                path.join(os.path.join(root, user_object))
                print(f"path: {path}")
    
    if path:
        print(f"Found {user_object} at: ", path)
        return path
    print(f"Could not find {user_object}")
###################################
def open_application(user_object):
    print(f"Executing: '{user_object}'\n")
    user_object = user_object + ".exe"
    target_app = find_path(user_object)
    if target_app:
        print(f"Found at: {target_app}") # Debugging
        subprocess.Popen([target_app])
    else:
        print(f"Cannot find: {user_object}.\n")
###################################
def close_application(user_object):
    print(f"Closing {user_object}...")
    target_path = find_path(user_object)
    target = Path(target_path)
    subprocess.call('taskkill', '/IM', f'{target.name}')
###################################
def open_target(target): # <---------------- Make this function responsable to open already found paths. Not to find new paths.
    """
    Currently searches the entire C:/ drive from find_path() even if found early. 
    This is to find any and all files with the same name. 
    Launches the default app of the target regaurdless of file type and directory. 
    """
    candidates = find_path(target)
    
    # No matches
    if not candidates:
        print(f"Cannot find {target}")
        return None
    
    else:
        for dir in candidates:
            candidates[dir] = Path(dir)
        
        print(candidates) # Debugging
        
        # One match.
        if len(candidates) == 1:
            subprocess.Popen(candidates[0])
            
        # Setup for multiple files with the same name.
        else:
            # Multiple matches found.
            print(f"\nMultiple matches found for {target}:")
            for idx, match in enumerate(candidates, start=1):
                item_type = "Folder" if match.is_dir() else f"File ({match.suffix})"
                print(f"  [{idx}] {match.name} --> {item_type}")
            
            choice = input(f"Which one do you want to open? (1-{len(candidates)}): ")
            try:
                selected_index = int(choice) - 1
                subprocess.Popen(candidates[selected_index])
            except (ValueError, IndexError):
                print("Invalid selecetion.")
                return None
    return None
###################################
###################################
#Registry / Maps
intent_map = { # Key-Word : Intent
    # Application Commands
    "find":"FIND_PATH",
    
    "open":"OPEN_PATH",
    
    "start":"OPEN_APPLICATION",
    "launch":"OPEN_APPLICATION",
    
    "close":"CLOSE_APPLICATION",
    "kill":"CLOSE_APPLICATION",
    "terminate":"CLOSE_APPLICATION",
    "exit":"CLOSE_APPLICATION",
    "quit":"CLOSE_APPLICATION",
    
    # Jarvis Commands
    f"{hotkey_quit}":"QUIT_JARVIS"
            }

command_map = { # Intent : Command
    "FIND_PATH":find_path,
    "OPEN_PATH":open_target,
    "OPEN_APPLICATION":open_application,
    "CLOSE_APPLICATION":close_application,
    "QUIT_JARVIS":toggle_active,
            }
###################################
###################################
# main()
def main():
    print(f"\nHello!")
    while active:
        ask_for_command()
    print(f"\nGoodbye!\n")
    
    #end of main()
if __name__ == "__main__":
    main()
