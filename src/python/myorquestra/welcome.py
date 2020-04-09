"""
This module saves a welcome message.
"""

import json

def welcome():
    message = "Welcome to Orquestra!"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    with open("welcome.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact

def create_diatomic_molecule_geometry(species1, species2, bond_length):
    """Create a molecular geometry for a diatomic molecule.
    
    Args:
        species1 (str): Chemical symbol of the first atom, e.g. 'H'.
        species2 (str): Chemical symbol of the second atom.
        bond_length (float): bond distance.
        
    Returns:
        dict: a dictionary containing the coordinates of the atoms.
    """

    geometry = {"sites": [
        {'species': species1, 'x': 0, 'y': 0, 'z': 0},
        {'species': species2, 'x': 0, 'y': 0, 'z': bond_length}
    ]}

    return geometry