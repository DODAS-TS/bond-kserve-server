from setuptools import setup, find_packages

setup(
    name='bondserver',
    version='0.0.1',
    author_email='diego.ciangottini@gmail.com',
    license='https://github.com/kserve/kserve/LICENSE',
    url='https://github.com/dodas-ts/bond-kserve-server/bondserver',
    description='Model Server implementation for bondmachine. \
                 Not intended for use outside KServe Frameworks Images',
    long_description=open('README.md').read(),
    python_requires='>3.7',
    packages=find_packages("bondserver"),
    install_requires=[
        "kserve",
    ],
)
