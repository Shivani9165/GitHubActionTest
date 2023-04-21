import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
    name="Auto-Git-Action",
    version="1.0.0",
    description="GitHub Action to automate houston version upgrade",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.come/Shivani9165/GitHubActionTest",
    packages=find_packages(),
    author="Shivani",
    author_email="shivani9165@gmail.com",
    install_requires=[],
    entry_points={
         "console_scripts":[
             "testsparq=testsparq.__main__:main",
         ]
    },
)