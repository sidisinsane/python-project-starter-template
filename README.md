<div align="center">
<a title="Home" href="https://github.com/sidisinsane/python-project-starter-template">
    <img alt="Project Logo" src="docs/images/logo.svg" width="200">
</a>

# Python Project Starter Template

A Copier template for projects managed by Hatch.

[![License](https://img.shields.io/github/license/sidisinsane/python-project-starter-template)](https://github.com/sidisinsane/python-project-starter-template/blob/main/LICENSE)
[![CI Status](https://img.shields.io/github/actions/workflow/status/sidisinsane/python-project-starter-template/ci.yml?logo=github&label=ci)](https://github.com/sidisinsane/python-project-starter-template/blob/main/.github/workflows/ci.yml)
[![CodeQL Status](https://img.shields.io/github/actions/workflow/status/sidisinsane/python-project-starter-template/codeql.yml?logo=github&label=codeql)](https://github.com/sidisinsane/python-project-starter-template/blob/main/.github/workflows/codeql.yml)
[![GH-Pages Deploy Status](https://img.shields.io/github/actions/workflow/status/sidisinsane/python-project-starter-template/gh-pages-deploy.yml?logo=github&label=gh-pages-deploy)](https://github.com/sidisinsane/python-project-starter-template/blob/main/.github/workflows/gh-pages-deploy.yml)
[![Test Status](https://img.shields.io/github/actions/workflow/status/sidisinsane/python-project-starter-template/test.yml?logo=github&label=test)](https://github.com/sidisinsane/python-project-starter-template/blob/main/.github/workflows/test.yml)

[![Python Version](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/sidisinsane/python-project-starter-template/main/pyproject.toml&logo=python&logoColor=white&label=Python)](https://www.python.org/)
[![Copier](https://img.shields.io/badge/Copier-4b5563)](https://copier.readthedocs.io/en/stable/)
[![Hatch](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
[![Pytest](https://img.shields.io/badge/Pytest-0a9edc?logo=pytest&amp;logoColor=white&labelColor=4b5563)](https://pytest.org/)
[![Markdownlint](https://img.shields.io/badge/Markdownlint-000000?logo=markdown&amp;logoColor=white&labelColor=4b5563)](https://github.com/DavidAnson/markdownlint)
[![Commitlint](https://img.shields.io/badge/Commitlint-3451b2?logo=commitlint&amp;logoColor=white&labelColor=4b5563)](https://commitlint.js.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://docs.astral.sh/ruff/)
[![Bandit](https://img.shields.io/badge/Bandit-4b5563)](https://github.com/PyCQA/bandit)
[![Mypy](https://img.shields.io/badge/Mypy-4b5563)](https://mypy-lang.org/)
</div>

## Prerequisites

### Hatch

[Hatch](https://hatch.pypa.io/latest/) is a modern, [PEP 621](https://peps.python.org/pep-0621/)
compliant, extensible Python project manager.

#### Install Hatch

```shell
pipx install hatch
```

#### Configure Hatch

Store virtual environments in a directory named `.hatch` in each project directory.

```shell
hatch config set dirs.env.virtual .hatch
```

> [!NOTE]
> This adds the following to the configuration:
>
> ```toml
> [dirs.env]
> virtual = ".hatch"
> ```
>
> The [Configuration for Hatch](https://hatch.pypa.io/latest/config/hatch/) is stored in
a `config.toml` file at i.e. `~/Library/Application Support/hatch` on macOS.

## Usage

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

> [!NOTE]
> You can also clone the project template using `git clone https://github.com/sidisinsane/python-project-starter-template.git`,
modify it and generate a project the locally cloned repo.
>
> ```shell
> copier copy --trust PATH/TO/CLONED/PROJECT/TEMPLATE PATH/TO/DESTINATION
> ```

## Aftermath

### Create Virtual Environment

```shell
cd PATH/TO/DESTINATION && hatch env create
```

> [!NOTE]  
> You can locate environments by running `hatch env find`.

### Install Pre-Commit Hooks

```shell
git init && hatch run dev:pre-commit-install
```

> [!NOTE]  
> After you have created a new empty GitHub project, you are ready to make your
initial commit.
>
> ```shell
> git add .
> git commit -m "initial commit"
> git branch -M main
> git remote add origin <https://github.com/REPO_NAMESPACE/REPO_NAME.git>
> git push -u origin main
> ```

See the [documentation](https://sidisinsane.github.io/python-project-starter-template/)
for more details.
