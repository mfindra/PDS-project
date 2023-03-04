from setuptools import setup, find_packages

setup(
    name='PDS-project',
    version='0.1.0',
    description='Bittorrent analyzator',
    author='Michal Findra (findr00)',
    author_email='xfindr00@vutbr.cz',
    packages=find_packages(),
    install_requires=[
        # List of dependencies required by your project
    ],
    entry_points={
        'console_scripts': [
            'project_name=main:main'
        ]
    }
)