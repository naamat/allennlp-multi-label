import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="allennlp_multi_label",
    version="0.1.0",
    author="John Giorgi",
    author_email="johnmgiorgi@gmail.com",
    description=("A multi-label classification plugin for AllenNLP"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/semantic-health/allennlp-multi-label",
    packages=setuptools.find_packages(),
    keywords=[
        "natural language processing",
        "pytorch",
        "allennlp",
        "transformers",
        "document classification",
        "multi-label",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Typing :: Typed",
    ],
    python_requires=">=3.6.1",
    install_requires=["allennlp>=1.0.0"],
    extras_require={
        "dev": ["black", "flake8", "hypothesis", "pytest", "pytest-cov", "coverage", "codecov"]
    },
)
