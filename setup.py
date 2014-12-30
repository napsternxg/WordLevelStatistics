from setuptools import setup
def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='WordLevelStatistics',
    version='0.1',
    description='Implementation of WordLevelStatistics module from perl',
    long_description=readme(),
    url='http://github.com/napsternxg/WordLevelStatistics',
    author='Shubhanshu Mishra',
    author_email='smishra8@illinois.edu',
    clasifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Topic :: Text Processing :: General"
    ]
    license='GPL v2.0',
    packages=['WordLevelStatistics'],
    include_package_data=True,
    zip_safe=False)
