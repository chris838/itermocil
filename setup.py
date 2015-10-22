from setuptools import setup, find_packages

setup(
    name='itermocil',
    version='0.1.8',
    url='https://github.com/chris838/itermocil',
    license='MIT',
    description='Create pre-defined window/pane layouts and run commands in iTerm',
    author='Tom Anthony',
    author_email='',
    packages=find_packages(),
    py_modules=['itermocil'],
    package_data={},
    classifiers=[],
    entry_points={
        'console_scripts': [
            'itermocil = itermocil:main',
        ]
    },
    install_requires=[
        'PyYAML',
    ]
)
