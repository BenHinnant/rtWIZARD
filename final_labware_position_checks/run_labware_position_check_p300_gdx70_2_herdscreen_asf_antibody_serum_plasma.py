metadata = {"apiLevel": "2.13"}

def run(protocol):
    slot1 = protocol.load_labware('rtwizard_slot_147_gdx70_2_herdscreen_asf_antibody_serum_plasma', 1)
    slot2 = protocol.load_labware('rtwizard_slot_258_gdx70_2_herdscreen_asf_antibody_serum_plasma', 2)
    slot3 = protocol.load_labware('rtwizard_slot_369_gdx70_2_herdscreen_asf_antibody_serum_plasma', 3)
    slot4 = protocol.load_labware('rtwizard_slot_147_gdx70_2_herdscreen_asf_antibody_serum_plasma', 4)
    slot5 = protocol.load_labware('rtwizard_slot_258_gdx70_2_herdscreen_asf_antibody_serum_plasma', 5)
    slot6 = protocol.load_labware('rtwizard_slot_369_gdx70_2_herdscreen_asf_antibody_serum_plasma', 6)
    slot7 = protocol.load_labware('rtwizard_slot_147_gdx70_2_herdscreen_asf_antibody_serum_plasma', 7)
    slot8 = protocol.load_labware('rtwizard_slot_258_gdx70_2_herdscreen_asf_antibody_serum_plasma', 8)
    slot9 = protocol.load_labware('rtwizard_slot_369_gdx70_2_herdscreen_asf_antibody_serum_plasma', 9)
    
    sample_plate = protocol.load_labware('rtwizard_48_well_plate_1100ul_sample_tubes_2ml_rb_tubes', 10)
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
    
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips])
    p300.pick_up_tip()
    p300.return_tip()