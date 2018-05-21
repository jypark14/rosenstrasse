# Import the pygame library and initialise the game engine


# player name / character name on the game page 
	# go through each cards, which ones need to update risk matrix 
	# both player and character name 
	# complicity card just the player name 
# sound files must be only played if facilitator clikcs on the sound effect 4
	# hacking way : changing the track 
# only show cards that are relevant (if Izak is in prison use this card - just ask the facilitator) 3 
	# pop up first and dont show the card if not
# going to specific cards from the playing screen - in an easy way --- lowest priority 
# readme text 2 --> don't forget to install pygame (link for pygame)
# no hardcoded text -> textfile 1
# update instruction with inputting scores 
# menu return with same card number 
#risk matrix --> characters across the top ; categories down the bottom which specific values like +2, -3... 
	#risk matrix appears 
#instruction for the stage on the screen for orientation score 

import pygame
import time  
import sys
import os 
import random
pygame.init()

background = pygame.transform.scale(pygame.image.load("images/gameimages/back_intro.png"), (1200, 900))
riskMatrix = pygame.transform.scale(pygame.image.load("images/gameimages/report.png"), (30, 30))
backgroundImg = pygame.transform.scale(pygame.image.load("images/mainbg.png"), (1200,900))
instructionImg = pygame.transform.scale(pygame.image.load("images/gameimages/back_instruction.png"), (230,80))
playImg = pygame.transform.scale(pygame.image.load("images/gameimages/back_play.png"), (230,80))
nextImg = pygame.transform.scale(pygame.image.load("images/gameimages/gofront.png"), (30,30))
prevImg = pygame.transform.scale(pygame.image.load("images/gameimages/goback.png"), (50,50))
cardBg = pygame.transform.scale(pygame.image.load("images/cardbackgroundImg.png"), (1200,900))
logoTextImg = pygame.transform.scale(pygame.image.load("images/mainlogo.png"), (400,100))
dir1 = pygame.transform.scale(pygame.image.load("images/dir/1.png"), (330,550))
dir2 = pygame.transform.scale(pygame.image.load("images/dir/2.png"), (330,550))
dir3 = pygame.transform.scale(pygame.image.load("images/dir/3.png"), (330,550))
dir4 = pygame.transform.scale(pygame.image.load("images/dir/4.png"), (330,550))
dir5 = pygame.transform.scale(pygame.image.load("images/dir/5.png"), (330,550))
dir6 = pygame.transform.scale(pygame.image.load("images/dir/6.png"), (330,550))
dir7 = pygame.transform.scale(pygame.image.load("images/dir/7a.png"), (330,550))
dir8 = pygame.transform.scale(pygame.image.load("images/dir/8.png"), (330,550))
dir9 = pygame.transform.scale(pygame.image.load("images/dir/9.png"), (330,550))
dir10 = pygame.transform.scale(pygame.image.load("images/dir/10.png"), (330,550))
dir11 = pygame.transform.scale(pygame.image.load("images/dir/11.png"), (330,550))
dir12 = pygame.transform.scale(pygame.image.load("images/dir/12.png"), (330,550))
dir13 = pygame.transform.scale(pygame.image.load("images/dir/13a.png"), (330,550))
dir14 = pygame.transform.scale(pygame.image.load("images/dir/14.png"), (330,550))
dir15 = pygame.transform.scale(pygame.image.load("images/dir/15.png"), (330,550))
dir16 = pygame.transform.scale(pygame.image.load("images/dir/16.png"), (330,550))
dir17 = pygame.transform.scale(pygame.image.load("images/dir/17.png"), (330,550))
dir18 = pygame.transform.scale(pygame.image.load("images/dir/18.png"), (330,550))
dir19 = pygame.transform.scale(pygame.image.load("images/dir/19.png"), (330,550))
dir20 = pygame.transform.scale(pygame.image.load("images/dir/20.png"), (330,550))
dir21 = pygame.transform.scale(pygame.image.load("images/dir/21.png"), (330,550))
dir22 = pygame.transform.scale(pygame.image.load("images/dir/22.png"), (330,550))
dir23 = pygame.transform.scale(pygame.image.load("images/dir/23.png"), (330,550))
dir24 = pygame.transform.scale(pygame.image.load("images/dir/24.png"), (330,550))
dir25 = pygame.transform.scale(pygame.image.load("images/dir/25.png"), (330,550))
dir26 = pygame.transform.scale(pygame.image.load("images/dir/26.png"), (330,550))
dir27 = pygame.transform.scale(pygame.image.load("images/dir/27a.png"), (330,550))
dir28 = pygame.transform.scale(pygame.image.load("images/dir/28a.png"), (330,550))
dir29 = pygame.transform.scale(pygame.image.load("images/dir/29.png"), (330,550))
dir30 = pygame.transform.scale(pygame.image.load("images/dir/30.png"), (330,550))
dir31 = pygame.transform.scale(pygame.image.load("images/dir/31.png"), (330,550))
dir32 = pygame.transform.scale(pygame.image.load("images/dir/32.png"), (330,550))
dir33 = pygame.transform.scale(pygame.image.load("images/dir/33.png"), (330,550))
dir34 = pygame.transform.scale(pygame.image.load("images/dir/34.png"), (330,550))


dirArray = [0, dir1, dir2, dir3, dir4, dir5, dir6, dir7, dir8, dir9, dir10, dir11, dir12, dir13, 
dir14, dir15, dir16, dir17, dir18, dir19, dir20, dir21, dir22, dir23, dir24, dir25, dir26, dir27, dir28, 
dir29, dir30, dir31, dir32]

