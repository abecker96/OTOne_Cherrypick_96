# OTOne_Cherrypick_96
	This program runs a cherrypicking protocol on the OpenTrons OT One
automated pipetting machine. It determines its routine based on a CSV file
to be placed on the desktop in the following format


Source Plate    Source Well    Destination Plate    Destination Well    Amount to transfer(uL)


There is an example CSV in the repository with the .py file.

Machine Layout:
|-------|-------|-------|-------|-------|
|       |       |       |       |       |
|       |       |       |       |       |
|   2   |   5   |   8   |   11  |  14   |
|       |       |       |       |(bad)  |
|       |       |       |       |       |
|-------|-------|-------|-------|-------|
|       |       |       |       |       |
|       |       |       |       |       |
|   1   |   4   |   7   |   10  |  13   |
|       |       |       |       |(bad)  |
|       |       |       |       |       |
|-------|-------|-------|-------|-------|
|       |       |       |       |       |
|       |       |       |       |       |
|   0   |   3   |   6   |   9   |  12   |
|       |       |       |       |(bad)  |
|       |       |       |       |       |
|-------|-------|-------|-------|-------|
IMPORTANT NOTE:
	Plates 12, 13, and 14 ARE NOT ACCESSIBLE.
	Do not try to use them as either source or destination plates.

The OpenTrons app uses calibration data that is linked to a user's account. When running for the first time, the app will need to be calibrated.
	There are two files on git that will set you calibration data. Just download calibrations.json and calibrations.bat to your desktop, and 
	run calibrations.bat. The .json file should disappear, and your app will be calibrated.

Steps for operation:

1:	Create a CSV file to access wells and plates in the format above, and save the file to the desktop as "CherrypickMap.csv"
3:	Open the app on the desktop called "Opentrons 2.0"
4:	On the top right of the app, there is a login button with a little red circle next to it. To the left of that
		is a dropdown menus saying "Select a port". Select COM4, and click "OK" on the prompt that shows up.
		The red circle should turn green, and the machine should move a little.
5:	On the top left of the app, click "Click to Upload", and select "cherrypick_96to96.py"
6:	Click run, and click "OK" on the prompt that shows up.

Make sure that all plates and tipracks are firmly seated in the bottom left corner of their slots, and that the source
	plate is firmly seated in its holder.
