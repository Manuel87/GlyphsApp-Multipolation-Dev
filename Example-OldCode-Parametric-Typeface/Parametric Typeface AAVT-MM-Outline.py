#MenuTitle: Parametric Typeface AAVT-MM-Outline


# To Do
# ###########################

# 0 (Clean up a bit + a few more comments)
# 1 Seperate in different files: project spec (values+relations) / interpolation script / interface script
# 2 Spec File
# 3 Interpolation Script
# 4 (Interface)


# Spec File
# -----------------------------------------
# Write it up as a json format,
# Include all master claculations / maybe I should take the calculation with the very first master out of the interpolation script
# possiblity to add maped Design values (instead of 0-1 / 0-1000  -> 80-120) (http://bit.ly/25OEsID - stackoverflow: mapping in pyhton)
# possiblity to have a custom min/max for the slider interface
# possiblity for custom parameters (especial Transformation would quite interesting)


# Interface Script
# -----------------------------------------
# Iterate the slider function - so sliders get added depending depending on the master count (I couldnt make it work in python :(
# Names for spec - Write file master names into the spec-file (taking them from Glyphs, wasnt possible in Glyphs 1 (no custom names))
# 		Add extra numerical field for the current instance value
# Save button - with field to specify instance name -> save current values to spec file
# Instance Dropdown -  to select already defined instances
# Indicate when extrapolation happens (maybe colour current value)


# Interpolation / Execution Script
# -----------------------------------------
# Allow design values - add possiblity to specify a custom number for 0 and 1 (eg. 100% is not 1 but 120 (as the stemwidth in that specific master / and 80 for the Parentmaster)
# input fields for custom parameters (maybe even sliders)


# All Files
# -----------------------------------------
# Add y-interpolation support (#1 interpolation script, #2 spec and #3 interface)



# Bugs to fix
# ###########################
# why is the spacing master interpolation not working in Glyphs2 ??   (not sure if in my Glyphsfile or in the script)




# ################################################
# ################################################


# Before Using
# ###########################

# 1 The Main/Root/Initial Master has to be the first one!

# 3 Refelect the design of each Master towards the Root Master

# 4 Check Master-Compatibility eg Point-Count, ...


#################################################
#################################################


# General Settings
#############################
Add_Masters_as_Instances = False
Add_Custom_Parameter = True #eg Filters
Activate_New_Instances = False
Activate_Last_Filter = False

Standard_Filters = ["GlyphsFilterRemoveOverlap;"] #["GlyphsFilterOffsetCurve; 1; 1; 1; 0.5;", "GlyphsFilterRoundCorner; 1; 1;"]
Standard_Filters_Interpolated_Instances = Standard_Filters
Standard_Last_Filter_Interpolated_Instances = ["GlyphsFilterRemoveOverlap;"]

#################################################
#################################################

# Init / Dont touch if you don't understand ;)
#############################



# -*- coding: utf-8 -*-
"""Slider Interpolation for infinite Masters"""

import GlyphsApp
import math
import vanilla



slider_array = []

# M E T R I C S 	---------------------------------------------------------------------

slider_array_0 = ["M Spacing (Tight Kerned)", 0.3]

# S K E L E T O N	---------------------------------------------------------------------
# Proportions		---------------------------------------------------------------------
slider_array_1 = ["P Width (200%)", 0.0]# 	P - Width (200%)

slider_array_2 = ["P Width Variation (n,u,h,m)", 0.3]# 	P - Width - Variation wider n,u,h,m (+100)
#			P - Width - Mono Proportional
slider_array_3 = ["P Width MonoProp", 0.0]
slider_array_4 = ["P UC Size (138%/690)", 0.0] # 	P - UPPERCASE - Size / Height at 690 (138%)
slider_array_5 = ["P UC Width (200%)", 0.25] # 	P - UPPERCASE - Width (200%) / keeping sidebearings
slider_array_6 = ["P UC - Shifted (-190)", 0.0] # 	P - UPPERCASE - Shifted (-190)
slider_array_7 = ["P Ascenders (+100)", 0.0]#
slider_array_8 = ["P Descenders (-100)", 0.0]#
#slider_array_9 = ["P Descenders (-100)", 0.0]#

slider_array_9 = ["P Joints (None)", 0.0]#
slider_array_10 = ["P Joints (Mid)", 1.0]#
slider_array_11 = ["P Joints (Bottom)", 0.0]#

slider_array_12 = ["P Lc Midline (Top)", 0.0]#

slider_array_13 = ["P Exp Extensions(+100)", 0.0]#
slider_array_14 = ["P Exp Smaller Circles (1/2)", 0.0]#

#			...
# Slant / Slope / ...	---------------------------------------------------------------------
#			A - Slant - Horizontal - Vertical - Z-Horizontal - Z-Vertical
slider_array_15 = ["C MiddleTop-to-Outer Side", 0.0]#  	A - Middle - Top - to Outer Side: n,h,u,m,p,d,b,q (not o, e, ...)
#			A - Middle - Bottom  - to Outer side
#			A - Middle - Left  -  to Top
#			A - Middle - Right  - to Top
# Curvature		---------------------------------------------------------------------

slider_array_16 = ["C Cubic (70%) ", 0.0]#
slider_array_17 = ["C Broken (10%) ", 0.0]#
slider_array_18 = ["C Joints Angle", 0.0]#
slider_array_19 = ["C Expand/vSlant Corners", 0.0]#  Expand (and vSlant)


# O U T L I N E - S K E L E T O N  C O M P E N S A T I O N - Keep Proportions, ... ----------
# StokeWidth		---------------------------------------------------------------------
#Master_1 = slider_2/2 # 	Comp - Strokewidth - Scale y (-200)
#Master_2 = slider_2/2 # 	Comp - Strokewidth - Scale x (-200)
#Master_5 = 0.0 # 	Comp - Strokewidth - Scale Proportional (as y(-200) -> 66,67)
#Master_6 = 0.0 # 	Comp - TerminalStyle - Rounded Corners - Optical Correction - Baseline Terminal Overshoot (+10)
#Master_4 = slider_2/2 +0.1 # 	Comp - TerminalStyle - Sharp Corners - Glyphs Path Offset - Extend Terminals  (+200)


# O U T L I N E 	(with Second Root Master) -------------------------------------------
#			---------------------------------------------------------------------
# StokeWidth		---------------------------------------------------------------------
slider_array_20 = ["O Srokewidth", 0.8]#
slider_array_21 = ["O -> Inner Skeleton Scale", 0.0]#
slider_array_22 = ["O -> Inner Horizontal Skeleton", 0.0]#
slider_array_31 = ["O -> Inner Vertical Skeleton", 0.0]#
slider_array_23 = ["O -> Black", 0.0]#


