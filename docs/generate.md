---
weight: 1
---
# Generate a Project

```shell
copier copy --trust https://github.com/sidisinsane/python-project-starter-template.git PATH/TO/DESTINATION
```

or

```shell
copier copy --trust gh:sidisinsane/python-project-starter-template PATH/TO/DESTINATION
```

??? note
    You can also clone the project template using
    `git clone https://github.com/sidisinsane/python-project-starter-template.git`,
    modify it and generate a project the locally cloned repo.

    ```shell
    copier copy --trust PATH/TO/CLONED/PROJECT/TEMPLATE PATH/TO/DESTINATION
    ```

## Prompts

[Copier](https://copier.readthedocs.io/en/stable/) will request your input for some
prompts. Prompts are configured in the `copier.yaml` file.

!!! note
    This template only supports GitHub as repository provider!

### `project_name`

```text
🎤 Your project name (main heading)
  [None]
```

??? note "Configuration"
    ```yaml
    project_name:
    type: str
    help: Your project name (main heading)
    ```

### `project_description`

```text
🎤 Your project description (main description)
  [None]
```

??? note "Configuration"
    ```yaml
    project_description:
    type: str
    help: Your project description (main description)
    ```

### `author_fullname`

```shell
🎤 Your full name (project.authors.name in pyproject.toml)
  ['Dirk Sidney Jansen' | git_user_name]
```

!!! note
    The `git_user_name` variable is handled by the custom
    [Jinja2](https://palletsprojects.com/p/jinja/) extension at `extensions/git.py`.

??? note "Configuration"
    ```yaml
    author_fullname:
    type: str
    help: Your full name (project.authors.name in pyproject.toml)
    default: "{{ 'Dirk Sidney Jansen' | git_user_name }}"
    ```

### `author_email`

```text
🎤 Your email (project.authors.email in pyproject.toml)
  ['sidisinsane@users.noreply.github.com' | git_user_email]
```

!!! note
    The `git_user_email` variable is handled by the custom
    [Jinja2](https://palletsprojects.com/p/jinja/) extension at `extensions/git.py`.

??? note "Configuration"
    ```yaml
    author_email:
    type: str
    help: Your email (project.authors.email in pyproject.toml)
    default: "{{ 'sidisinsane@users.noreply.github.com' | git_user_email }}"
    ```

### `author_username`

```text
🎤 Your GitHub username
  [sidisinsane]
```

??? note "Configuration"
    ```yaml
    author_username:
    type: str
    help: Your GitHub username
    default: sidisinsane
    ```

### `repository_provider`

```text
🎤 Your repository provider
» github.com
```

??? note "Configuration"
    ```yaml
    repository_provider:
    type: str
    help: Your repository provider
    default: github.com
    choices:
        - github.com
    ```

### `repository_namespace`

```text
🎤 Your repository namespace
  [author_username] 
```

??? note "Configuration"
    ```yaml
    repository_namespace:
    type: str
    help: Your repository namespace
    default: "{{ author_username }}"
    ```

### `repository_name`

```text
🎤 Your repository name
  [project_name | slugify]
```

!!! note
    The `slugify` method is handled by the custom
    [Jinja2](https://palletsprojects.com/p/jinja/) extension at `extensions/slugify.py`.

??? note "Configuration"
    ```yaml
    repository_name:
    type: str
    help: Your repository name
    default: "{{ project_name | slugify }}"
    ```

### `copyright_holder`

```text
🎤 The name of the person/entity holding the copyright
  [author_fullname]
```

??? note "Configuration"
    ```yaml
    copyright_holder:
    type: str
    help: The name of the person/entity holding the copyright
    default: "{{ author_fullname }}"
    ```

### `copyright_holder_email`

```text
🎤 The email of the person/entity holding the copyright
  [author_email]
```

??? note "Configuration"
    ```yaml
    copyright_holder_email:
    type: str
    help: The email of the person/entity holding the copyright
    default: "{{ author_email }}"
    ```

### `copyright_date`

```text
🎤 The copyright date
  [current_year]
```

!!! note
    The `current_year` variable is handled by the custom
    [Jinja2](https://palletsprojects.com/p/jinja/) extension at `date/git.py`.

??? note "Configuration"
    ```yaml
    copyright_date:
    type: str
    help: The copyright date
    default: "{{ current_year }}"
    ```

### `copyright_license`

```text
🎤 Your project's license
  (Use arrow keys)
  Apache-2.0
  BSD-2-Clause
  BSD-3-Clause
  CDDL-1.0
  EPL-2.0
  GPL-2.0
  GPL-3.0-only
  ISC
  LGPL-2.0-only
  LGPL-2.1
  LGPL-3.0-only
» MIT
  MPL-2.0 
```

??? note "Configuration"
    ```yaml
    copyright_license:
    type: str
    help: Your project's license
    default: MIT
    choices:
    - Apache-2.0
    - BSD-2-Clause
    - BSD-3-Clause
    - CDDL-1.0
    - EPL-2.0
    - GPL-2.0
    - GPL-3.0-only
    - ISC
    - LGPL-2.0-only
    - LGPL-2.1
    - LGPL-3.0-only
    - MIT
    - MPL-2.0
    ```

!!! note
    To add more licenses, add the [SPDX identifier](https://spdx.org/licenses/) to the
    `copier.yml` and the license text to the `project/LICENSE.jinja` file. License texts
    can be found at [choosealicense.com](https://choosealicense.com/).

### `python_package_distribution_name`

```text
🎤 Your Python package distribution name (for `pip install NAME`)
  [project_name | slugify]
```

??? note "Configuration"
    ```yaml
    python_package_distribution_name:
    type: str
    help: Your Python package distribution name
    default: "{{ project_name | slugify }}"
    ```

The name under which your Python package will be distributed.
This will be the name of your project on pypi.org for example.

### `python_package_import_name`

```text
🎤 Your Python package import name (for `import NAME` in Python code)
  [project_name | slugify('_')]
```

??? note "Configuration"
    ```yaml
    python_package_import_name:
    type: str
    help: Your Python package import name (for `import NAME` in Python code)
    default: "{{ project_name | slugify('_') }}"
    ```

The name that will be used to import your package in Python code.
Yes, distribution name and import name can be different!

### `python_package_command_line_name`

```text
🎤 Your CLI name if any (for use in the shell)
  [project_name | slugify] 
```

??? note "Configuration"
    ```yaml
    python_package_command_line_name:
    type: str
    help: Your CLI name if any (for use in the shell)
    default: "{{ project_name | slugify }}"
    ```

The generated project will have the following structure in the specified directory:

```ascii
YOUR-PROJECT-NAME/
├── .coveragerc
├── .env.template
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── codeql.yml
│       ├── gh-pages-deploy.yml
│       └── test.yml
├── .gitignore
├── .markdownlint.yaml
├── .pre-commit-config.yaml
├── .pylintrc
├── .vscode/
│   ├── argv.json
│   ├── extensions.json
│   └── settings.json
├── .yamllint.yaml
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
│   └── your_project_name/
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
