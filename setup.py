from setuptools import setup, find_packages


setup(
    name="em_product",
    version="0.2.15",
    install_requires=[
        "pydantic",
    ],
    url="https://github.com/VG-IT/em-product",
    author="Sky Zhao",
    author_email="newkbsky@gmail.com",
    packages=find_packages(exclude=["*tests"]),
    setup_requires=["wheel"],
)
