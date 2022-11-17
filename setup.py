from setuptools import setup, find_packages

setup(
    name='mkdocs-extra-sass-plugin',
    install_requires=[
        'libsass==0.22.0',
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'extra-sass = mkdocs_extra_sass_plugin.plugin:RoamLinksPlugin',
        ]
    }
)