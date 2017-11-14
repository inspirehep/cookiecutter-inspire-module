..
    This file is part of {{ cookiecutter.superproject }}.
    Copyright (C) {{ cookiecutter.years }} {{ cookiecutter.copyright_holder }}.

    {{ cookiecutter.superproject }} is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    {{ cookiecutter.superproject }} is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with {{ cookiecutter.superproject }}. If not, see <http://www.gnu.org/licenses/>.
{%- if cookiecutter.copyright_by_intergovernmental | lower not in ['0', 'f', 'false', 'n', 'no'] %}

    In applying this license, {{ cookiecutter.copyright_holder }} does not waive the privileges and immunities
    granted to it by virtue of its status as an Intergovernmental Organization
    or submit itself to any jurisdiction.
{%- endif %}


{{ '=' * (cookiecutter.project_name|length + 2) }}
 {{ cookiecutter.project_name }}
{{ '=' * (cookiecutter.project_name|length + 2) }}

.. image:: https://travis-ci.org/{{ cookiecutter.github_repo }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_repo }}

.. image:: https://coveralls.io/repos/github/{{ cookiecutter.github_repo }}/badge.svg?branch=master
    :target: https://coveralls.io/github/{{ cookiecutter.github_repo }}?branch=master


About
=====

{{ cookiecutter.description }}
