# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'nbsphinx',
    'recommonmark',
    'myst_nb',
]

source_suffix = {
    '.rst': 'restructuredtext',
    #'.md': 'markdown',
    '.ipynb': 'myst-nb',
}

myst_enable_extensions = [
    "dollarmath",  # 解析美元 $ 和 $$ 封装的数学和 LaTeX 数学公式
    "amsmath",     # 支持 amsmath 宏包的数学环境
    "deflist",     # 定义列表
    "colon_fence", # 使用冒号的代码围栏
    "html_admonition", # HTML 警告
    "html_image",  # HTML 图像
    "smartquotes", # 智能引号
    "replacements", # 替换
    "linkify",     # 自动识别 bare 网址并添加超链接
    "substitution", # 替换
    "tasklist",    # 任务列表
]


html_context = {
    'css_files': [
        '_static/custom.css',  # 自定义 CSS 文件路径
    ],
}

html_static_path = ['_static']

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