slider_array_24 = ["P Width (m) inner-n-proportion", 0.0]#

slider_array_25 = ["O Contrast Vertical", 0.0]#
slider_array_26 = ["O Contrast Joints", 0.0]#


slider_array_27 = ["O Terminal Angle (All)", 0.0]#
slider_array_28 = ["O Contrast Diagonal", 0.0]#

slider_array_29 = ["O UC Strokewidth", 0.0]#

slider_array_30 = ["M Monospaced (600)", 0.0]#

slider_array.append([slider_array_0, slider_array_1, slider_array_2, slider_array_3, slider_array_4, slider_array_5, slider_array_6, slider_array_7, slider_array_8, slider_array_9, slider_array_10, slider_array_11, slider_array_12, slider_array_13, slider_array_14, slider_array_15, slider_array_16, slider_array_17, slider_array_18, slider_array_19, slider_array_20, slider_array_21, slider_array_22, slider_array_23, slider_array_24, slider_array_25, slider_array_26, slider_array_27, slider_array_28, slider_array_29, slider_array_30, slider_array_31])

slider = []
slider_array = slider_array[0]
slider_count = len(slider_array)
for k in range(0, slider_count, 1):
	slider.append(slider_array[k][1])

print slider
print slider[20]

Doc  = Glyphs.currentDocument
Font = Glyphs.font

interpol_array = []
Instances = Font.instances
Masters = Font.masters
Master_Count = len(Masters)
Instances_Count = len(Instances)
print "Mastercount"
print Master_Count

# clear values
Instance_reset_Values = []

for k in range(0, Master_Count-1, 1):
	Instance_reset_Values = Instance_reset_Values + [0.0] #.append(0.0)


# sets each Master as an Instances
if(Add_Masters_as_Instances):
	#Add Root as Instance
	interpol_array.append(Instance_reset_Values+["0 - Root-Master"]+[Standard_Filters])
	#interpol_array.append("0 - Root-Master")


	#Add other Masters
	for j in range(1, Master_Count, 1): #0, Master_Count-1, 1)
		interpol_array.append(Instance_reset_Values[:]) # use as a copy
		interpol_array[-1][j-1]=1.0
		interpol_array[-1].append(Masters[j].name)#j+1) #Master name (1, 2, ...)
		interpol_array[-1].append(Standard_Filters)


print interpol_array

import inspect
import copy
import math

#def toString(myNumber):
#	str(decimal.Decimal('0.1'))


def func(a, b, c):
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    print 'function name "%s"' % inspect.getframeinfo(frame)[2]
    for i in args:
        print "    %s = %s" % (i, values[i])
    return [(i, values[i]) for i in args]





#NSClassFromString("GSCustomParameter").__init__()#NSClassFromString("GSCustomParameter").__init__()#.alloc().init()


def AddInstance(myname, myfilters):
	newInstance = GSInstance()
	newInstance.active = Activate_New_Instances
	newInstance.name = myname #prefix + "{0:.0f}".format( thisWeight )
	newInstance.weightValue = 1
	newInstance.widthValue = 1
	newInstance.isItalic = False
	newInstance.isBold = False

	if Add_Custom_Parameter:
		if myfilters[0]:
			newInstance.customParameters["Filter"] = myfilters[0]
			myfilters = myfilters + Standard_Last_Filter_Interpolated_Instances
			myfilters_Count = len(myfilters)

			for k in range(1, myfilters_Count, 1):
				#myCustomParameter = copy.copy(myCustomParameter)
				newInstance.customParameters["Filter"] = myfilters[k]

	Glyphs.font.addInstance_( newInstance )






#################################################
#################################################


