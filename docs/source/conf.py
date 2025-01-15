# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Npspy'
copyright = '2023, BGI Research'
author = 'Hailin Pan'

release = '1.0.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'nbsphinx',
    'sphinx_copybutton',
]

nbsphinx_execute = 'never'

nbsphinx_input_prompt = 'In2 [%s]:'
nbsphinx_output_prompt = 'Out2 [%s]:'

html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
