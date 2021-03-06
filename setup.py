from setuptools import setup

setup(
    name='sphinxcontrib-visio',
    version='1.0.1',
    author='Yassu',
    author_email='yassumath@gmail.com',
    url='https://github.com/yassu/sphinxcontrib-visio',
    description='Python reStructuredText directive for embedding visio image',
    license='apachae2',
    packages=['sphinxcontrib'],
    install_requires=[
        'visio2img'
    ],
    namespace_packages=['sphinxcontrib'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
