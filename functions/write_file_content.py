import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        with open(target_file, "x") as f:
            pass
    try:
        with open(target_file, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        print(f"Error: writing to {file_path}: {e}")

schema_wrte_file_info = types.FunctionDeclaration(
    name="write_file",
    description="Checks if file given exists and creates it if it doesn't, then writes over that file with the new content given.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file you want to write to, relative to the working directory. This value must be provided amd must be given first.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that you wish to write to the given file. This value must be provided and must be given second."
            ),
        },
    ),
)
