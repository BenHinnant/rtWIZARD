metadata = {"apiLevel": "2.13"}

def run(protocol):
    slot1 = protocol.load_labware('rtwizard_slot_147_ingezim_ppa_crom', 1)
    slot2 = protocol.load_labware('rtwizard_slot_258_ingezim_ppa_crom', 2)
    slot3 = protocol.load_labware('rtwizard_slot_369_ingezim_ppa_crom', 3)
    slot4 = protocol.load_labware('rtwizard_slot_147_ingezim_ppa_crom', 4)
    slot5 = protocol.load_labware('rtwizard_slot_258_ingezim_ppa_crom', 5)
    slot6 = protocol.load_labware('rtwizard_slot_369_ingezim_ppa_crom', 6)
    slot7 = protocol.load_labware('rtwizard_slot_147_ingezim_ppa_crom', 7)
    slot8 = protocol.load_labware('rtwizard_slot_258_ingezim_ppa_crom', 8)
    slot9 = protocol.load_labware('rtwizard_slot_369_ingezim_ppa_crom', 9)
    
    sample_plate = protocol.load_labware('rtwizard_48_well_plate_1100ul_sample_tubes_2ml_rb_tubes', 10)
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
    
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips])
    p300.pick_up_tip()
    p300.return_tip()