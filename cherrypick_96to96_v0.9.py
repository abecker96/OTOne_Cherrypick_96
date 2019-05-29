from opentrons import robot, containers, instruments

#This program is for cherrypicking from any well in any plate to any well in any plate
#This is functionally very similar to cherrypick_multiplate_96to96 in all of its iterations
#except the end user should only ever have to interface with the first few lines, and 
#plates aren't limited to being source or destination plates, they can be both.
#Last edited 03/21/2019


#IMPORTANT NOTE
# A single channel pipette on the B axis (left side) CANNOT reach
# ANY part of slots E1, E2, or E3. Not even well A1

#Slot positions for tipracks and trashes
tiprack_slots = ['A3']
trash_slots = ['D1', 'D2', 'D3']

#Copy and paste csv here

#cherrypickingmap_csv = """
# 0,A1,0,A1,53
# 0,H1,0,B1,53
# 0,A12,0,G1,53
# 0,H12,0,H1,53
# 1,A1,0,A12,53
# 1,H1,0,B12,53
# 1,A12,0,G12,53
# 1,H12,0,H12,53
# 2,A1,1,A1,53
# 2,H1,1,H1,53
# 2,A12,1,A12,53
# 2,H12,1,H12,53
# """
cherrypickingmap_csv = """
0,H6,3,A1,50
0,B4,3,A2,50
0,C8,3,A3,50
0,F1,3,A4,50
0,B2,3,A5,50
0,F11,3,A6,50
0,H2,3,A7,50
0,C9,3,A8,50
0,H4,3,B1,50
0,E10,3,B2,50
0,A4,3,B3,50
0,G2,3,B4,50
0,D5,3,B5,50
0,B11,3,B6,50
0,D10,3,B7,50
0,F4,3,B8,50
0,G8,3,C1,50
0,D8,3,C2,50
0,H3,3,C3,50
0,B10,3,C4,50
0,E12,3,C5,50
0,D9,3,C6,50
0,G4,3,C7,50
0,C5,4,C8,50
"""

robot.clear_commands()
robot.comment("")
robot.comment("Begin cherrypick_96to96_v0.9.py")




robot.head_speed(6000)  #max 6000
asp_distance = 10		#THIS IS A TEMP NUMBER
						#will be replaced with a better number
asp_overhead = 10		#Extra volume to be aspirated to guarantee all liquid is sucked up

#All slots available as either a destination plate or source plate
slots = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3']

#load tipracks, trashes, source plates, and destination plates
tipracks = [containers.load('tiprack-200ul', slot) for slot in tiprack_slots]
tiptrashes = [containers.load('point', slot) for slot in trash_slots]
plates = [containers.load('96-PCR-tall', slot) for slot in slots]


#Using a single channel 200ul pipette
pipette = instruments.Pipette(
    axis='b',
    channels=1,
    max_volume=200,
    min_volume=20,
    aspirate_speed=250,		#GET NEW VALUE
    dispense_speed=500,
    tip_racks=tipracks,
    trash_container=tiptrashes)


#Format Data
data = [
        [int(src_plate), src_well, int(dest_plate), dest_well, float(vol)]
        for src_plate, src_well, dest_plate, dest_well, vol  in
        [row.split(',') for row in cherrypickingmap_csv.strip().split('\n') if row]
]
      
def run_custom_protocol():
    pipette.pick_up_tip()

    for well_idx, (source_plate, source_well, destination_plate, destination_well, vol) in enumerate(data):

        pipette.transfer(
                vol + asp_overhead, 
                plates[source_plate].wells(source_well).bottom(), 
                plates[destination_plate].wells(destination_well).bottom(18), 
                new_tip='always',
                blow_out = True,
                trash=False,
                )  
     
    robot.home()


run_custom_protocol()


#//Make a dictionary so that source plates can be called from user input
#src_dict = {}
#x = 'src_plate_1'
#y = 'src_plate_2'
#z = 'src_plate_3'
#src_dict[x] = src_plates[0]
#src_dict[y] = src_plates[1]
#src_dict[z] = src_plates[2]
