import sys, os
project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
from bootstrap import buildsystem, master_conf
sys.path.append(os.path.join(project_root, buildsystem))
from utils.config import get_conf

conf = get_conf(os.path.dirname(master_conf))

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

needs_sphinx = '1.0'

extensions = ["sphinx.ext.intersphinx", "sphinx.ext.extlinks", "hieroglyph"]
templates_path = ['']
source_suffix = '.txt'
master_doc = 'index'

project = u'Better MongoDB Documentation'
copyright = u'2012, 10gen Inc.'

version = '1.0'
release = version

exclude_patterns = []
pygments_style = 'sphinx'

extlinks = {}

git_name = 'stl-mug-201403'

html_theme_options = {
    'project': git_name,
}

html_sidebars = {
    '**': ['localtoc.html', 'relations.html', 'sourcelink.html']
}

# -- Options for HTML output ---------------------------------------------------
html_theme_path = [os.path.join(conf.paths.projectroot, conf.paths.buildsystem, 'themes')]
html_theme = 'tychoish'

print(html_theme_path)

html_title = "The Documentation Project at 10gen"
html_use_smartypants = True
