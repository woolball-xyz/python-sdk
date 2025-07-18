# coding: utf-8

"""
    Woolball AI Network API

    **Transform idle browsers into a powerful distributed AI inference network**  For detailed examples and model lists, visit our [GitHub repository](https://github.com/woolball-xyz/woolball-server).  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "woolball-sdk"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Python client for Woolball AI Network API",
    author_email="",
    url="",
    keywords=["Woolball", "AI", "SDK", "Python"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    **Transform idle browsers into a powerful distributed AI inference network**  For detailed examples and model lists, visit our [GitHub repository](https://github.com/woolball-xyz/woolball-server).  # noqa: E501
    """
)
