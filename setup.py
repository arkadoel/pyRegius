import os

from setuptools import setup #tener instalado sudo apt-get install libboost-all-dev

with open('README.md') as readme_file:
    readme = readme_file.read()

this = os.path.dirname(os.path.realpath(__file__))

def read(name):
    with open(os.path.join(this, name)) as f:
        return f.read()
setup(
    name='pyregius',
    version='0.0.1',
    description='description',
    long_description=readme,
    author='',
    author_email='',
    url='https://github.com/arkadoel/pyRegius',
    packages = [],
    install_requires=read('requirements.txt'),
    include_package_data=True,
    zip_safe=True,
    license='GPLv3',
    keywords='example app snap linux ubuntu',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English'
    ],
    test_suite='tests',
    scripts=['src/main.py']
)
