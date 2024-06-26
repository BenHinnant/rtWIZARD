metadata = {"apiLevel": "2.13"}

def run(protocol):
    slot1 = protocol.load_labware('rtwizard_slot_147_rapid_asfv_ag', 1)
    slot2 = protocol.load_labware('rtwizard_slot_258_rapid_asfv_ag', 2)
    slot3 = protocol.load_labware('rtwizard_slot_369_rapid_asfv_ag', 3)
    slot4 = protocol.load_labware('rtwizard_slot_147_rapid_asfv_ag', 4)
    slot5 = protocol.load_labware('rtwizard_slot_258_rapid_asfv_ag', 5)
    slot6 = protocol.load_labware('rtwizard_slot_369_rapid_asfv_ag', 6)
    slot7 = protocol.load_labware('rtwizard_slot_147_rapid_asfv_ag', 7)
    slot8 = protocol.load_labware('rtwizard_slot_258_rapid_asfv_ag', 8)
    slot9 = protocol.load_labware('rtwizard_slot_369_rapid_asfv_ag', 9)
    
    sample_plate = protocol.load_labware('rtwizard_48_wellplate_1.1ml_sample_tubes_2ml_rb_tubes', 10)
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
    
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips])
    p300.pick_up_tip()
    p300.return_tip()