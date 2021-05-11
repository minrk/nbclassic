from .notebookapp import NotebookApp
from ._version import version_info, __version__  # noqa

def _jupyter_server_extension_paths():
    return [
        {
            'module': 'nbclassic.notebookapp',
            'app': NotebookApp,
            'name': 'jupyter-nbclassic'
        },
        {
            'module': 'nbclassic.nbserver',
        }
    ]
