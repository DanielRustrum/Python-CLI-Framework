command = {
    'name': "",
    'args': {
        'flags': {},
        'unnamed': {}
    },
    'logging': None,
    'has-logging': False,
    'is-noisy': False,
    'noise-level': 1
}


def formatCommand():
    '''Formats the Command into a Consumable Singleton Format'''
    from sys import argv as args
    args_len = len(args)
    
    if args_len <= 1:
        command['name'] = "help"
        return

    command['name'] = args[1]

    if args_len <= 2:
        return

    def getArgKeyValue(arg):
        arg.replace("%20", " ")

        if arg.startswith("--"):
            result = arg[2:].split("=", 1)
        elif arg.startswith("-"):
            result = arg[1:].split("=", 1)
        else: 
            result = arg.split("=", 1)

        if len(result) == 1:
            return [result[0], None]
        return result

    unnamed_index = 0

    for arg in args[2:]:
        arg_key, arg_value = getArgKeyValue(arg)
        
        if not (arg.startswith("--") or arg.startswith("-")):
            unnamed_index += 1
            command["args"]['unnamed'][unnamed_index] = arg_key
            continue

        
        if arg.startswith("--log"):
            if arg_value is None:
                command["logging"] = "catalyst.log"
            else:
                command["logging"] = arg_value
            command["has-logging"] = True
            continue

        if arg.startswith("--noisy"):
            command["is-noisy"] = True
            continue

        if arg.startswith("--noise-level"):
            if arg_value is None:
                command["noise-level"] = 1
            else:
                command["noise-level"] = int(arg_value)
            command["has-logging"] = True
            continue
        
        command['args']['flags'][arg_key] = arg_value
