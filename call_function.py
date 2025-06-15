from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_contnet_info, get_file_content
from functions.run_python import schema_run_python_file_info, run_python_file
from functions.write_file_content import schema_wrte_file_info, write_file

# Create a list of all available function schema to pass to the LLM
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_contnet_info,
        schema_run_python_file_info,
        schema_wrte_file_info,
    ]
)

available_functions_run = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
}


def call_function(function_call_part, verbose=False):
    print(f"{function_call_part.args}")
    arguments = function_call_part.args
    arguments["working_directory"] = "./calculator"
    print(f"{arguments}")
    function_name = function_call_part.name

    if verbose:
        print(f"Calling function: {function_name}({arguments})")
    else:
        print(f" - Calling function: {function_name}")

    try:
        if function_name not in available_functions_run.keys():
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"},
                    )
                ],
            )

        function_result = available_functions_run[function_name](**arguments)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )
    except Exception as e:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Error: {e}"},
                )
            ],
        )
