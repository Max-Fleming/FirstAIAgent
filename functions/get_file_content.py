import os
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        max_chars = 10000
        with open(target_file, "r") as f:
            file_content_string = f.read(max_chars)
            if len(file_content_string) >= max_chars:
                file_content_string += (
                    f'...File "{file_path}" truncated at {max_chars} characters'
                )
        return file_content_string
    except Exception as e:
        return f"Error reading file: {e}"

schema_get_file_contnet_info = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the file in the specified directory and returns the text content of the file up to a maximum of 10,000 characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file you want to read, relative to the working directory. This value must be provided.",
            ),
        },
    ),
)
