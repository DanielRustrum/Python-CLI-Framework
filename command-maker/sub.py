subcommands = {}
helpers = {}

class SubcommandAlreadyDefined(Exception):
    '''Exception: Multiple Subcommand have been Defined.'''

class SubcommandNotDefined(Exception):
    '''Exception: Subcommand needed to be defined before being called.'''

class InvalidSubcommandParameter(Exception):
    '''Exception: Thrown if provided a parameter that doesn't exist in the 
    helper map.'''


def getCallbackParameters(callback):
    '''Gets the parameters of a provided callback as well as their position.'''
    import inspect
    return inspect.getfullargspec(callback)[0]

def handleCallback(callback):
    '''Handles the Callback Call and Provides the callback with 
    its specified helpers.'''
    params = getCallbackParameters(callback)
    callback_args = []
    for param in params:
        formated_param = param.replace("_", "").lower()

        if formated_param not in helpers:
            raise InvalidSubcommandParameter(f"""Parameter {param} doesn't in 
            the subcommand parameter map.""")
        
        callback_args.append(helpers[formated_param])


def subcommand(subcommand_name: str):
    '''Declorator for declaring that the function is a CLI Subcommand.'''
    if subcommand_name in subcommands:
        raise SubcommandAlreadyDefined(
            f"""Can't define Subcommand 
            {subcommand_name} multiple times."""
        )

    def decorator(func):
        subcommands[subcommand_name] = {}
        subcommands[subcommand_name]["overloads"] = {}
        subcommands[subcommand_name]["root"] = func
    return decorator

# TODO: Full Implementation of Overloads Require Edge Cases Support
def overload(subcommand_name, flag_name):
    '''Declorator for declaring that this function should run in place of root
    callback if the flag is defined in command.'''
    if subcommand_name not in subcommands:
        raise SubcommandNotDefined(
            f"""Subcommand {subcommand_name} can not be 
            overloaded due to subcommand not being defined before function 
            overload has been defined."""
        )

    def decorator(func):
        subcommands[subcommand_name]["overloads"][flag_name] = func
    return decorator

def addHelper(helper_name, helper):
    '''Adds a helper to the helper map which is pulled by the subcommand 
    function if specified.'''
    helpers[helper_name] = helper

def executeSubcommand(command):
    if command["name"] not in subcommands:
        handleCallback(actions['help']['root'])
        raise SubcommandNotDefined(
            f"""Subcommand {command["name"]} has not been defined when 
            executing the subcommand."""
        )
    
    subcommand = subcommands[command["name"]]

    addHelper("args", command["args"])
    addHelper("arguments", command["args"])
    
    # TODO: Implement Overload Check

    handleCallback(subcommand["root"])
