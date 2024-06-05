def setupLogging():
    '''provides a logging object to use'''
    import logging, sys
    handlers = []
    if command['has-logging']:
        handlers.append(logging.FileHandler(filename=command['logging']))
    
    if command['is-noisy']:
        handlers.append(logging.StreamHandler(stream=sys.stdout))


    logging.basicConfig(
        level=logging.DEBUG,
        format=f'[%(asctime)s] ({command["action"]}) %(levelname)s - %(message)s',
        handlers=handlers
    )

def actionLogger(level = "Debug", message = ""):
    '''Log a Message to the Console with a criticality level of 1-5'''
    import logging
    
    Levels = {
        "debug": [logging.DEBUG, 1],
        "info": [logging.INFO, 2],
        "warning": [logging.WARNING, 3],
        "error": [logging.ERROR, 4],
        "critical": [logging.CRITICAL, 5]
    }

    if level.lower() not in Levels:
        raise Exception(f"Level {level} is not a valid logging level.")

    level_status, level_amount = Levels[level.lower()]

    if level_amount < command['noise-level']:
        return

    Logger = logging.getLogger(command['action'])
    
    if command['has-logging'] or command['is-noisy']:            
        Logger.log(level_status, message)