#cardImages rightside 
cardImg1 = pygame.transform.scale(pygame.image.load("images/cards/r1.png"), (330,550))
cardImg2 = pygame.transform.scale(pygame.image.load("images/cards/r2.png"), (330,550))
cardImg3 = pygame.transform.scale(pygame.image.load("images/cards/r3.png"), (330,550))
cardImg4 = pygame.transform.scale(pygame.image.load("images/cards/r4.png"), (330,550))
cardImg5 = pygame.transform.scale(pygame.image.load("images/cards/r5.png"), (330,550))
cardImg6 = pygame.transform.scale(pygame.image.load("images/cards/r6.png"), (330,550))
cardImg7 = pygame.transform.scale(pygame.image.load("images/cards/r7.png"), (330,550))
cardImg8 = pygame.transform.scale(pygame.image.load("images/cards/r8.png"), (330,550))
cardImg9 = pygame.transform.scale(pygame.image.load("images/cards/r9.png"), (330,550))
cardImg10 = pygame.transform.scale(pygame.image.load("images/cards/r10.png"), (330,550))
cardImg11 = pygame.transform.scale(pygame.image.load("images/cards/r11.png"), (330,550))
cardImg12 = pygame.transform.scale(pygame.image.load("images/cards/r12.png"), (330,550))
cardImg13 = pygame.transform.scale(pygame.image.load("images/cards/r13.png"), (330,550))
cardImg14 = pygame.transform.scale(pygame.image.load("images/cards/r14.png"), (330,550))
cardImg15 = pygame.transform.scale(pygame.image.load("images/cards/r15.png"), (330,550))
cardImg16 = pygame.transform.scale(pygame.image.load("images/cards/r16.png"), (330,550))
cardImg17 = pygame.transform.scale(pygame.image.load("images/cards/r17.png"), (330,550))
cardImg18 = pygame.transform.scale(pygame.image.load("images/cards/r18.png"), (330,550))
cardImg19 = pygame.transform.scale(pygame.image.load("images/cards/r19.png"), (330,550))
cardImg20 = pygame.transform.scale(pygame.image.load("images/cards/r20.png"), (330,550))
cardImg21 = pygame.transform.scale(pygame.image.load("images/cards/r21.png"), (330,550))
cardImg22 = pygame.transform.scale(pygame.image.load("images/cards/r22.png"), (330,550))
cardImg23 = pygame.transform.scale(pygame.image.load("images/cards/r23.png"), (330,550))
cardImg24 = pygame.transform.scale(pygame.image.load("images/cards/r24.png"), (330,550))
cardImg25 = pygame.transform.scale(pygame.image.load("images/cards/r25.png"), (330,550))
cardImg26 = pygame.transform.scale(pygame.image.load("images/cards/r26.png"), (330,550))
cardImg27 = pygame.transform.scale(pygame.image.load("images/cards/r27.png"), (330,550))
cardImg28 = pygame.transform.scale(pygame.image.load("images/cards/r28.png"), (330,550))
cardImg29 = pygame.transform.scale(pygame.image.load("images/cards/r29.png"), (330,550))
cardImg30 = pygame.transform.scale(pygame.image.load("images/cards/r30.png"), (330,550))
cardImg31 = pygame.transform.scale(pygame.image.load("images/cards/r31.png"), (330,550))
cardImg32 = pygame.transform.scale(pygame.image.load("images/cards/r32.png"), (330,550))
cardImg33 = pygame.transform.scale(pygame.image.load("images/cards/r33.png"), (330,550))
cardImg34 = pygame.transform.scale(pygame.image.load("images/cards/r34.png"), (330,550))
cardImg35 = pygame.transform.scale(pygame.image.load("images/cards/r35.png"), (330,550))
cardImg36 = pygame.transform.scale(pygame.image.load("images/cards/r36.png"), (330,550))
cardImg37 = pygame.transform.scale(pygame.image.load("images/cards/r37.png"), (330,550))
cardImg38 = pygame.transform.scale(pygame.image.load("images/cards/r38.png"), (330,550))
cardImg39 = pygame.transform.scale(pygame.image.load("images/cards/r39.png"), (330,550))
cardImg40 = pygame.transform.scale(pygame.image.load("images/cards/r40.png"), (330,550))
cardImg41 = pygame.transform.scale(pygame.image.load("images/cards/r41.png"), (330,550))
cardImg42 = pygame.transform.scale(pygame.image.load("images/cards/r42.png"), (330,550))
cardImg43 = pygame.transform.scale(pygame.image.load("images/cards/r43.png"), (330,550))
cardImg44 = pygame.transform.scale(pygame.image.load("images/cards/r44.png"), (330,550))
cardImg45 = pygame.transform.scale(pygame.image.load("images/cards/r45.png"), (330,550))
cardImg46 = pygame.transform.scale(pygame.image.load("images/cards/r46.png"), (330,550))
cardImg47 = pygame.transform.scale(pygame.image.load("images/cards/r47.png"), (330,550))
cardImg48 = pygame.transform.scale(pygame.image.load("images/cards/r48.png"), (330,550))
cardImg49 = pygame.transform.scale(pygame.image.load("images/cards/r49.png"), (330,550))
cardImg50 = pygame.transform.scale(pygame.image.load("images/cards/r50.png"), (330,550))
cardImg51 = pygame.transform.scale(pygame.image.load("images/cards/r51.png"), (330,550))
cardImg52 = pygame.transform.scale(pygame.image.load("images/cards/r52.png"), (330,550))
cardImg53 = pygame.transform.scale(pygame.image.load("images/cards/r53.png"), (330,550))
cardImg54 = pygame.transform.scale(pygame.image.load("images/cards/r54.png"), (330,550))
cardImg55 = pygame.transform.scale(pygame.image.load("images/cards/r55.png"), (330,550))
cardImg56 = pygame.transform.scale(pygame.image.load("images/cards/r56.png"), (330,550))
cardImg57 = pygame.transform.scale(pygame.image.load("images/cards/r57.png"), (330,550))
cardImg58 = pygame.transform.scale(pygame.image.load("images/cards/r58.png"), (330,550))
cardImg59 = pygame.transform.scale(pygame.image.load("images/cards/r59.png"), (330,550))
cardImg60 = pygame.transform.scale(pygame.image.load("images/cards/r60.png"), (330,550))
cardImg61 = pygame.transform.scale(pygame.image.load("images/cards/r61.png"), (330,550))
cardImg62 = pygame.transform.scale(pygame.image.load("images/cards/r62.png"), (330,550))
cardImg63 = pygame.transform.scale(pygame.image.load("images/cards/r63.png"), (330,550))
cardImg64 = pygame.transform.scale(pygame.image.load("images/cards/r64.png"), (330,550))
cardImg65 = pygame.transform.scale(pygame.image.load("images/cards/r65.png"), (330,550))
cardImg66 = pygame.transform.scale(pygame.image.load("images/cards/r66.png"), (330,550))
cardImg67 = pygame.transform.scale(pygame.image.load("images/cards/r67.png"), (330,550))
cardImg68 = pygame.transform.scale(pygame.image.load("images/cards/r68.png"), (330,550))
cardImg69 = pygame.transform.scale(pygame.image.load("images/cards/r69.png"), (330,550))
cardImg70 = pygame.transform.scale(pygame.image.load("images/cards/r70.png"), (330,550))
cardImg71 = pygame.transform.scale(pygame.image.load("images/cards/r71.png"), (330,550))
cardImg72 = pygame.transform.scale(pygame.image.load("images/cards/r72.png"), (330,550))
cardImg73 = pygame.transform.scale(pygame.image.load("images/cards/r73.png"), (330,550))
cardImg74 = pygame.transform.scale(pygame.image.load("images/cards/r74.png"), (330,550))
cardImg75 = pygame.transform.scale(pygame.image.load("images/cards/r75.png"), (330,550))
cardImg76 = pygame.transform.scale(pygame.image.load("images/cards/r76.png"), (330,550))
cardImg77 = pygame.transform.scale(pygame.image.load("images/cards/r77.png"), (330,550))
cardImg78 = pygame.transform.scale(pygame.image.load("images/cards/r78.png"), (330,550))
cardImg79 = pygame.transform.scale(pygame.image.load("images/cards/r79.png"), (330,550))
cardImg80 = pygame.transform.scale(pygame.image.load("images/cards/r80.png"), (330,550))
cardImg81 = pygame.transform.scale(pygame.image.load("images/cards/r81.png"), (330,550))
cardImg82 = pygame.transform.scale(pygame.image.load("images/cards/r82.png"), (330,550))
cardImg83 = pygame.transform.scale(pygame.image.load("images/cards/r83.png"), (330,550))
cardImg84 = pygame.transform.scale(pygame.image.load("images/cards/r84.png"), (330,550))
cardImg85 = pygame.transform.scale(pygame.image.load("images/cards/r85.png"), (330,550))
cardImg86 = pygame.transform.scale(pygame.image.load("images/cards/r86.png"), (330,550))
cardImg87 = pygame.transform.scale(pygame.image.load("images/cards/r87.png"), (330,550))
cardImg88 = pygame.transform.scale(pygame.image.load("images/cards/r88.png"), (330,550))
cardImg89 = pygame.transform.scale(pygame.image.load("images/cards/r89.png"), (330,550))
cardImg90 = pygame.transform.scale(pygame.image.load("images/cards/r90.png"), (330,550))

