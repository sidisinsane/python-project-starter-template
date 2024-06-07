<div align="center">
<a title="Home" href="https://github.com/sidisinsane/python-project-starter-template">
    <img alt="Project Logo" src="images/logo.svg" width="200">
</a>

<h1>Python Project Starter Template</h1>

<p><i>A Copier template for Python projects managed by Hatch.</i></p>

<p>
<a title="License" href="https://github.com/sidisinsane/python-project-starter-template/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/sidisinsane/python-project-starter-template">
</a>
<a title="CI Status" href="https://github.com/sidisinsane/python-project-starter-template/blob/main/.github/workflows/ci.yml">
    <img alt="CI Status" src="https://img.shields.io/github/actions/workflow/status/sidisinsane/python-project-starter-template/ci.yml?logo=github&label=ci">
</a>
<a title="CodeQL Status" href="https://github.com/sidisinsane/python-project-starter-template/blob/main/.github/workflows/codeql.yml">
    <img alt="CodeQL Status" src="https://img.shields.io/github/actions/workflow/status/sidisinsane/python-project-starter-template/codeql.yml?logo=github&label=codeql">
</a>
<a title="GH-Pages Deploy Status" href="https://github.com/sidisinsane/python-project-starter-template/blob/main/.github/workflows/gh-pages-deploy.yml">
    <img alt="GH-Pages Deploy Status" src="https://img.shields.io/github/actions/workflow/status/sidisinsane/python-project-starter-template/gh-pages-deploy.yml?logo=github&label=gh-pages-deploy">
</a>
<a title="Test Status" href="https://github.com/sidisinsane/python-project-starter-template/blob/main/.github/workflows/test.yml">
    <img alt="Test Status" src="https://img.shields.io/github/actions/workflow/status/sidisinsane/python-project-starter-template/test.yml?logo=github&label=test">
</a>
</p>

<p>
<a title="Python Version" href="https://www.python.org/">
    <img alt="Python Version" src="https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/sidisinsane/python-project-starter-template/main/pyproject.toml&logo=python&logoColor=white&label=Python">
</a>
<a title="Copier" href="https://copier.readthedocs.io/en/stable/">
    <img alt="Copier" src="https://img.shields.io/badge/Copier-4b5563">
</a>
<a title="Hatch" href="https://github.com/pypa/hatch">
    <img alt="Hatch" src="https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg">
</a>
<a title="Material for MkDocs" href="https://squidfunk.github.io/mkdocs-material/">
    <img alt="Material for MkDocs" src="https://img.shields.io/badge/Material_for_MkDocs-526CFE?logo=MaterialForMkDocs&logoColor=white">
</a>
<a title="Pytest" href="https://pytest.org/">
    <img alt="Pytest" src="https://img.shields.io/badge/Pytest-0a9edc?logo=pytest&amp;logoColor=white&labelColor=4b5563">
</a>
<a title="Markdownlint" href="https://github.com/DavidAnson/markdownlint">
    <img alt="Markdownlint" src="https://img.shields.io/badge/Markdownlint-000000?logo=markdown&amp;logoColor=white&labelColor=4b5563">
</a>
<a title="Commitlint" href="https://commitlint.js.org/">
    <img alt="Commitlint" src="https://img.shields.io/badge/Commitlint-3451b2?logo=commitlint&amp;logoColor=white&labelColor=4b5563">
</a>
<a title="Ruff" href="https://docs.astral.sh/ruff/">
    <img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json">
</a>
<a title="Bandit" href="https://github.com/PyCQA/bandit">
    <img alt="Bandit" src="https://img.shields.io/badge/Bandit-4b5563">
</a>
<a title="Mypy" href="https://mypy-lang.org/">
    <img alt="Mypy" src="https://img.shields.io/badge/Mypy-4b5563">
</a>
</p>
</div>

## Quickstart

### Generate a Project

```shell
copier copy --trust https://github.com/sidisinsane/python-project-starter-template.git PATH/TO/DESTINATION
```

or

```shell
copier copy --trust gh:sidisinsane/python-project-starter-template PATH/TO/DESTINATION
```

This will generate a new project with the following structure:

```ascii
YOUR-PROJECT-NAME/
├── bandit.yaml
├── commitlint.config.js
├── docs/
│   ├── images/
│   │   ├── favicon.svg
│   │   └── logo.svg
│   ├── index.md
│   ├── javascripts/
│   │   └── mathjax.js
│   └── license.md
├── LICENSE
├── mkdocs.yaml
├── mypy.ini
├── pyproject.toml
├── pytest.ini
├── README.md
├── ruff.toml
├── schemas/
│   ├── github-workflow.json
│   ├── markdownlint-config-schema.json
│   ├── pre-commit-config.json
│   └── yamllint.json
├── src/
│   └── YOUR_PROJECT_NAME/
│       ├── __about__.py
│       ├── __init__.py
│       ├── calc.py
│       ├── cli/
│       │   └── __init__.py
│       ├── example.py
│       └── logger.py
├── taplo.toml
└── tests/
    ├── __init__.py
    ├── test_calc.py
    └── test_example.py
```

??? note
    You can also clone the project template using
    `git clone https://github.com/sidisinsane/python-project-starter-template.git`,
    modify it and generate a project the locally cloned repo.

    ```shell
    copier copy --trust PATH/TO/CLONED/PROJECT/TEMPLATE PATH/TO/DESTINATION
    ```

## Aftermath

### Create Virtual Environment

```shell
cd PATH/TO/DESTINATION && hatch env create
```

??? note
    You can locate environments by running `hatch env find`.

### Install Pre-Commit Hooks

```shell
git init && hatch run pre-commit install
```

??? note
    After you have created a new empty GitHub project, you are ready to make your
    initial commit.
    ```shell
    git add .
    git commit -m "initial commit"
    git branch -M main
    git remote add origin https://github.com/REPO_NAMESPACE/REPO_NAME.git
    git push -u origin main
    ```
