import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PiNode3'
copyright = '2024, Mineno Laboratory'
author = 'Shimada Takuto, Kurita Kazuaki, Ebisawa Hajime'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "myst_parser"
]

templates_path = ['_templates']
exclude_patterns = []

language = 'jp'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'
html_static_path = ['_static']

autodoc_default_options = {'private-members': True,   # プライベートメソッドも出力
                           'show-inheritance': True}  # 継承を表示

napoleon_custom_sections = [('Returns', 'params_style')]