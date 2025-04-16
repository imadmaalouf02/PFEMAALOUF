# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Intelligent AI Platform for Automobile Component Management'
copyright = '2025, GIIADS, by Maalouf IMAD '
author = 'imad maalouf'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']  

# Choix du moteur LaTeX (par exemple 'xelatex' pour une meilleure gestion des encodages)
latex_engine = 'xelatex'

# Personnalisation des éléments LaTeX (préambule, commandes, etc.)
latex_elements = {
    'preamble': r'''
        \usepackage[utf8]{inputenc}
        \usepackage[T1]{fontenc}
        \usepackage{lmodern}
    ''',
}
