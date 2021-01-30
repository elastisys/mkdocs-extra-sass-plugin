# mkdocs-extra-sass-plugin

[![PyPI version](https://img.shields.io/pypi/v/mkdocs-extra-sass-plugin.svg)](https://pypi.org/project/mkdocs-extra-sass-plugin)
[![PyPI downloads](https://img.shields.io/pypi/dm/mkdocs-extra-sass-plugin.svg)](https://pypi.org/project/mkdocs-extra-sass-plugin)

---

This plugin adds stylesheets to your mkdocs site from `Sass`/`SCSS`.

## Features

* using [LibSass][LibSass] with [libsass-python][libsass-python].

## How to use

### Installation

1. Install the package with pip:

    ```sh
    pip install mkdocs-extra-sass-plugin
    ```

2. Enable the plugin in your `mkdocs.yml`:

    ```yml
    plugins:
      - extra-sass
    ```

    > **Note**: If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

3. Create a `extra_sass` directory in your working directory _(usually the same directory as` mkdocs.yml`)_, and create **entry point file** named `style.css.sass` or `style.css.scss`.

    ```none
    (top)
    ├── docs
    ：  ...snip...
    │   └── index.md
    ├── extra_sass
    ：  ...snip...
    │   └── style.css.scss (or style.css.sass)  # compiler entry point file.
    └── mkdocs.yml
    ```

More information about plugins in the [MkDocs documentation][mkdocs-plugins].

## Contributing

From reporting a bug to submitting a pull request: every contribution is appreciated and welcome. Report bugs, ask questions and request features using [Github issues][github-issues].
If you want to contribute to the code of this project, please read the [Contribution Guidelines][contributing].

[LibSass]: https://sass-lang.com/libsass
[libsass-python]: https://github.com/sass/libsass-python
[mkdocs-plugins]: https://www.mkdocs.org/user-guide/plugins/
[github-issues]: https://github.com/orzih/mkdocs-extra-sass-plugin/issues
[contributing]: https://github.com/orzih/mkdocs-extra-sass-plugin/blob/master/CONTRIBUTING.md
