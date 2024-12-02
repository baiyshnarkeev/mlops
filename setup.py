from setuptools import find_packages, setup
from typing import List

hupen_e_dot = "-e ."
def get_requirements(file_path:str) -> List[str]:
        """ 
        this function will return the list of requirements
        """

        requirements=[]
        with open(file_path) as file_obj:
                requirements = file_obj.readlines()
                requirements = [req.replace("\n", "") for req in requirements]

                if hupen_e_dot in requirements:
                        requirements.remove(hupen_e_dot)
                        
                return requirements
        
setup(
name = "mlproject",
version = "0.0.1",
author = "Baiysh",
author_email = "narkeev123@gmaill.com",
install_requires = get_requirements('requirements.txt')

)