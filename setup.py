#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-sling",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_sling"],
    install_requires=[
        "singer-python==5.9.0",
        "requests==2.24.0",
    ],
    entry_points="""
    [console_scripts]
    tap-sling=tap_sling:main
    """,
    packages=["tap_sling"],
    package_data = {
        "schemas": ["tap_sling/schemas/*.json"]
    },
    include_package_data=True,
)
