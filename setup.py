from setuptools import setup, find_packages
from packaging import version
import re
import os

from imagesplit.utils.versioning import get_git_version


version_buf, version_git, command_git = get_git_version()

# Create a module that will keep the
# version descriptor returned by Git
info_module = open(os.path.join('imagesplit', 'info.py'), 'w')
info_module.write('# -*- coding: utf-8 -*-\n')
info_module.write('"""ImageSplit version tracker.\n')
info_module.write('\n')
info_module.write('This module only holds the ImageSplit version,')
info_module.write(' generated using the \n')
info_module.write('``{}`` command.\n'.format(' '.join(command_git)))
info_module.write('\n')
info_module.write('"""\n')
info_module.write('\n')
info_module.write('\n')
info_module.write('VERSION_DESCRIPTOR = "{}"\n'.format(version_buf))
info_module.close()

# Regex for checking PEP 440 conformity
# https://www.python.org/dev/peps/pep-0440/#id79
pep440_regex = re.compile(
    r"^\s*" + version.VERSION_PATTERN + r"\s*$",
    re.VERBOSE | re.IGNORECASE,
)

# Check PEP 440 conformity
if not version_git or pep440_regex.match(version_git) is None:
    raise ValueError('The version tag {} constructed from {} output'
                     ' (generated using the "{}" command) does not'
                     ' conform to PEP 440'.format(
                         version_git, version_buf, ' '.join(command_git)))

# Get the summary
description = 'Utility for splitting large image files into slices or chunks'\

# Get the long description
with open('README.rst.rst') as f:
    long_description = f.read()


setup(
    name='ImageSplit',

    version=version_git,

    description=description,
    long_description=long_description,

    url='https://github.com/gift-surg/ImageSplit',

    author='Tom Doel',
    author_email='t.doel@ucl.ac.uk',

    license='BSD license',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',

        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Scientific/Engineering :: Visualization',
    ],

    keywords='image file formats',

    packages=find_packages(
        exclude=[
            'pip',
            'docs',
            'tests',
        ]
    ),

    install_requires=[
        'six>=1.10',
        'numpy>=1.11',
        'pillow',
    ],

    entry_points={
        'console_scripts': [
            'imagesplit=imagesplit.applications.split_files:main',
        ],
    },
)
