import  sys

from .notebook import Notebook

class Menu:
    """Display a menu and respond to choices when run."""
    def __init__(self):
        self.notebook =Notebook()
        self.choices = {
            "1":self.show_notes,


        }

