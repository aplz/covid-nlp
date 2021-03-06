import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


dependencies = [
    'dacite',  # for loading nested data classes from json
    'scispacy',
    # scispacy models
    # 'en_core_sci_sm @ https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.4/en_core_sci_sm-0.2.4.tar.gz',
    # 'en_ner_craft_md @ https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.4/en_ner_craft_md-0.2.4.tar.gz',
    'en_ner_bc5cdr_md @ https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.4/en_ner_bc5cdr_md-0.2.4.tar.gz',
    'en_ner_jnlpba_md @ https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.4/en_ner_jnlpba_md-0.2.4.tar.gz',
    'pytextrank==2.0.1',
]
setuptools.setup(
    name="covid-nlp",
    version="0.0.1",
    author="Anja Pilz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aplz/covid-nlp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        #    "License :: OSI Approved :: MIT License",
    ],
    install_requires=dependencies,
    python_requires='>=3',
    package_dir={'': 'src'},
)
