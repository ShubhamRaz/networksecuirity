from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function returns a list of requirements from the 'requirements.txt' file.
    """
    req_list: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
        # Remove any leading/trailing whitespace characters and filter out empty lines
        for line in lines:
            requirement = line.strip()

            if requirement and requirement !="-e.":
                req_list.append(requirement)

    except FileNotFoundError:
        print("The 'requirements.txt' file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the 'requirements.txt' file: {e}")
    return req_list
setup(
    name="NetworkSEcuirity",
    version="0.0.1",
    author="Shubham",
    author_email="pankajkr6810@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)