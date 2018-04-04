# -*- coding: utf-8 -*-
#
# This file is part of {{ cookiecutter.superproject }}.
# Copyright (C) {{ cookiecutter.years }} {{ cookiecutter.copyright_holder }}.
#
# {{ cookiecutter.superproject }} is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# {{ cookiecutter.superproject }} is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with {{ cookiecutter.superproject }}. If not, see <http://www.gnu.org/licenses/>.
{%- if cookiecutter.copyright_by_intergovernmental | lower not in ['0', 'f', 'false', 'n', 'no'] %}
#
# In applying this license, {{ cookiecutter.copyright_holder }} does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.
{%- endif %}

"""{{ cookiecutter.description }}"""

from __future__ import absolute_import, division, print_function

from setuptools import find_packages, setup


url = 'https://github.com/{{ cookiecutter.github_repo }}'

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
]

extras_require = {
    'docs': docs_require,
    'tests': tests_require,
    'tests:python_version=="2.7"': [
        'unicode-string-literal~=1.0,>=1.1',
    ],
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    extras_require['all'].extend(reqs)

packages = find_packages(exclude=['docs'])

setup(
    name='{{ cookiecutter.project_shortname }}',
    autosemver={
        'bugtracker_url': url + '/issues',
    },
    url=url,
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