#cardImages leftside
lcardImg1 = pygame.transform.scale(pygame.image.load("images/cards/l1.png"), (211,352))
lcardImg2 = pygame.transform.scale(pygame.image.load("images/cards/l2.png"), (211,352))
lcardImg3 = pygame.transform.scale(pygame.image.load("images/cards/l3.png"), (211,352))
lcardImg4 = pygame.transform.scale(pygame.image.load("images/cards/l4.png"), (211,352))
lcardImg5 = pygame.transform.scale(pygame.image.load("images/cards/l5.png"), (211,352))
lcardImg6 = pygame.transform.scale(pygame.image.load("images/cards/l6.png"), (211,352))
lcardImg7 = pygame.transform.scale(pygame.image.load("images/cards/l7.png"), (211,352))
lcardImg8 = pygame.transform.scale(pygame.image.load("images/cards/l8.png"), (211,352))
lcardImg9 = pygame.transform.scale(pygame.image.load("images/cards/l9.png"), (211,352))
lcardImg10 = pygame.transform.scale(pygame.image.load("images/cards/l10.png"), (211,352))
lcardImg11 = pygame.transform.scale(pygame.image.load("images/cards/l11.png"), (211,352))
lcardImg12 = pygame.transform.scale(pygame.image.load("images/cards/l12.png"), (211,352))
lcardImg13 = pygame.transform.scale(pygame.image.load("images/cards/l13.png"), (211,352))
lcardImg14 = pygame.transform.scale(pygame.image.load("images/cards/l14.png"), (211,352))
lcardImg15 = pygame.transform.scale(pygame.image.load("images/cards/l15.png"), (211,352))
lcardImg16 = pygame.transform.scale(pygame.image.load("images/cards/l16.png"), (211,352))
lcardImg17 = pygame.transform.scale(pygame.image.load("images/cards/l17.png"), (211,352))
lcardImg18 = pygame.transform.scale(pygame.image.load("images/cards/l18.png"), (211,352))
lcardImg19 = pygame.transform.scale(pygame.image.load("images/cards/l19.png"), (211,352))
lcardImg20 = pygame.transform.scale(pygame.image.load("images/cards/l20.png"), (211,352))
lcardImg21 = pygame.transform.scale(pygame.image.load("images/cards/l21.png"), (211,352))
lcardImg22 = pygame.transform.scale(pygame.image.load("images/cards/l22.png"), (211,352))
lcardImg23 = pygame.transform.scale(pygame.image.load("images/cards/l23.png"), (211,352))
lcardImg24 = pygame.transform.scale(pygame.image.load("images/cards/l24.png"), (211,352))
lcardImg25 = pygame.transform.scale(pygame.image.load("images/cards/l25.png"), (211,352))
lcardImg26 = pygame.transform.scale(pygame.image.load("images/cards/l26.png"), (211,352))
lcardImg27 = pygame.transform.scale(pygame.image.load("images/cards/l27.png"), (211,352))
lcardImg28 = pygame.transform.scale(pygame.image.load("images/cards/l28.png"), (211,352))
lcardImg29 = pygame.transform.scale(pygame.image.load("images/cards/l29.png"), (211,352))
lcardImg30 = pygame.transform.scale(pygame.image.load("images/cards/l30.png"), (211,352))
lcardImg31 = pygame.transform.scale(pygame.image.load("images/cards/l31.png"), (211,352))
lcardImg32 = pygame.transform.scale(pygame.image.load("images/cards/l32.png"), (211,352))
lcardImg33 = pygame.transform.scale(pygame.image.load("images/cards/l33.png"), (211,352))
lcardImg34 = pygame.transform.scale(pygame.image.load("images/cards/l34.png"), (211,352))
lcardImg35 = pygame.transform.scale(pygame.image.load("images/cards/l35.png"), (211,352))
lcardImg36 = pygame.transform.scale(pygame.image.load("images/cards/l36.png"), (211,352))
lcardImg37 = pygame.transform.scale(pygame.image.load("images/cards/l37.png"), (211,352))
lcardImg38 = pygame.transform.scale(pygame.image.load("images/cards/l38.png"), (211,352))
lcardImg39 = pygame.transform.scale(pygame.image.load("images/cards/l39.png"), (211,352))
lcardImg40 = pygame.transform.scale(pygame.image.load("images/cards/l40.png"), (211,352))
lcardImg41 = pygame.transform.scale(pygame.image.load("images/cards/l41.png"), (211,352))
lcardImg42 = pygame.transform.scale(pygame.image.load("images/cards/l42.png"), (211,352))
lcardImg43 = pygame.transform.scale(pygame.image.load("images/cards/l43.png"), (211,352))
lcardImg44 = pygame.transform.scale(pygame.image.load("images/cards/l44.png"), (211,352))
lcardImg45 = pygame.transform.scale(pygame.image.load("images/cards/l45.png"), (211,352))
lcardImg46 = pygame.transform.scale(pygame.image.load("images/cards/l46.png"), (211,352))
lcardImg47 = pygame.transform.scale(pygame.image.load("images/cards/l47.png"), (211,352))
lcardImg48 = pygame.transform.scale(pygame.image.load("images/cards/l48.png"), (211,352))
lcardImg49 = pygame.transform.scale(pygame.image.load("images/cards/l49.png"), (211,352))
lcardImg50 = pygame.transform.scale(pygame.image.load("images/cards/l50.png"), (211,352))
lcardImg51 = pygame.transform.scale(pygame.image.load("images/cards/l51.png"), (211,352))
lcardImg52 = pygame.transform.scale(pygame.image.load("images/cards/l52.png"), (211,352))
lcardImg53 = pygame.transform.scale(pygame.image.load("images/cards/l53.png"), (211,352))
lcardImg54 = pygame.transform.scale(pygame.image.load("images/cards/l54.png"), (211,352))
lcardImg55 = pygame.transform.scale(pygame.image.load("images/cards/l55.png"), (211,352))
lcardImg56 = pygame.transform.scale(pygame.image.load("images/cards/l56.png"), (211,352))
lcardImg57 = pygame.transform.scale(pygame.image.load("images/cards/l57.png"), (211,352))
lcardImg58 = pygame.transform.scale(pygame.image.load("images/cards/l58.png"), (211,352))
lcardImg59 = pygame.transform.scale(pygame.image.load("images/cards/l59.png"), (211,352))
lcardImg60 = pygame.transform.scale(pygame.image.load("images/cards/l60.png"), (211,352))
lcardImg61 = pygame.transform.scale(pygame.image.load("images/cards/l61.png"), (211,352))
lcardImg62 = pygame.transform.scale(pygame.image.load("images/cards/l62.png"), (211,352))
lcardImg63 = pygame.transform.scale(pygame.image.load("images/cards/l63.png"), (211,352))
lcardImg64 = pygame.transform.scale(pygame.image.load("images/cards/l64.png"), (211,352))
lcardImg65 = pygame.transform.scale(pygame.image.load("images/cards/l65.png"), (211,352))
lcardImg66 = pygame.transform.scale(pygame.image.load("images/cards/l66.png"), (211,352))
lcardImg67 = pygame.transform.scale(pygame.image.load("images/cards/l67.png"), (211,352))
lcardImg68 = pygame.transform.scale(pygame.image.load("images/cards/l68.png"), (211,352))
lcardImg69 = pygame.transform.scale(pygame.image.load("images/cards/l69.png"), (211,352))
lcardImg70 = pygame.transform.scale(pygame.image.load("images/cards/l70.png"), (211,352))
lcardImg71 = pygame.transform.scale(pygame.image.load("images/cards/l71.png"), (211,352))
lcardImg72 = pygame.transform.scale(pygame.image.load("images/cards/l72.png"), (211,352))
lcardImg73 = pygame.transform.scale(pygame.image.load("images/cards/l73.png"), (211,352))
lcardImg74 = pygame.transform.scale(pygame.image.load("images/cards/l74.png"), (211,352))
lcardImg75 = pygame.transform.scale(pygame.image.load("images/cards/l75.png"), (211,352))
lcardImg76 = pygame.transform.scale(pygame.image.load("images/cards/l76.png"), (211,352))
lcardImg77 = pygame.transform.scale(pygame.image.load("images/cards/l77.png"), (211,352))
lcardImg78 = pygame.transform.scale(pygame.image.load("images/cards/l78.png"), (211,352))
lcardImg79 = pygame.transform.scale(pygame.image.load("images/cards/l79.png"), (211,352))
lcardImg80 = pygame.transform.scale(pygame.image.load("images/cards/l80.png"), (211,352))
lcardImg81 = pygame.transform.scale(pygame.image.load("images/cards/l81.png"), (211,352))
lcardImg82 = pygame.transform.scale(pygame.image.load("images/cards/l82.png"), (211,352))
lcardImg83 = pygame.transform.scale(pygame.image.load("images/cards/l83.png"), (211,352))
lcardImg84 = pygame.transform.scale(pygame.image.load("images/cards/l84.png"), (211,352))
lcardImg85 = pygame.transform.scale(pygame.image.load("images/cards/l85.png"), (211,352))
lcardImg86 = pygame.transform.scale(pygame.image.load("images/cards/l86.png"), (211,352))
lcardImg87 = pygame.transform.scale(pygame.image.load("images/cards/l87.png"), (211,352))
lcardImg88 = pygame.transform.scale(pygame.image.load("images/cards/l88.png"), (211,352))
lcardImg89 = pygame.transform.scale(pygame.image.load("images/cards/l89.png"), (211,352))
lcardImg90 = pygame.transform.scale(pygame.image.load("images/cards/l90.png"), (211,352))

