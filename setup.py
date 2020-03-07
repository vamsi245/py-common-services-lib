from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()



setup(
    name='common-services',
    version="1.0.2",
    description='common services for structured logging',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Nike',
    url="https://github.nike.com/gflsdrepo/deliver-edi-xml-splitter",

    packages=['common_services'],

    setup_requires=['pytest-runner', 'boto3'],
    tests_require=['pytest'],
    test_suite='test'

)