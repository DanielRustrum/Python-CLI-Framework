def handleDynamicCallback(callback, *args):
    '''Depending on the parameters of the callback it will pass 
    the correct data.'''
    import inspect
    callback_args = inspect.getfullargspec(callback)[0]
    arg_length = len(callback_args)

    if arg_length == 0:
        actions[command["action"]]["callback"]()
        return

    if arg_length == 1:
        actions[command["action"]]["callback"](actionLogger)
        return

    actions[command["action"]]["callback"](actionLogger, command["args"])
