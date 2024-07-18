# -- Project information -----------------------------------------------------

repository = 'documentation'
project = 'System Level Documentation'
copyright = '2024, Analog Devices, Inc.'
author = 'Analog Devices, Inc.'

# -- General configuration ---------------------------------------------------

extensions = [
    "adi_doctools"
]

needs_extensions = {
    'adi_doctools': '0.3.17'
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'

# -- External docs configuration ----------------------------------------------

interref_repos = ['doctools']

# -- Custom extensions configuration ------------------------------------------

# -- Options for HTML output --------------------------------------------------

html_theme = 'cosmic'
numfig = True


numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}