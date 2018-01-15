from setuptools import setup, find_packages

setup(
    name="nsource",
    version="0.0dev",
    description="nsource for planex test building",
    author="Kun Ma",
    author_email=', '.join([
        "kun.ma@citrix.com"]),
    url="http://unspecified.yet",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'nsource = nsource.cmd.test:main'
        ]
    },
)
