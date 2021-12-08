from setuptools import setup, find_packages
import os


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


fedml_api_files = package_files('fedml_api')
fedml_core_files = package_files('fedml_core')
fedml_experiments_files = package_files('fedml_experiments')

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="FedML",
    url="https://github.com/FedML-AI/FedML",
    packages=['fedml_api', 'fedml_core', 'fedml_experiments'],
    package_data={'fedml_api': fedml_api_files,
                  'fedml_core': fedml_core_files,
                  'fedml_experiments': fedml_experiments_files},
    include_package_data=True,
    python_requires=">=3.6",

)
