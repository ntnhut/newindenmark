# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'New In Denmark'
copyright = '2025, Nhut Nguyen'
author = 'Nhut Nguyen'
release = '2025.08.25'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_theme_options = {
    # 'logo_only': True,
    "sidebar_hide_name": True,
    # 'nosidebar': True,
    "announcement": "Support my work by <a href='https://buymeacoffee.com/nhutnguyen'  target='_blank'>buying me a coffee</a>!", 
}