from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude=["tests"]),
    license="MIT",
    description="EDSA example python package",
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url="https://github.com/Zandile254/<package-name>",
    author="Lucy Anita",
    author_email="lucywamboi80@gmail.com"
)