#cardimageArray rightside 
cardRArray = [0, cardImg1, cardImg2, cardImg3, cardImg4, cardImg5, cardImg6, cardImg7, cardImg8, cardImg9, cardImg10, 
cardImg11, cardImg12, cardImg13, cardImg14, cardImg15, cardImg16, cardImg17, cardImg18, cardImg19, cardImg20,
cardImg21, cardImg22, cardImg23, cardImg24, cardImg25, cardImg26, cardImg27, cardImg28, cardImg29, cardImg30,
cardImg31, cardImg32, cardImg33, cardImg34, cardImg35, cardImg36, cardImg37, cardImg38, cardImg39, cardImg40,
cardImg41, cardImg42, cardImg43, cardImg44, cardImg45, cardImg46, cardImg47, cardImg48, cardImg49, cardImg50,
cardImg51, cardImg52, cardImg53, cardImg54, cardImg55, cardImg56, cardImg57, cardImg58, cardImg59, cardImg60,
cardImg61, cardImg62, cardImg63, cardImg64, cardImg65, cardImg66, cardImg67, cardImg68, cardImg69, cardImg70,
cardImg71, cardImg72, cardImg73, cardImg74, cardImg75, cardImg76, cardImg77, cardImg78, cardImg79, cardImg80,
cardImg81, cardImg82, cardImg83, cardImg84, cardImg85, cardImg86, cardImg87, cardImg88, cardImg89, cardImg90]

