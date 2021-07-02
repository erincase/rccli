from setuptools import setup, find_packages

setup(
    name='rccli',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['click', 'requests'],
    entry_points={
        'console_scripts': [
            'rccli = src.cli.rccli:main'
        ]
    }
)
