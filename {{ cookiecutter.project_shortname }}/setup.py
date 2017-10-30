{% include 'misc/header.py' %}
"""{{ cookiecutter.description }}"""

from __future__ import absolute_import, division, print_function

from setuptools import find_packages, setup


URL = 'https://github.com/{{ cookiecutter.github_repo }}'

readme = open('README.rst').read()

setup_requires = [
    'autosemver~=0.0,>=0.5.2',
]

install_requires = []

docs_require = []

tests_require = [
    'flake8-future-import~=0.0,>=0.4.3',
    'mock~=2.0,>=2.0.0',
    'pytest~=3.0,>=3.2.3',
    'pytest-cov~=2.0,>=2.5.1',
    'pytest-flake8~=0.0,>=0.9.1',
]

extras_require = {
    'docs': docs_require,
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    extras_require['all'].extend(reqs)

packages = find_packages(exclude=['docs'])

setup(
    name='{{ cookiecutter.project_shortname }}',
    autosemver={
        'bugtracker_url': URL + '/issues',
    },
    url=URL,
    license='GPLv3',
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    packages=packages,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    description=__doc__,
    long_description=readme,
    setup_requires=setup_requires,
    install_require=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