def process( slider, interpol_array ):

	#print sliderPos
	print interpol_array

	interpol_array = []
	InstancesNames = []
	Instances_Count = len(Instances)


	# Interpolation Settings (Change Values as needed)
	#################################################



	#Basis
	neutral_bx_decrement = 0.8
	Master_1 = 0.0 # Bolden y 200
	Master_2 = 0.0 # Bolden x 200
	Master_3 = 0.0 # P Widen Width 200%
	Master_4 = 0.0 # Correction Offset Terminals for sharp corners
	Master_5 = 0.0 # Bolden Proporitonal Scale (as y200 ->66,67)
	Master_6 = 1.0 # Correction Rounded Baseline Terminal Overshoot
	Master_7 = 1.0 # Curvature Cubic (70)
	Master_8 = 0.0 # Upercase Size / Height at 690 (138%)
	Master_9 = 0.0 # Uppercase Width (200%) / keeping sidebearings
	Master_10 = 0.0 # S Tightest Spacing/Kerning 107(0)--19(1)
	Master_11 = 0.0 # S MetricWidth 200% / keepinitialbounds (widen 200%)
	Master_12 = 0.0 # P WidthVariation wider n,u,h,m +100
	Master_13 = 0.0 # P Ascenders -100
	Master_14 = 0.0 # P Descenders -100
	Master_15 = 0.0 # P Joints low
	Master_16 = 0.0 # P lowercase high midline
	Master_17 = 0.0 # P baseline shifts / inner extensions (+100)
	Master_18 = 0.0 # Curvature Broken (10)
	Master_19 = 0.0 # Curvature Joint Angle
	Master_20 = 0.0 # N inner top to outer side: n,h,u,m,p,d,b,q
	Master_21 = 0.0 # P smaller circles (1/2) towards x-height
	Master_22 = 0.0 # P Joints None
	Master_23 = 0.0 # C Expand Sharp Corners
	Master_24 = 0.0 # P Joints on Midline
	Master_25 = 0.0 # P Shifted Caps (-190)
	Master_26 = 0.0 # KK Outline (59.52*2 -> 119,04 --> 100)
	Master_27 = 0.0 # KK Fat / Black / Negative Skeleton
	Master_28 = 0.0 # KK Terminal Angles
	Master_29 = 0.0 # KK Contrast
	Master_30 = 0.0 # KK Contrast Thin Joints
	Master_31 = 0.0 # KK Terminal Angles2
	Master_32 = 0.0 # KK Contrast AngleTest
	Master_33 = 0.0 # m - black proportion compensation
	Master_34 = 0.0 #	P - Width - Mono Proportional
	Master_35 = 0.0 # KK Outline -> Only UPPERCASE
	Master_36 = 0.0 # M Monospaced



	#######################################################################
	#######################################################################
	#######################################################################
	#######################################################################




	# Master_0 = Root
	Master_1 = 0.4 # Bolden y 200
	Master_2 = 0.4 # Bolden x 200
	Master_3 = 0.0 # P Widen Width 200%
	Master_4 = 0.45 # Correction Offset Terminals for sharp corners
	Master_5 = 0.0 # Bolden Proporitonal Scale (as y200 ->66,67)
	Master_6 = 0.0 # Correction Rounded Baseline Terminal Overshoot
	Master_10 = 0.3 # S Tightest Spacing/Kerning 107(0)--19(1)  # 107-0,3*(107-19) = 80,6 -> 161,2 (un)

	#######################################################################
	#######################################################################
	#######################################################################




	InstanceName = "Plain"  # spaced03 Uppercase widthvar n02
	#--------------------
	Master_3 = 0.0 # P Widen Width 200%
	Master_7 = 0.0 # Curvature Cubic (70)
	Master_8 = 1.0 # Upercase Size / Height at 690 (138%)
	Master_9 = 0.0 # Uppercase Width (200%) / keeping sidebearings
	Master_11 = 0.0 # S MetricWidth 200% / keepinitialbounds (widen 200%)
	Master_12 = 0.2 # P WidthVariation wider n,u,h,m +100
	Master_13 = 0.0 # P Ascenders -100
	Master_14 = 0.0 # P Descenders -100
	Master_15 = 0.0 # P Joints low
	Master_16 = 0.0 # P lowercase high midline
	Master_17 = 0.0 # P baseline shifts / inner extensions (+100)
	Master_18 = 0.0 # Curvature Broken (10)
	Master_19 = 0.0 # Curvature Joint Angle
	Master_20 = 0.0 # N inner top to outer side: n,h,u,m,p,d,b,q
	Master_21 = 0.0 # P smaller circles (1/2) towards x-height
	Master_22 = 0.0 # P Joints None
	Master_23 = 0.0 # C Expand Sharp Corners
	Master_24 = 0.0 # P Joints on Midline
	Master_25 = 0.0 # P Shifted Caps (-190)
	Master_26 = 0.8 - 0.1 # KK Outline (59.52*2 -> 119,04 --> 100)
	Master_27 = 0.0 # KK Fat / Black / Negative Skeleton
	Master_28 = 0.0 # KK Terminal Angles
	Master_29 = 0.1 # KK Contrast
	Master_30 = 0.0 # KK Contrast Thin Joints
	Master_31 = 0.0 # KK Terminal Angles2
	Master_32 = 0.0 # KK Contrast AngleTest
	Master_33 = 0.0 # m - black proportion compensation
	Master_34 = 0.0 #	P - Width - Mono Proportional
	Master_35 = 0.0 # KK Outline -> Only UPPERCASE
	Master_36 = 0.0 # M Monospaced
	Master_37 = 0.0 # M +100 (left+right)
	#
	Filter = Standard_Filters_Interpolated_Instances
	#
	interpol_array.append([Master_1, Master_2, Master_3, Master_4, Master_5, Master_6, Master_7, Master_8, Master_9, Master_10, Master_11, Master_12, Master_13, Master_14, Master_15, Master_16, Master_17, Master_18, Master_19, Master_20, Master_21, Master_22, Master_23, Master_24, Master_25, Master_26, Master_27, Master_28, Master_29, Master_30, Master_31, Master_32, Master_33, Master_34, Master_35, Master_36, InstanceName, Filter])






	InstanceName = "SliderInstance"  # spaced03 Uppercase widthvar n02
	#--------------------

	# M E T R I C S 	---------------------------------------------------------------------
	Master_10 = slider[0] # 0.3 	M - Tightest Spacing/Kerning (107(0)--19(1))  # 107-0,3*(107-19) = 80,6 -> 161,2 (un)
	Master_36 = slider[30] # M - Mono Spaced
	Master_37 = slider[22]*((slider[20])/2*1.19) # M - +100 (left+right)

	# S K E L E T O N	---------------------------------------------------------------------
	# Proportions		---------------------------------------------------------------------
	Master_3 = slider[1] # 	P - Width (200%)
	Master_11 = slider[1] # 	P - 	 Metric Compensation (Sidebearings 200%) / keepinitialbounds (for Width 200%)
	Master_12 = slider[2] # 0.2 	P - Width - Variation wider n,u,h,m (+100)
	Master_34 = slider[3] #	P - Width - Mono Proportional

	Master_8 = slider[4] # 	P - UPPERCASE - Size / Height at 690 (138%)
	Master_9 = slider[5] # 	P - UPPERCASE - Width (200%) / keeping sidebearings
	Master_25 = slider[6] # 	P - UPPERCASE - Shifted (-190)
	Master_13 = slider[7] # 	P - Ascenders (-100)
	Master_14 = slider[8] # 	P - Descenders (-100)
	Master_22 = slider[9] # 0.2	P - Joints - to Top (None)
	Master_24 = slider[10] # 	P - Joints - to Midline (~Optical Middle)
	Master_15 = slider[11] # 	P - Joints - to Bottom (Bottom)
	Master_16 = slider[12] # 	P - Lc Midline - to Top // only Lowercase
	Master_17 = slider[13] # 	P - Exp - baseline Shifts / random Extensions (+100)
	Master_21 = slider[14] #  	P - Exp - smaller Circles (1/2 towards x-height)
	#			...
	# Slant / Slope / ...	---------------------------------------------------------------------
	#			A - Slant - Horizontal - Vertical - Z-Horizontal - Z-Vertical
	Master_20 = slider[15] # 	A - Middle - Top - to Outer Side: n,h,u,m,p,d,b,q (not o, e, ...)
	#			A - Middle - Bottom  - to Outer side
	#			A - Middle - Left  -  to Top
	#			A - Middle - Right  - to Top
	# Curvature		---------------------------------------------------------------------
	Master_7 = slider[16] # 	C - Cubic (C 70%)
	Master_18 = slider[17] # 	C - Broken (C 10%)
	Master_19 = slider[18] # 	C - Joints Angle
	Master_23 = slider[19] # 	C - Sharp Corners - Expand (and vSlant)




	# O U T L I N E - S K E L E T O N  C O M P E N S A T I O N - Keep Proportions, ... ----------
	# StokeWidth		---------------------------------------------------------------------
	Master_1 = (slider[20]-(slider[20]*slider[31]))/2*1.19 - slider[23]/230*119 # 	Comp - Strokewidth - Scale y (-200)
	Master_2 = (slider[20]-(slider[20]*slider[22]))/2*1.19 - slider[23]/230*119 - (slider[21])*(slider[20]/2*1.19) #	Comp - Strokewidth - Scale x (-200)
	Master_5 = (slider[21]/2*1.19)*(slider[20]) #(slider[20]-(slider[20]*slider[21]))/2 # 	Comp - Strokewidth - Scale x Proportional (as y(-200) -> 66,67)
	Master_6 = 0.0 # 	Comp - TerminalStyle - Rounded Corners - Optical Correction - Baseline Terminal Overshoot
	Master_4 = slider[20]/2*1.19 - slider[23]/230*119 #+ 0.1 # 	Comp - TerminalStyle - Sharp Corners - Glyphs Path Offset - Extend Terminals  (+200)
	Master_33 = slider[24] # m - black proportion compensation

	# O U T L I N E 	(with Second Root Master) -------------------------------------------
	#			---------------------------------------------------------------------
	# StokeWidth		---------------------------------------------------------------------
	Master_26 = slider[20] - slider[23]/130*119 # ROOT2	KK - Strokewidth (+119 instead of 100 unfortunatly) // - 0.8 - 0.4 - 0.0 - 0.4 + 0.1 # KK Outline (59.52*2 -> 119,04 --> 100)
	Master_35 = slider[29] # KK Outline -> Only UPPERCASE

	Master_27 = slider[23] # 	KK - Strokewidth - Fat/Black/Negative Skeleton (Maximum, while keeping proportions)
	# Contrast		---------------------------------------------------------------------
	Master_29 = (slider[20]/100*119)*slider[25] # 0.1	KK - Contrast - Vertical
	Master_30 = (slider[20]/101*100)*slider[26] # 0.5	KK - Contrast - Thin Joints
	# Angles		---------------------------------------------------------------------
	Master_28 = slider[20] - slider[23]/130*119# 	KK - Terminal Angles (only straighten diagonal terminals: v,x,w,k)
	Master_31 = slider[27] # 	KK - Terminal Angles2
	Master_32 = slider[28] # KK Contrast AngleTest


	# Second Root Master Calculation
	Master_26 = Master_26 - Master_27 - Master_28 - Master_29 - Master_30 - Master_31 - Master_32
	#
	Filter = Standard_Filters_Interpolated_Instances
	#
	interpol_array.append([Master_1, Master_2, Master_3, Master_4, Master_5, Master_6, Master_7, Master_8, Master_9, Master_10, Master_11, Master_12, Master_13, Master_14, Master_15, Master_16, Master_17, Master_18, Master_19, Master_20, Master_21, Master_22, Master_23, Master_24, Master_25, Master_26, Master_27, Master_28, Master_29, Master_30, Master_31, Master_32, Master_33, Master_34, Master_35, Master_36, Master_37, InstanceName, Filter])






	InstanceName = "BlackRoman"  # zKK RomanBlack spaced03 Uppercase widthvar n02
	#--------------------

	# M E T R I C S 	---------------------------------------------------------------------
	Master_10 = 0.3 # 	S - Tightest Spacing/Kerning (107(0)--19(1))  # 107-0,3*(107-19) = 80,6 -> 161,2 (un)
	#			S - Mono Spaced
	Master_37 = 0 # M - +100 (left+right)

	# S K E L E T O N	---------------------------------------------------------------------
	# Proportions		---------------------------------------------------------------------
	Master_3 = 0.3 # 	P - Width (200%)
	Master_11 = 0.3 # 	P - 	 Metric Compensation (Sidebearings 200%) / keepinitialbounds (for Width 200%)
	Master_12 = 0.0 # 	P - Width - Variation wider n,u,h,m (+100)
	#			P - Width - Mono Proportional
	Master_8 = 1.0 # 	P - UPPERCASE - Size / Height at 690 (138%)
	Master_9 = 0.0 # 	P - UPPERCASE - Width (200%) / keeping sidebearings
	Master_25 = 0.0 # 	P - UPPERCASE - Shifted (-190)
	Master_13 = 0.0 # 	P - Ascenders (-100)
	Master_14 = 0.0 # 	P - Descenders (-100)
	Master_22 = 0.0 # 	P - Joints - to Top (None)
	Master_24 = 0.0 # 	P - Joints - to Midline (~Optical Middle)
	Master_15 = 0.9 # 	P - Joints - to Bottom (Bottom)
	Master_16 = 0.0 # 	P - Lc Midline - to Top // only Lowercase
	Master_17 = 0.0 # 	P - Exp - baseline Shifts / random Extensions (+100)
	Master_21 = 0.0 #  	P - Exp - smaller Circles (1/2 towards x-height)
	#			...
	# Slant / Slope / ...	---------------------------------------------------------------------
	#			A - Slant - Horizontal - Vertical - Z-Horizontal - Z-Vertical
	Master_20 = 0.2 # 	A - Middle - Top - to Outer Side: n,h,u,m,p,d,b,q (not o, e, ...)
	#			A - Middle - Bottom  - to Outer side
	#			A - Middle - Left  -  to Top
	#			A - Middle - Right  - to Top
	# Curvature		---------------------------------------------------------------------
	Master_7 = 0.4 # 	C - Cubic (C 70%)
	Master_18 = 0.0 # 	C - Broken (C 10%)
	Master_19 = 0.0 # 	C - Joints Angle
	Master_23 = 0.0 # 	C - Sharp Corners - Expand (and vSlant)


	# O U T L I N E - S K E L E T O N  C O M P E N S A T I O N - Keep Proportions, ... ----------
	# StokeWidth		---------------------------------------------------------------------
	Master_1 = 0.5 - 0.1# 	Comp - Strokewidth - Scale y (-200)
	Master_2 = 0.0   # 	Comp - Strokewidth - Scale x (-200)
	Master_5 = 0.5 # 	Comp - Strokewidth - Scale x Proportional to y (as y(-200) -> 66,67)
	Master_6 = 0.0 # 	Comp - TerminalStyle - Rounded Corners - Optical Correction - Baseline Terminal Overshoot
	Master_4 = 0.4 # 	Comp - TerminalStyle - Sharp Corners - Glyphs Path Offset - Extend Terminals  (+200)
	Master_32 = 0.0 # m - black proportion compensation

	# O U T L I N E 	(with Second Root Master) -------------------------------------------
	#			---------------------------------------------------------------------
	# StokeWidth		---------------------------------------------------------------------
	Master_26 = 0.8 # 0.8 R O O T 2 - KK - Strokewidth (+100) // - 0.8 - 0.4 - 0.0 - 0.4 + 0.1 # KK Outline (59.52*2 -> 119,04 --> 100)
	Master_35 = 0.0 #   KK - Strokewidth Uppercase
	Master_27 = 1.0 # 	KK - Strokewidth - Fat/Black/Negative Skeleton (Maximum, while keeping proportions)
	# Contrast		---------------------------------------------------------------------
	Master_29 = 0.6 # 	KK - Contrast - Vertical
	Master_30 = 1.0 # 	KK - Contrast - Thin Joints
	# Angles		---------------------------------------------------------------------
	Master_28 = 1.0 # 	KK - Terminal Angles (only straighten diagonal terminals: v,x,w,k)
	Master_31 = 0.1 # 	KK - Terminal Angles2


	# Second Root Master Calculation
	Master_26 = Master_26 - Master_27 - Master_28 - Master_29 - Master_30 - Master_31
	#
	Filter = Standard_Filters_Interpolated_Instances
	#
	interpol_array.append([Master_1, Master_2, Master_3, Master_4, Master_5, Master_6, Master_7, Master_8, Master_9, Master_10, Master_11, Master_12, Master_13, Master_14, Master_15, Master_16, Master_17, Master_18, Master_19, Master_20, Master_21, Master_22, Master_23, Master_24, Master_25, Master_26, Master_27, Master_28, Master_29, Master_30, Master_31, Master_32, Master_33, Master_34, Master_35, Master_36, Master_37, InstanceName, Filter])



	#################################################
	#################################################




	#Excecute / dont't touch if you don't understand ...
	###########################

	Interpol_Count = len(interpol_array)

	print(Interpol_Count)
	print("Setups for Interpolation")
	print(Instances_Count)
	print("Instances")


	#Add Instances if needed
	if(Instances_Count < Interpol_Count):
		#print("Please add more Instances in the info dialog.")
		Missing_Instances_Count = Interpol_Count-Instances_Count
		print(Missing_Instances_Count)
		print("missing Instances")
		print("")

		#print(interpol_array)



		for k in range(0, Missing_Instances_Count, 1):
			#print(interpol_array[k][-1]);
			#     			name			filters
			AddInstance(interpol_array[Instances_Count+k][-2], interpol_array[Instances_Count+k][-1]) #Instances_Count + k
			print("Instance added")


	###########################

	for i in range(0, len(interpol_array), 1):

		interpol = interpol_array[i]
		Instance = Font.instances[i]

		interpol_sum = 0.0
		Instance.setManualInterpolation_(True)

		multiplemode = 1

		#Instance.instanceInterpolations()[Masters[1].id] = 2.0


		if multiplemode:
			#xrange([start], stop[, step])
			#calc interpol_sum
			for k in range(0, len(interpol)-2, 1): #-2 is excluding the InstanceName + Filter
				interpol_sum += interpol[k] #without first
				#k += 1

			#recalculate the value of the main-master so the sum equals 1.0
			interpol = [1.0 - interpol_sum] + interpol;

			#apply
			for k in range(0, len(interpol)-2, 1): #-1 is excluding the InstanceName + Filter
				#standard interpolation
				#convert values so its sum equals 1.0
				#interpol[k] = interpol[k] / interpol_sum

				#assign to instance

				Instance.instanceInterpolations[Masters[k].id] = interpol[k]

		#print Instance.instanceInterpolations()
		#Doc = Glyphs.currentDocument

		#Refresh the instance preview ()
		numberOfInstances = len( Glyphs.font.instances )

		try:
			currentInstanceNumber = Doc.windowController().activeEditViewController().selectedInstance()

			if currentInstanceNumber < numberOfInstances:
				Doc.windowController().activeEditViewController().setSelectedInstance_( currentInstanceNumber + 1 )
			else:
				Doc.windowController().activeEditViewController().setSelectedInstance_( 1 )


			currentInstanceNumber = Doc.windowController().activeEditViewController().selectedInstance()

			if currentInstanceNumber > 1:
				Doc.windowController().activeEditViewController().setSelectedInstance_( currentInstanceNumber - 1 )
			else:
				Doc.windowController().activeEditViewController().setSelectedInstance_( numberOfInstances )

		except Exception, e:
			print "Error:", e


