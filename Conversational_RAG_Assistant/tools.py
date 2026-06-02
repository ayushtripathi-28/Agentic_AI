# This file is generated to create tools which will later help in the conversational RAG assistant and Tool calling process.

from datetime import datetime
import math

def get_current_time():

    # Returns the current date and time.

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Returns the time in the same format.

    return {"tool_name" : "get_current_time",
            "result" : current_time}

def calculate(expression):

    #Evaluates basic mathematical expressions.

    try:
        allowed_names = {
            "sqrt" : math.sqrt,
            "pow" : pow,
            "abs" : abs,
            "round" : round
       }
        
        result = eval(expression, {"__builtin__" : {}}, allowed_names)

        return {"tool_name" : "calculate",
                "result" : result}
    
    except Exception as e:
        return {"tool_name" : "calculate",
                "error" : str(e)}
    
# Defining the JSON schema of this file.

TIME_TOOL_SCHEMA = {
    "name" : "get_current_time",
    "description" : "Returns the current date and time.",
    "parameters" : {
        "type" : "object",
        "properties" : {}
    }
}

CALCULATOR_TOOL_SCHEMA = {
    "name" : "calculate",
    "description" : "Evaluate a mathematical expression",
    "parameters" : {
        "type" : "object",
        "properties" : {
            "expression" : {
                "type" : "string",
                "description" : "Mathematical expression to evaluate."
            }
        },
        "required" : ["expression"]
    }
}