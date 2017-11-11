{% include 'misc/header.rst' %}

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
