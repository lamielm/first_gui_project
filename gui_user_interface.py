"""Simple Beverage Management GUI"""

# Third-party imports
import FreeSimpleGUI as sg

# First-party imports
from errors import AlreadyImportedError


class BeverageListWindow:
    """Simple Beverage List"""

    def __init__(self, beverage_collection, csv_processor, path_to_csv):
        """Constructor"""
        self.beverage_collection = beverage_collection
        self.csv_processor = csv_processor
        self.path_to_csv = path_to_csv

        layout = [
            [sg.Text("Beverage List")],
        ]

        self.window = sg.Window("Beverage List", layout)
