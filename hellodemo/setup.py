from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: MacOS :: MacOS X"
]

with open("README.md", "r") as readme_file:
    README = readme_file.read()

setup(
    name='hellodemo',
    version='1.0.0',
    description='hello package',
    long_description=README,
    url='',
    author='Jesse DeSimone',
    author_email='desimone.neuro@gmail.com',
    classifers=classifiers,
    keywords='hello',
    packages=find_packages(),
    install_requires=[]
)
