description = """A Config Manager that allows you to change config on the fly
while still allowing you to Personalize."""

@action(
    "help", 
    ["Provides Specific Information about a Specified Sub Command"]
)
def help(log, args):
    '''Provides a list of subcommands along side what they do and how to use them.'''
    print("\n====== Catalyst Help ======")
    if len(args["unnamed"]) > 0:
        action_name = args["unnamed"][1]
        
        if action_name not in actions:
            print("Subcommand not Available.")
            return

        action = actions[action_name]

        desc =  action["callback"].__doc__ \
            if action["callback"].__doc__ is not None\
            else "Undocumented Subcommand."

        print(f'\n{action_name}:\n    {desc}')
        
        if len(action["expected"]["args"]) != 0:
            print("\n    Arguments:")
            for arg_position, arg_desc in enumerate(action["expected"]["args"]):
                print(f"      - {arg_position + 1}: {arg_desc}")


        if len(action["expected"]["flags"]) != 0:
            print("\n    Flags:")
            for flag_name, flag_desc in action["expected"]["flags"].items():
                print(f"      - {flag_name}: {flag_desc}")
    else:
        print(description, "\n")
        for action_name, action in actions.items():
            desc =  action["callback"].__doc__ \
                if action["callback"].__doc__ is not None\
                else "Undocumented Subcommand."\

            print(f'{action_name}: {desc}')

    print("\n")
