import os

def get_environment_variable(var_name: str) -> str:
    """
    Fetch the value of an environment variable.

    Parameters:
    - var_name (str): The name of the environment variable.

    Returns:
    - str: The value of the environment variable or None if not found.
    """
    return os.environ.get(var_name)

def load_env_from_file(filename: str):
    """
    Load environment variables from a file.

    Parameters:
    - filename (str): The path to the file containing the environment variables.
    """
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

def setup_env(filename: str):
    
    ENV_VAR_NAME = "ENV_YELP_FUSION_APIKEY" 
    local_variable = get_environment_variable(ENV_VAR_NAME)

    
    if local_variable:
        print(f"The value of {ENV_VAR_NAME} exists")
    else:
        # Load environment variables from a file
        local_variable = load_env_from_file(filename)
        print(f"{ENV_VAR_NAME} from env exists.")

# Example usage:
if __name__ == "__main__":
    setup_env(".env")
