# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='test_erp',
    version=version,
    description='Mange All doctype,report',
    author='Frappe',
    author_email='sagar.s@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
