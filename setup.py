from setuptools import find_packages, setup

from booleanoperator.Release import __author__, __author_email__, \
    __description__, __license__, __name__, __url__, __version__


setup(
    name=__name__,
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    license=__license__,
    description=__description__,
    long_description=open("README.rst").read(),
    url=__url__,
    packages=find_packages(),
    package_data={
        "booleanoperator": [],
    },
    data_files=[],
    entry_points={
        "console_scripts": [
            "BooleanOperator = booleanoperator.run_server:run_boolean_operator"
        ]
    },
    project_urls={
        "Bug Reports":
            "https://github.com/synchrotron-solaris/dev-booleanoperator/issues",
        "Documentation":
            "https://example.com/",
        "Source":
            "https://github.com/synchrotron-solaris/dev-booleanoperator.git",
    }
)