cardLArray = [0, lcardImg1, lcardImg2, lcardImg3, lcardImg4, lcardImg5, lcardImg6, lcardImg7, lcardImg8, lcardImg9, lcardImg10, 
lcardImg11, lcardImg12, lcardImg13, lcardImg14, lcardImg15, lcardImg16, lcardImg17, lcardImg18, lcardImg19, lcardImg20,
lcardImg21, lcardImg22, lcardImg23, lcardImg24, lcardImg25, lcardImg26, lcardImg27, lcardImg28, lcardImg29, lcardImg30,
lcardImg31, lcardImg32, lcardImg33, lcardImg34, lcardImg35, lcardImg36, lcardImg37, lcardImg38, lcardImg39, lcardImg40,
lcardImg41, lcardImg42, lcardImg43, lcardImg44, lcardImg45, lcardImg46, lcardImg47, lcardImg48, lcardImg49, lcardImg50,
lcardImg51, lcardImg52, lcardImg53, lcardImg54, lcardImg55, lcardImg56, lcardImg57, lcardImg58, lcardImg59, lcardImg60,
lcardImg61, lcardImg62, lcardImg63, lcardImg64, lcardImg65, lcardImg66, lcardImg67, lcardImg68, lcardImg69, lcardImg70,
lcardImg71, lcardImg72, lcardImg73, lcardImg74, lcardImg75, lcardImg76, lcardImg77, lcardImg78, lcardImg79, lcardImg80,
lcardImg81, lcardImg82, lcardImg83, lcardImg84, lcardImg85, lcardImg86, lcardImg87, lcardImg88, lcardImg89, lcardImg90]


#Direction for keys 
DIRECTION_RIGHT = "right"
DIRECTION_LEFT = "left"
DIRECTION_UP = "up"
DIRECTION_DOWN = "down"

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

# Open a new window
size = (1200, 800)
screen = pygame.display.set_mode(size)
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

