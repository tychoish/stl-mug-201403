import sys
import os
import datetime

project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
from bootstrap import buildsystem, master_conf
sys.path.append(os.path.join(project_root, buildsystem))
sys.path.append(os.path.join(project_root, "sphinxext"))
from utils.config import get_conf

conf = get_conf(os.path.dirname(master_conf))

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

needs_sphinx = '1.0'

extensions = ["intermanual", "sphinx.ext.extlinks", "hieroglyph", "mongodb"]
templates_path = ['']
source_suffix = '.txt'
master_doc = 'index'

project = u'MongoDB Tuning Overview'
copyright = u'{0}, MongoDB Inc.'.format(datetime.datetime.today().year)

version = '1.0'
release = version

exclude_patterns = []
npygments_style = 'sphinx'

extlinks = {}

git_name = 'stl-mug-201403'

html_theme_options = {
    'project': git_name,
}

html_sidebars = {
    '**': []
}

intersphinx_mapping = {'mongodb': ( 'http://docs.mongodb.org/manual', os.path.join(conf.paths.projectroot,
                                                                                   conf.paths.output,
                                                                                   "mongodb.inv")) }

# -- Options for HTML output ---------------------------------------------------
html_theme_path = [os.path.join(conf.paths.projectroot, conf.paths.buildsystem, 'themes')]
html_theme = 'tychoish'

html_title = "The Documentation Project at 10gen"
html_use_smartypants = True
