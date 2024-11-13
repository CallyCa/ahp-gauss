from setuptools import setup, find_packages

setup(
    name="ahp-gauss",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "pyyaml",
        "pytest"
    ],
    entry_points={
        "console_scripts": [
            "ahp-gauss=main:main",
        ],
    },
)