class InputBox:
    #initalize variables
    def __init__(self, x, y, w, h, name, text='0'):
        self.sum = 0
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.name = name

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            #adds  new risk if clicked upon when facilitator presses enter
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.sum = self.sum + int(self.text)
                    print(self.sum)
                    self.text = str(self.sum)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        screen.blit(FONT.render(self.name, True, self.color), (self.rect.x-70, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Menu(object): 
    def __init__(self):  
        self.instructionBox = pygame.Rect(185, 640, 230, 80)  
        self.playBox = pygame.Rect(785, 640, 230, 80)    
        self.matrixBox = pygame.Rect(1050,700, 30, 30) #not detecting 
        self.menuBox = pygame.Rect(1100,40, 50, 50)
        homeScreen = True 

    def riskMatrix(self):
	    clock = pygame.time.Clock()
	    screen.blit
	    #creates risk matrixes for each character
	    input_box1 = InputBox(500, 100, 140, 32, "Kurt")
	    input_box2 = InputBox(500, 200, 140, 32, "Josef")
	    input_box3 = InputBox(500, 300, 140, 32, "Max")
	    input_box4 = InputBox(500, 400, 140, 32, "Izak")
	    input_boxes = [input_box1, input_box2, input_box3, input_box4]
	    done = False

	    while not done:
	        for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	                done = True
	            for box in input_boxes:
	                box.handle_event(event)

	        for box in input_boxes:
	            box.update()

	        screen.fill((30, 30, 30))
	        for box in input_boxes:
	            box.draw(screen)

	        pygame.display.flip()
	        clock.tick(30)

    def playGame(self): 
        # screen.fill(WHITE)
        mouseposition = pygame.mouse.get_pos()  
        mousepressed = pygame.mouse.get_pressed()
        
        screen.blit(cardBg, (0,0))
        screen.blit(riskMatrix, (1050,700))
        screen.blit(prevImg, (1100,40))
        # screen.draw.rect 

        cardIndex = 0 
        events = pygame.event.get()  # this will return a que of events
        running = True 
        while running:  
            if self.menuBox.collidepoint(mouseposition) and mousepressed[0] == 1:
                print 'Menu'
            if self.matrixBox.collidepoint(mouseposition) and mousepressed[0] == 1:
                print 'g'

            events = pygame.event.get()  
            for event in events: 
                if event.type == pygame.QUIT: 
                    sys.exit(0) 

                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_LEFT and cardIndex > 1: 
                        cardIndex -= 1 
                        screen.blit(cardLArray[cardIndex], (100,100))  
                        screen.blit(cardRArray[cardIndex], (435,100))   
                        screen.blit(dirArray[cardIndex], (835,100))
                    if event.key == pygame.K_RIGHT and cardIndex < 90: 
                        cardIndex += 1 
                        screen.blit(cardLArray[cardIndex], (100,100))  
                        screen.blit(cardRArray[cardIndex], (435,100)) 
                        screen.blit(dirArray[cardIndex], (835,100))
                    if event.key == pygame.K_r: 
                        self.riskMatrix()
                    if event.key == pygame.K_m: 
                        self.menu()
  
            pygame.display.update()

    def playInstructions(self):
        info_array = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
        instruction_index = 0
        events = pygame.event.get() 
        running = True
        screen.blit(backgroundImg, (0,0))
        screen.blit(logoTextImg, (400,10))
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and instruction_index <= len(info_array):
                        instruction_index += 1
                    if event.key == pygame.K_LEFT and instruction_index > 1:
                        instruction_index -= 1
                    num = info_array[instruction_index]
                    if num == 1:
                        self.personal_context()
                        pygame.display.update()
                    if num == 2:
                        self.lineups_casting1()
                        pygame.display.update()
                    if num == 3:
                        self.character_assign()
                        pygame.display.update()

                    #   self.lineups_casting2()
                    #   pygame.display.update()
                    if num == 4:
                        self.lineups_casting3()
                        pygame.display.update()
                    if num == 5:
                        self.lineups_casting4()
                        pygame.display.update()
                    if num == 6:
                        self.lineups_casting5()
                        pygame.display.update()
                    if num == 7:
                        self.lineups_casting6()
                        pygame.display.update()
                    if num == 8:
                        self.lineups_casting7()
                        pygame.display.update()
                    if num == 9:    
                        self.lineups_casting8()
                        pygame.display.update()
                    if num == 10:
                        self.lineups_casting9()
                        pygame.display.update()
                    if num == 11:
                        self.lineups_casting10()
                        pygame.display.update()
                    if num == 12:
                        self.lineups_casting11()
                        pygame.display.update()
                    if num == 13:
                        self.lineups_casting12()
                        pygame.display.update()
                    if event.key == pygame.K_m: #apply for instruction as well 
                        self.menu()
	
	#instrution_sets    
    def lineups_casting1(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #gobackrectangle = pygame.Rect(40, 40, 80, 80)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        script = "Workshop:LineUps and Casting(20 mins)Let the players know that in the game they will have two" 
        script1 = "characters to play. One character will be male, and one will be female. Each character will be"
        script3 = " character. To determine who should play which character, you will be running a short series of line-ups."
        script4 = "Have all players stand side by side in a straight line. Tell them you will be asking them a few questions," 
        script5 = "and will designate what each end of the line means. Then they will need to find the place on that line"
        script6 = "where they as a player fit. Ensure everyone understands how this works by doing a quick test run - you" 
        script7 = "will ask them to line according to their age. Point to the left side of the room and tell them that that "
        script8 = "end of the line is older. Point to the right side and tell them that that side of the line is younger. Let"
        script9 = " them self-arrange into a line-up. At any time, if players all clump up in one spot, make them straighten"
        script10 = "the line. Once you are sure that everyone understands what they need to do, proceed to call for the lineups on the next page."
        # script11 = "talking about aligns with the goal of this work- shop, it is appropriate. If a player diverges"
        # script12 = "from these topics, gently bring them back to focus on the game."
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script1
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        #self.instructiontext = script2
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script3
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script4
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script5
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script6
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script7
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script8
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script9
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script10
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)


    def character_assign(self):
        pygame.draw.rect(screen, (0,0,0), (0,0,1200,700))
        self.player1text = "Player 1: "
        self.player2text = "Player 2: "
        self.player3text = "Player 3: "
        self.player4text = "Player 4: "
        self.playerfontcolor = (255,255,255)
        self.playerfont = pygame.font.SysFont('comicsansms',20)
        self.player1ren = self.playerfont.render(self.player1text,30,self.playerfontcolor)
        self.player2ren = self.playerfont.render(self.player2text,30,self.playerfontcolor)
        self.player3ren = self.playerfont.render(self.player3text,30,self.playerfontcolor)
        self.player4ren = self.playerfont.render(self.player4text,30,self.playerfontcolor)
        screen.blit(self.player1ren,(180,130))
        screen.blit(self.player2ren,(180,230))
        screen.blit(self.player3ren,(180,330))
        screen.blit(self.player4ren,(180,430))


    def lineups_casting2(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))   
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #gobackrectangle = pygame.Rect(40, 40, 80, 80)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)

        script = "1. This lineup is about how comfortable you are playing a character whose storyline involves the"
        script1 = "serious illness of a child. Going this way (point left) means that you strongly would not want to"
        script2 = "play that kind of story. Going that way (point right) means that you think it would be interesting"
        script3 = " to play that kind of story. Position yourself on the line where you are comfortable. Write down the" 
        script4 = "order. (Note: if for some reason all players indicate that they strongly would not want to play"
        script5 = "in that story, identify for them that this subject matter is limited to a short portion of the scenario"
        script6 = ", and ask them to repeat the line-up with the directions more comfortable, less comfortable.)" 
        script7 = "                                                                                                "
        script8 = "2. This next lineup is about how comfortable you are playing a character that you as a player may"
        script9 = "consider morally challenging. Going this way (point left) means that you strongly would not want to"
        script10 = "play that kind of character. Going that way (point right) means that you think it would be interesting to"
        script11 = "play that kind of character. Position yourself on the line where you are comfortable. Write down the order."
        # script11 = "talking about aligns with the goal of this work- shop, it is appropriate. If a player diverges"
        # script12 = "from these topics, gently bring them back to focus on the game."
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script1
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script2
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script3
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script4
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script5
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script6
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script7
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script8
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script9
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script10
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script11
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()

    def lineups_casting3(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        
        #pygame.draw.rect(screen, (245,245,220), self.scorebox)
        #screen.blit(backmenuImg, (0,0))    
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #gobackrectangle = pygame.Rect(40, 40, 80, 80)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #self.instructiontext = "Instructions"
        #self.instructionren = self.instructionfont.render(self.instructiontext,50,self.instructionfontcolor)
        #screen.blit(self.instructionren,(350,0))
        #self.instructionfontcolor = (0,255,127)
        #self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #self.instructiontext = "Instructions"
        #self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        #screen.blit(self.instructionren,(350,0))
        script = "3. The next question is about the kinds of characters you like to play. Would you prefer to play a"
        script1 = " character who responds to the world more intellectually (point left) or more emotionally (point right)."
        script2 = " Write down the order."
        script3 = "                                                                                                 "
        script4 = "4. And lastly, would you prefer to play a character that is highly vulnerable (point left) or less"
        script5 = " vulnerable (point right)? Write down the order."
        script6 = "                                                                                                 "
        script7 = "Now assign characters according to this process:"
        script8 = "1. Assign both Izak and Anneliese to a player who is not adverse to playing a story with risk to children,"
        script9 = " and who would prefer to play a more vulnerable character."
        script10 = "2. Assign both Kurt and Klara to the remaining player who is most comfortable with playing a character"
        script11 = " with difficult moral perspectives."
        script11 = "3. Assign both Josef and Inge to the remaining player who more strongly prefers to play characters that"
        script12 = " approach the world intellectually."
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script1
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script2
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script3
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script4
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script5
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script6
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script7
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script8
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script9
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script10
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script11
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script12
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()

    def lineups_casting4(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        
        #pygame.draw.rect(screen, (245,245,220), self.scorebox)
        #screen.blit(backmenuImg, (0,0))    
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #gobackrectangle = pygame.Rect(40, 40, 80, 80)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #self.instructiontext = "Instructions"
        #self.instructionren = self.instructionfont.render(self.instructiontext,50,self.instructionfontcolor)
        #screen.blit(self.instructionren,(350,0))
        #self.instructionfontcolor = (0,255,127)
        #self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #self.instructiontext = "Instructions"
        #self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        #screen.blit(self.instructionren,(350,0))
        script = "4. Assign both Max and Ruth to the final player."
        script1 = "Note: if for some reason the options available to you do not allow you to follow the process above,"
        script2 = "use your best judgement based on your observations of the group, but be sure to assign them according"
        script3 = "to the character pairs identified above."                                                                                                 
        script4 = "Note that all character genders are fixed, and must be played as the gender written."
        script5 = "Workshop: Principles of the Game (10 minutes)"
        script6 = "Before beginning play, review the principles of the game with players. Read each principle and its explanatory"
        script7 = "text aloud, then ask the group if they have questions. These principles should guide both the players and"
        script8 = "your own behavior as a Director."
        script10 = "authentic. You do not need to have extensive knowledge of the history in order to play. If you do have such"
        script11 = "knowledge, put it to one side and focus on the daily experiences of your characters."
        script11 = "- No superheroics. The characters in this game are ordinary people living under a totalitarian, oppressive"
        script12 = " regime. Even mild resistance can have deadly consequences. Characters can control the way they respond to"
        script13 =  "the situation they are living in, but do not have the power to change it."
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script1
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script2
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script3
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script4
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script5
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script6
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script7
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script8
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script9
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script10
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script11
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script12
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script13
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,520))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)

    def lineups_casting5(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        
        #pygame.draw.rect(screen, (245,245,220), self.scorebox)
        #screen.blit(backmenuImg, (0,0))    
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #gobackrectangle = pygame.Rect(40, 40, 80, 80)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        script = "- Player transparency, Director secrecy. Players, you can share anything in your game materials either"
        script1 = "in or out of character. Be aware that the Director will be secretly tracking some of the actions you"
        script2 = "take during the game, just as the Nazi regime spied on its citizens."
        script3 = "- We are more important than the game. The game material may be highly personal and painful for some"
        script5 = "not shy away from difficult material, be respectful of the human beings in this room as you engage with it."
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script1
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script2
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script3
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script4
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script5
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()
        # if gobackrectangle.collidepoint(mouseposition) and mousepressed[0] == 1: 
        #   self.instructionpage = False

    def lineups_casting6(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        
        #pygame.draw.rect(screen, (245,245,220), self.scorebox)
        #screen.blit(backmenuImg, (0,0))    
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #gobackrectangle = pygame.Rect(40, 40, 80, 80)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #self.instructiontext = "Instructions"
        #self.instructionren = self.instructionfont.render(self.instructiontext,50,self.instructionfontcolor)
        #screen.blit(self.instructionren,(350,0))
        #self.instructionfontcolor = (0,255,127)
        #self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #self.instructiontext = "Instructions"
        #self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        #screen.blit(self.instructionren,(350,0))
        script = "In this scenario, players do not have a great deal of agency to affect the world around them. Players"
        script1 = "cannot effectively resist the Nazi regime until the protest in collective action. They can occasionally"
        script2 = "change their personal circumstances, and those situations are clearly marked. During the rest of the game,"
        script4 = "inner feelings, and how they negotiate living in exceptionally difficult circumstances. The primary responsibility"
        script5 = " of the Director in this game is to read and calibrate the emotional intensity of the players by asking questions"
        script6 = " that facilitate emotional exploration."
        script7 = "The pre-written scenes for this scenario emphasize these factors. In many of these scenes, you will have the"
        script9 = " find suggestions for how to do this for particular scenes, and examples of questions you might ask. In all cases"
        script10 = ", however, you should keep in mind that your questions should help the characters reveal their inner feelings,"
        script11 = "expose or demonstrate their relationships, or connect to daily life."
        # script13 =  "the situation they are living in, but do not have the power to change it."
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script1
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script2
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script3
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script4
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script5
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script6
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script7
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script8
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script9
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script10
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script11
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script12
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)


    def personal_context(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
           
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #gobackrectangle = pygame.Rect(40, 40, 80, 80)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        script = "Workshop:Personal Context( 10 mins)Beginning with the player to your left, ask each person to say their name, and tell the group"
        script1 = "how they first learned about the Holocaust. Go around the circle and end with yourself."
        script2 = "If you wish, you may also briefly tell the group why you chose to run this scenario. By asking" 
        script3 = "players to discuss their personal relationship to the Holocaust, this workshop helps calibrate"
        script5 = "Additionally, the Holocaust shaped the lives of multiple generations of Jews, even those whose." 
        script6 = "families were not personally affected. If Jewish players are present, this workshop can help set"  
        script7 = "the tone for the game, and serve as a reminder that the Holocaust is still present in the lives " 
        script8 = "of many Jews today. Some players may answer the question more broadly than it is written. "
        script9 = "For example, Jewish players often speak about their connection to Judaism or the effect the Holocaust had on their family"
        script10 = "Players might also talk about their connection to genocide more broadly. As long as what they are" 
        script11 = "talking about aligns with the goal of this work- shop, it is appropriate. If a player diverges"
        script12 = "from these topics, gently bring them back to focus on the game."
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script1
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script2
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script3
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        #self.instructiontext = script4
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script5
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script6
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script7
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script8
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script9
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script10
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script11
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script12
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()

    def lineups_casting7(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        
        #pygame.draw.rect(screen, (245,245,220), self.scorebox)
        #screen.blit(backmenuImg, (0,0))    
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #gobackrectangle = pygame.Rect(40, 40, 80, 80)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #self.instructiontext = "Instructions"
        #self.instructionren = self.instructionfont.render(self.instructiontext,50,self.instructionfontcolor)
        #screen.blit(self.instructionren,(350,0))
        #self.instructionfontcolor = (0,255,127)
        #self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #self.instructiontext = "Instructions"
        #self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        #screen.blit(self.instructionren,(350,0))
        script = "It is possible that your players will try to break the tone of the game, either because they are accustomed"
        script1 = " to games where the characters have a great deal of freedom or as a response to difficult feelings they,"
        script2 = " as a player, may be having. If this happens, gently intercede. Do not accept the contribution into the"
        script3 = " fiction of the game. Explain that their proposed action does not fit this scenario, reminding them of the"
        script4 = " principles of play if necessary, and ask them to try again."
        script5 = "                                                                                                           "
        script6 = "Dyads"
        script7 = "This scenario centers not on individual characters, but rather on dyads - three husband-wife pairs, and one"
        script8 = "brother-sister pair. Each player portrays a male and a female character from different dyads, and each dyad"
        script9 = " involves two of the four players."
        script10 = "These dyads are the heart of the game. As such, keep in mind the following:"
        script11 = "- The two players in a dyad should be seated next to one another, so that they can engage closely and"
        script11 = " intimately during their scenes. If this is not possible, ask the active players to leave their seats and"
        script12 = " stand next to one another while they play."
        # script13 =  "the situation they are living in, but do not have the power to change it."
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script1
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script2
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script3
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script4
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script5
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script6
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script7
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script8
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script9
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script10
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script11
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script12
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
 

    def menu(self): 
        screen.blit(backgroundImg, (0,0))
        screen.blit(logoTextImg, (400,10))
        screen.blit(instructionImg, (185,640)) 
        screen.blit(playImg, (785,640))

        running = True 
        while running:  
            mouseposition = pygame.mouse.get_pos()  
            mousepressed = pygame.mouse.get_pressed()
            if self.instructionBox.collidepoint(mouseposition) and mousepressed[0] == 1:
                print 'b'
                self.playInstructions()
            if self.playBox.collidepoint(mouseposition) and mousepressed[0] == 1:
                self.playGame()
    
            # --- Limit to 60 frames per second
            clock.tick(60)

            events = pygame.event.get()  
            for event in events: 
                if event.type == pygame.QUIT: 
                    sys.exit(0) 

            pygame.display.update() 

Menu().menu() # runs the menu of the page 