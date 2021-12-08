from setuptools import setup, find_packages
import os
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="FedML",
    url="https://github.com/FedML-AI/FedML",
    packages=['fedml_api', 'fedml_core', 'fedml_experiments'],
    package_data={'fedml_api': ['*'],
                  'fedml_core': ['*'],
                  'fedml_experiments': ['*']},
    include_package_data=True,
    python_requires=">=3.6",

)