print("process########")
print(slider)
print(slider[20])
process( slider, interpol_array)





class LivePolation( object ):
	def __init__( self ):

		zeile = 0
		zeilenabstand = 25
		windowHeight = 30 * zeilenabstand
		sliderLength = 100
		MinMaxWidth = 15;


		#for j in range(0, slider_count -1, 1):
		#	slider.append()
		#	slider[0] = "klj"



		# self.w.sliderMin = [0,1]
		# self.w.sliderMax = [0,1]
		# self.w.slider = [0,1]

		#self.w.addToolbar(vanilla.EditText( ( 15+0, 12+zeile-1, 50, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences ), "test")

		#print(self.w.my_compactDescription())
		#self.w.newXPCObject("sliderMin", vanilla.EditText( ( 15+0, 12+zeile-1, 50, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences ))

		# 	obj = someobject
		# 	obj.a = lambda: None
		# setattr(obj.a, 'somefield', 'somevalue')


		#params = ['sliderMin', 'attr2', 'attr3']
		#value =
		#for p in params:
		#	self.w.add(p, )
		#print("######k##")
		#print(self.w.sliderMin)
		#self.w._createToolbarItem(vanilla.EditText( (-15-50, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences ))



		self.w = vanilla.FloatingWindow( (300, windowHeight), "Live Multipolation", minSize=(300, windowHeight), maxSize=(1000, windowHeight), autosaveName="com.manuel.LivePolation.mainwindow" )


		textWidth = 30

		myname = slider_array[0][0]
		myvalue = slider_array[0][1]

		self.w.sliderMin_0 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( -1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_0 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_0 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue/2+0.5, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_0 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )



		myname = slider_array[30][0]
		myvalue = slider_array[30][1]
		zeile += zeilenabstand
		self.w.sliderMin_30 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_30 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_30 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_30 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )








		myname = slider_array[1][0]
		myvalue = slider_array[1][1]
		zeile += zeilenabstand
		self.w.sliderMin_1 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( -1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_1 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_1 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue/2+0.5, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_1 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )



		myname = slider_array[2][0]
		myvalue = slider_array[2][1]
		zeile += zeilenabstand
		self.w.sliderMin_2 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_2 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_2 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_2 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )




		myname = slider_array[3][0]
		myvalue = slider_array[3][1]
		zeile += zeilenabstand
		self.w.sliderMin_3 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_3 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_3 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_3 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )





		myname = slider_array[4][0]
		myvalue = slider_array[4][1]
		zeile += zeilenabstand
		self.w.sliderMin_4 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_4 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 2.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_4 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_4 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )





		myname = slider_array[5][0]
		myvalue = slider_array[5][1]
		zeile += zeilenabstand
		self.w.sliderMin_5 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( -1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_5 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_5 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue/2+0.5, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_5 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )



		myname = slider_array[6][0]
		myvalue = slider_array[6][1]
		zeile += zeilenabstand
		self.w.sliderMin_6 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_6 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_6 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_6 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )


		"""
		myname = slider_array[7][0]
		myvalue = slider_array[7][1]
		zeile += zeilenabstand
		self.w.sliderMin_7 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_7 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_7 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_7 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )




		myname = slider_array[8][0]
		myvalue = slider_array[8][1]
		zeile += zeilenabstand
		self.w.sliderMin_8 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_8 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_8 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_8 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )
		"""


		myname = slider_array[9][0]
		myvalue = slider_array[9][1]
		zeile += zeilenabstand
		self.w.sliderMin_9 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( -1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_9 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_9 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue/2+0.5, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_9 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )


		myname = slider_array[10][0]
		myvalue = slider_array[10][1]
		zeile += zeilenabstand
		self.w.sliderMin_10 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_10 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_10 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_10 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )


		myname = slider_array[11][0]
		myvalue = slider_array[11][1]
		zeile += zeilenabstand
		self.w.sliderMin_11 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_11 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_11 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_11 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )


		myname = slider_array[12][0]
		myvalue = slider_array[12][1]
		zeile += zeilenabstand
		self.w.sliderMin_12 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_12 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_12 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_12 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )


		myname = slider_array[13][0]
		myvalue = slider_array[13][1]
		zeile += zeilenabstand
		self.w.sliderMin_13 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_13 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_13 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_13 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )


		#myname = slider_array[14][0]
		#myvalue = slider_array[14][1]
		#zeile += zeilenabstand
		#self.w.sliderMin_14 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		#self.w.sliderMax_14 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		#self.w.sliderButton_14 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		#self.w.sliderLabel_14 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )

		myname = slider_array[15][0]
		myvalue = slider_array[15][1]
		zeile += zeilenabstand
		self.w.sliderMin_15 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_15 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_15 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_15 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )

		myname = slider_array[16][0]
		myvalue = slider_array[16][1]
		zeile += zeilenabstand
		self.w.sliderMin_16 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( -2.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_16 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 2.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_16 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue/4+0.5, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_16 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )


		myname = slider_array[17][0]
		myvalue = slider_array[17][1]
		zeile += zeilenabstand
		self.w.sliderMin_17 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_17 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_17 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_17 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )

		myname = slider_array[18][0]
		myvalue = slider_array[18][1]
		zeile += zeilenabstand
		self.w.sliderMin_18 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_18 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_18 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_18 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )

		myname = slider_array[19][0]
		myvalue = slider_array[19][1]
		zeile += zeilenabstand
		self.w.sliderMin_19 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_19 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_19 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_19 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )



		myname = slider_array[20][0]
		myvalue = slider_array[20][1]
		zeile += zeilenabstand
		self.w.sliderMin_20 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( -2.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_20 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 2.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_20 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue/4+0.5, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_20 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )




		myname = slider_array[29][0]
		myvalue = slider_array[29][1]
		zeile += zeilenabstand
		self.w.sliderMin_29 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_29 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_29 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_29 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )





		myname = slider_array[21][0]
		myvalue = slider_array[21][1]
		zeile += zeilenabstand
		self.w.sliderMin_21 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_21 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_21 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_21 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )


		myname = slider_array[22][0]
		myvalue = slider_array[22][1]
		zeile += zeilenabstand
		self.w.sliderMin_22 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_22 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_22 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_22 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )



		myname = slider_array[31][0]
		myvalue = slider_array[31][1]
		zeile += zeilenabstand
		self.w.sliderMin_31 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_31 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_31 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_31 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )


		myname = slider_array[23][0]
		myvalue = slider_array[23][1]
		zeile += zeilenabstand
		self.w.sliderMin_23 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_23 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_23 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_23 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )



		#myname = slider_array[24][0]
		#myvalue = slider_array[24][1]
		##zeile += zeilenabstand
		#self.w.sliderMin_24 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		#self.w.sliderMax_24 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		#self.w.sliderButton_24 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		#self.w.sliderLabel_24 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )




		myname = slider_array[25][0]
		myvalue = slider_array[25][1]
		zeile += zeilenabstand
		self.w.sliderMin_25 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( -1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_25 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_25 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue/2+0.5, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_25 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )




		myname = slider_array[26][0]
		myvalue = slider_array[26][1]
		zeile += zeilenabstand
		self.w.sliderMin_26 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_26 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_26 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_26 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )




		myname = slider_array[27][0]
		myvalue = slider_array[27][1]
		zeile += zeilenabstand
		self.w.sliderMin_27 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_27 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_27 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_27 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )



		myname = slider_array[28][0]
		myvalue = slider_array[28][1]
		zeile += zeilenabstand
		self.w.sliderMin_28 = vanilla.EditText( ( 15+0, 12+zeile-1, textWidth, 19), str( 0.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderMax_28 = vanilla.EditText( (-15-textWidth, 12+zeile-1, -15, 19), str( 1.0 ), sizeStyle='small', callback=self.SavePreferences )
		self.w.sliderButton_28 = vanilla.Slider((15+0+textWidth+10, 12+zeile, -15-textWidth-10, 19), value=myvalue, minValue=0.0, maxValue=1.0, sizeStyle='small', callback=self.LivePolationMain )
		self.w.sliderLabel_28 = vanilla.TextBox( (15+0+textWidth+10, 3+zeile, -15-textWidth-10, 19), myname, sizeStyle='small' )






		zeile += zeilenabstand
		self.w.liveSlider    = vanilla.CheckBox((15+3, 12+zeile, -15, 19), "Live slider", value=False, sizeStyle='small' )
		#self.w.useBackground = vanilla.CheckBox((15+3, 12+zeile+20, -15, 19), "Keep paths in background", value=True, sizeStyle='small', callback=self.SavePreferences )

		self.w.runButton = vanilla.Button((-80-15, -20-15, -15, -15), "Calc", sizeStyle='regular', callback=self.LivePolationMain )
		self.w.setDefaultButton( self.w.runButton )

		print("interface set up")

		try:
			self.LoadPreferences()
		except:
			pass

		self.w.open()

	def SavePreferences( self, sender ):
		try:
			#Glyphs.defaults["com.manuel.LivePolation.sliderMin_0"] = self.w.sliderMin_0.get()
			#Glyphs.defaults["com.manuel.LivePolation.sliderMax_0"] = self.w.sliderMax_0.get(_)
			#Glyphs.defaults["com.manuel.LivePolation.sliderButton_0"] = self.w.sliderButton_0.get()
			Glyphs.defaults["com.manuel.LivePolation.liveSlider"] = self.w.liveSlider.get()
			#Glyphs.defaults["com.manuel.LivePolation.useBackground"] = self.w.useBackground.get()
		except:
			return False

		return True

	def LoadPreferences( self ):
		try:
			#self.w.sliderMin_0.set( Glyphs.defaults["com.manuel.LivePolation.sliderMin_0"] )
			#self.w.sliderMax_0.set( Glyphs.defaults["com.manuel.LivePolation.sliderMax_0"] )
			#self.w.sliderButton_0.set( Glyphs.defaults["com.manuel.LivePolation.sliderButton_0"] )
			self.w.liveSlider.set( Glyphs.defaults["com.manuel.LivePolation.liveSlider"] )
			#self.w.useBackground.set( Glyphs.defaults["com.manuel.LivePolation.useBackground"] )
		except:
			return False

		return True

	def LivePolationMain( self, sender ):

		try:
			if ( bool(self.w.liveSlider.get()) and sender == self.w.sliderButton_0 ) or sender != self.w.sliderButton_0:
				Font = Glyphs.font
				FontMaster = Font.selectedFontMaster
				selectedLayers = Font.selectedLayers
				# deleteComponents = bool( self.w.replaceComponents.get() )
				#deleteComponents = True
				#componentName = self.w.componentName.get()


				print("#calculate")
				print(slider)
				print(slider[20])

				sliderMin_0 = float( self.w.sliderMin_0.get() )
				sliderMax_0 = float( self.w.sliderMax_0.get() )
				sliderPos_0 = float( self.w.sliderButton_0.get() )
				slider[0] = sliderMin_0 * ( 1.0 - sliderPos_0 ) + sliderMax_0 * sliderPos_0
				print("lkjkljkjlkjlk")
				print(sliderPos_0)

				sliderPos_0 = (slider[0] - sliderMin_0) / (sliderMax_0-sliderMin_0)

				print(sliderPos_0)
				sliderPos_0 = 1/((1-(sliderMax_0)/sliderMin_0) / ((-slider[1]/sliderMin_0)+1.0))

				print(sliderPos_0)

				sliderMin_1 = float( self.w.sliderMin_1.get() )
				sliderMax_1 = float( self.w.sliderMax_1.get() )
				#self.w.sliderButton_1.set(sliderPos_0)



				sliderPos_1 = float( self.w.sliderButton_1.get() )
				slider[1] = sliderMin_1 * ( 1.0 - sliderPos_1 ) + sliderMax_1 * sliderPos_1

				sliderMin_2 = float( self.w.sliderMin_2.get() )
				sliderMax_2 = float( self.w.sliderMax_2.get() )
				sliderPos_2 = float( self.w.sliderButton_2.get() )
				slider[2] = sliderMin_2 * ( 1.0 - sliderPos_2 ) + sliderMax_2 * sliderPos_2

				sliderMin_3 = float( self.w.sliderMin_3.get() )
				sliderMax_3 = float( self.w.sliderMax_3.get() )
				sliderPos_3 = float( self.w.sliderButton_3.get() )
				slider[3] = sliderMin_3 * ( 1.0 - sliderPos_3 ) + sliderMax_3 * sliderPos_3

				sliderMin_4 = float( self.w.sliderMin_4.get() )
				sliderMax_4 = float( self.w.sliderMax_4.get() )
				sliderPos_4 = float( self.w.sliderButton_4.get() )
				slider[4] = sliderMin_4 * ( 1.0 - sliderPos_4 ) + sliderMax_4 * sliderPos_4

				sliderMin_5 = float( self.w.sliderMin_5.get() )
				sliderMax_5 = float( self.w.sliderMax_5.get() )
				sliderPos_5 = float( self.w.sliderButton_5.get() )
				slider[5] = sliderMin_5 * ( 1.0 - sliderPos_5 ) + sliderMax_5 * sliderPos_5

				sliderMin_6 = float( self.w.sliderMin_6.get() )
				sliderMax_6 = float( self.w.sliderMax_6.get() )
				sliderPos_6 = float( self.w.sliderButton_6.get() )
				slider[6] = sliderMin_6 * ( 1.0 - sliderPos_6 ) + sliderMax_6 * sliderPos_6
				"""
				sliderMin_7 = float( self.w.sliderMin_7.get() )
				sliderMax_7 = float( self.w.sliderMax_7.get() )
				sliderPos_7 = float( self.w.sliderButton_7.get() )
				slider[7] = sliderMin_7 * ( 1.0 - sliderPos_7 ) + sliderMax_7 * sliderPos_7

				sliderMin_8 = float( self.w.sliderMin_8.get() )
				sliderMax_8 = float( self.w.sliderMax_8.get() )
				sliderPos_8 = float( self.w.sliderButton_8.get() )
				slider[8] = sliderMin_8 * ( 1.0 - sliderPos_8 ) + sliderMax_8 * sliderPos_8
				"""
				sliderMin_9 = float( self.w.sliderMin_9.get() )
				sliderMax_9 = float( self.w.sliderMax_9.get() )
				sliderPos_9 = float( self.w.sliderButton_9.get() )
				slider[9] = sliderMin_9 * ( 1.0 - sliderPos_9 ) + sliderMax_9 * sliderPos_9

				sliderMin_10 = float( self.w.sliderMin_10.get() )
				sliderMax_10 = float( self.w.sliderMax_10.get() )
				sliderPos_10 = float( self.w.sliderButton_10.get() )
				slider[10] = sliderMin_10 * ( 1.0 - sliderPos_10 ) + sliderMax_10 * sliderPos_10

				sliderMin_11 = float( self.w.sliderMin_11.get() )
				sliderMax_11 = float( self.w.sliderMax_11.get() )
				sliderPos_11 = float( self.w.sliderButton_11.get() )
				slider[11] = sliderMin_11 * ( 1.0 - sliderPos_11 ) + sliderMax_11 * sliderPos_11

				sliderMin_12 = float( self.w.sliderMin_12.get() )
				sliderMax_12 = float( self.w.sliderMax_12.get() )
				sliderPos_12 = float( self.w.sliderButton_12.get() )
				slider[12] = sliderMin_12 * ( 1.0 - sliderPos_12 ) + sliderMax_12 * sliderPos_12

				sliderMin_13 = float( self.w.sliderMin_13.get() )
				sliderMax_13 = float( self.w.sliderMax_13.get() )
				sliderPos_13 = float( self.w.sliderButton_13.get() )
				slider[13] = sliderMin_13 * ( 1.0 - sliderPos_13 ) + sliderMax_13 * sliderPos_13

				#sliderMin_14 = float( self.w.sliderMin_14.get() )
				#sliderMax_14 = float( self.w.sliderMax_14.get() )
				#sliderPos_14 = float( self.w.sliderButton_14.get() )
				#slider[14] = sliderMin_14 * ( 1.0 - sliderPos_14 ) + sliderMax_14 * sliderPos_14

				sliderMin_15 = float( self.w.sliderMin_15.get() )
				sliderMax_15 = float( self.w.sliderMax_15.get() )
				sliderPos_15 = float( self.w.sliderButton_15.get() )
				slider[15] = sliderMin_15 * ( 1.0 - sliderPos_15 ) + sliderMax_15 * sliderPos_15

				sliderMin_16 = float( self.w.sliderMin_16.get() )
				sliderMax_16 = float( self.w.sliderMax_16.get() )
				sliderPos_16 = float( self.w.sliderButton_16.get() )
				slider[16] = sliderMin_16 * ( 1.0 - sliderPos_16 ) + sliderMax_16 * sliderPos_16

				sliderMin_17 = float( self.w.sliderMin_17.get() )
				sliderMax_17 = float( self.w.sliderMax_17.get() )
				sliderPos_17 = float( self.w.sliderButton_17.get() )
				slider[17] = sliderMin_17 * ( 1.0 - sliderPos_17 ) + sliderMax_17 * sliderPos_17

				sliderMin_18 = float( self.w.sliderMin_18.get() )
				sliderMax_18 = float( self.w.sliderMax_18.get() )
				sliderPos_18 = float( self.w.sliderButton_18.get() )
				slider[18] = sliderMin_18 * ( 1.0 - sliderPos_18 ) + sliderMax_18 * sliderPos_18

				sliderMin_19 = float( self.w.sliderMin_19.get() )
				sliderMax_19 = float( self.w.sliderMax_19.get() )
				sliderPos_19 = float( self.w.sliderButton_19.get() )
				slider[19] = sliderMin_19 * ( 1.0 - sliderPos_19 ) + sliderMax_19 * sliderPos_19



				sliderMin_20 = float( self.w.sliderMin_20.get() )
				sliderMax_20 = float( self.w.sliderMax_20.get() )
				sliderPos_20 = float( self.w.sliderButton_20.get() )
				slider[20] = sliderMin_20 * ( 1.0 - sliderPos_20 ) + sliderMax_20 * sliderPos_20

				sliderMin_4 = float( self.w.sliderMin_4.get() )
				sliderMax_4 = float( self.w.sliderMax_4.get() )
				sliderPos_4 = float( self.w.sliderButton_4.get() )
				slider[4] = sliderMin_4 * ( 1.0 - sliderPos_4 ) + sliderMax_4 * sliderPos_4

				sliderMin_21 = float( self.w.sliderMin_21.get() )
				sliderMax_21 = float( self.w.sliderMax_21.get() )
				sliderPos_21 = float( self.w.sliderButton_21.get() )
				slider[21] = sliderMin_21 * ( 1.0 - sliderPos_21 ) + sliderMax_21 * sliderPos_21

				sliderMin_22 = float( self.w.sliderMin_22.get() )
				sliderMax_22 = float( self.w.sliderMax_22.get() )
				sliderPos_22 = float( self.w.sliderButton_22.get() )
				slider[22] = sliderMin_22 * ( 1.0 - sliderPos_22 ) + sliderMax_22 * sliderPos_22

				sliderMin_31 = float( self.w.sliderMin_31.get() )
				sliderMax_31 = float( self.w.sliderMax_31.get() )
				sliderPos_31 = float( self.w.sliderButton_31.get() )
				slider[31] = sliderMin_31 * ( 1.0 - sliderPos_31 ) + sliderMax_31 * sliderPos_31

				sliderMin_23 = float( self.w.sliderMin_23.get() )
				sliderMax_23 = float( self.w.sliderMax_23.get() )
				sliderPos_23 = float( self.w.sliderButton_23.get() )
				slider[23] = sliderMin_23 * ( 1.0 - sliderPos_23 ) + sliderMax_23 * sliderPos_23

				#sliderMin_24 = float( self.w.sliderMin_24.get() )
				#sliderMax_24 = float( self.w.sliderMax_24.get() )
				#sliderPos_24 = float( self.w.sliderButton_24.get() )
				#slider[24] = sliderMin_24 * ( 1.0 - sliderPos_24 ) + sliderMax_24 * sliderPos_24

				sliderMin_25 = float( self.w.sliderMin_25.get() )
				sliderMax_25 = float( self.w.sliderMax_25.get() )
				sliderPos_25 = float( self.w.sliderButton_25.get() )
				slider[25] = sliderMin_25 * ( 1.0 - sliderPos_25 ) + sliderMax_25 * sliderPos_25

				sliderMin_26 = float( self.w.sliderMin_26.get() )
				sliderMax_26 = float( self.w.sliderMax_26.get() )
				sliderPos_26 = float( self.w.sliderButton_26.get() )
				slider[26] = sliderMin_26 * ( 1.0 - sliderPos_26 ) + sliderMax_26 * sliderPos_26

				sliderMin_27 = float( self.w.sliderMin_27.get() )
				sliderMax_27 = float( self.w.sliderMax_27.get() )
				sliderPos_27 = float( self.w.sliderButton_27.get() )
				slider[27] = sliderMin_27 * ( 1.0 - sliderPos_27 ) + sliderMax_27 * sliderPos_27


				sliderMin_28 = float( self.w.sliderMin_28.get() )
				sliderMax_28 = float( self.w.sliderMax_28.get() )
				sliderPos_28 = float( self.w.sliderButton_28.get() )
				slider[28] = sliderMin_28 * ( 1.0 - sliderPos_28 ) + sliderMax_28 * sliderPos_28

				sliderMin_29 = float( self.w.sliderMin_29.get() )
				sliderMax_29 = float( self.w.sliderMax_29.get() )
				sliderPos_29 = float( self.w.sliderButton_29.get() )
				slider[29] = sliderMin_29 * ( 1.0 - sliderPos_29 ) + sliderMax_29 * sliderPos_29

				sliderMin_30 = float( self.w.sliderMin_30.get() )
				sliderMax_30 = float( self.w.sliderMax_30.get() )
				sliderPos_30 = float( self.w.sliderButton_30.get() )
				slider[30] = sliderMin_30 * ( 1.0 - sliderPos_30 ) + sliderMax_30 * sliderPos_30

				print("aftercalc")
				print(slider[20])
				print(sliderPos_20)
				print(self.w.sliderButton_20.get())





				Font.disableUpdateInterface()

				for thisLayer in selectedLayers:
					thisGlyph = thisLayer.parent
					# print "Processing", thisGlyph.name

					thisGlyph.beginUndo()
						#thisLayer, deleteComponents, componentName, distanceBetweenDots, useBackground,

					process( slider, interpol_array)	#process( sliderPos )
					thisGlyph.endUndo()

				Font.enableUpdateInterface()

				if not self.SavePreferences( self ):
					print "Note: could not write preferences."

			# self.w.close()
		except Exception, e:
			raise e

LivePolation()



# misc
#import sys
#current_module = sys.modules[__name__]
#print(dir(current_module))
#print(dir(Glyphs))



#(
#       {
#        Filter = "GlyphsFilterOffsetCurve; 1; 1; 1; 0.5;";
#    },
#        {
#        Filter = "GlyphsFilterOffsetCurve; -1; -1; 0; 0.5;";
#    },
#        {
#        sampleText = "Hey There";
#    }
#)
