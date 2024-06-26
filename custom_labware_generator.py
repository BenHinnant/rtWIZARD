import json
from io import BytesIO
from zipfile import ZipFile

def generate_labware_template(num_wells, slot_num, x_right_most, y_right_most, x_second=None, y_second=None):
    # Base structure for a labware file
    labware_template = {
        "brand": {
            "brand": "rtWIZARD",
            "brandId": ["La Jolla Institute for Immunology Histopathology Core"]
        },
        "metadata": {
            "displayCategory": "wellPlate",
            "displayVolumeUnits": "µL",
            "tags": []
        },
        "dimensions": {
            "xDimension": 127.89,
            "yDimension": 85.6,
            "zDimension": 27
        },
        "groups": [{
            "metadata": {
                "wellBottomShape": "flat"
            }
        }],
        "parameters": {
            "format": "irregular",
            "quirks": [],
            "isTiprack": False,
            "isMagneticModuleCompatible": False
        },
        "namespace": "custom_beta",
        "version": 1,
        "schemaVersion": 2,
        "cornerOffsetFromSlot": {
            "x": 0,
            "y": 0,
            "z": 0
        }
    }

    # global measurements
    # these should never change with our current deck printouts
    x_spacing = 88
    x_offset_147 = 40
    x_offset_258 = 80
    x_offset_369 = 32
    y_spacing = 28.67
    y_offset = 20.09
    # these can change depending on user input
    initial_x_147 = x_offset_147 - x_right_most
    initial_x_258 = x_offset_258 - x_right_most
    initial_x_369 = x_offset_369 - x_right_most
    initial_y = y_offset - y_right_most

    # order wells differently if template uses OT2 slots 1,4,7 or 3,6,9
    if slot_num == "147" or slot_num == "369":
        labware_template["ordering"] = [
            [
                "A1",
                "B1",
                "C1"
            ],
            [
                "A2",
                "B2",
                "C2"
            ]
        ]
        if slot_num == "147":
            initial_x_147_369 = initial_x_147
        else:
            initial_x_147_369 = initial_x_369
        # create wells_data dict that contains wells A1, B1, C1, A2, B2, C2
        wells_data = {
            "A1": {
                "depth": 3,
                "totalLiquidVolume": 500,
                "shape": "circular",
                "diameter": 4.1,
                "x": initial_x_147_369,
                "y": initial_y + (2 * y_spacing),
                "z": 24
            },
            "B1": {
                "depth": 3,
                "totalLiquidVolume": 500,
                "shape": "circular",
                "diameter": 4.1,
                "x": initial_x_147_369,
                "y": initial_y + y_spacing,
                "z": 24
            },
            "C1": {
                "depth": 3,
                "totalLiquidVolume": 500,
                "shape": "circular",
                "diameter": 4.1,
                "x": initial_x_147_369,
                "y": initial_y,
                "z": 24
            },
            "A2": {
                "depth": 3,
                "totalLiquidVolume": 500,
                "shape": "circular",
                "diameter": 4.1,
                "x": initial_x_147_369 + x_spacing,
                "y": initial_y + (2 * y_spacing),
                "z": 24
            },
            "B2": {
                "depth": 3,
                "totalLiquidVolume": 500,
                "shape": "circular",
                "diameter": 4.1,
                "x": initial_x_147_369 + x_spacing,
                "y": initial_y + y_spacing,
                "z": 24
            },
            "C2": {
                "depth": 3,
                "totalLiquidVolume": 500,
                "shape": "circular",
                "diameter": 4.1,
                "x": initial_x_147_369 + x_spacing,
                "y": initial_y,
                "z": 24
            }
        }
        labware_template["wells"] = wells_data
        labware_template["groups"][0]["wells"] = ["A1", "B1", "C1", "A2", "B2", "C2"]

        
    if slot_num == "258":
        labware_template["ordering"] = [
            [
                "A1",
                "B1",
                "C1"
            ]
        ]
        # create wells_data dict that contains wells A1, B1, C1
        wells_data = {
            "A1": {
                        "depth": 3,
                        "totalLiquidVolume": 500,
                        "shape": "circular",
                        "diameter": 4.1,
                        "x": initial_x_258,
                        "y": initial_y + (2 * y_spacing),
                        "z": 24
            },
            "B1": {
                        "depth": 3,
                        "totalLiquidVolume": 500,
                        "shape": "circular",
                        "diameter": 4.1,
                        "x": initial_x_258,
                        "y": initial_y + y_spacing,
                        "z": 24
            },
            "C1": {
                        "depth": 3,
                        "totalLiquidVolume": 500,
                        "shape": "circular",
                        "diameter": 4.1,
                        "x": initial_x_258,
                        "y": initial_y,
                        "z": 24
            }
        }
        labware_template["wells"] = wells_data
        labware_template["groups"][0]["wells"] = ["A1", "B1", "C1"]

    return labware_template

def generate_labware_zip_file(test_type, num_wells, x_right_most, y_right_most, x_second=None, y_second=None):
    """
    Return a zip file byte stream containing the labware files
    """
    # only allow 1 or 2 wells
    if num_wells not in [1, 2]:
        return

    # Create files for each slot set
    slot_sets = {
        "147": f"rtWIZARD Slot A: {test_type}",
        "258": f"rtWIZARD Slot B: {test_type}",
        "369": f"rtWIZARD Slot C: {test_type}"
    }

    # send the zip file as a byte stream to the parent process call
    # this way no files are created on the server
    stream = BytesIO()
    with ZipFile(stream, 'w') as zf:
        for slots, display_name in slot_sets.items():
            labware_data = generate_labware_template(num_wells, slots, x_right_most, y_right_most, x_second, y_second)
            labware_data["metadata"]["displayName"] = display_name
            labware_data["parameters"]["loadName"] = f"rtwizard_slot_{slots.lower()}_{test_type}"
            zf.writestr(f"rtwizard_labware_slot_{slots}.json", json.dumps(labware_data, indent=4))
    stream.seek(0)
    return stream
