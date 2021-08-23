import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monga",
    version="0.0.4",
    author="Riza Masykur",
    author_email="hanirizo@gmail.com",
    description="A Pymongo Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rizoadev/monga",
    project_urls={
        "Bug Tracker": "https://github.com/rizoadev/monga/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)