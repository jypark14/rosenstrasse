# Import the pygame library and initialise the game engine


# player name / character name on the game page 
# sound files must be only played if facilitator clikcs on the sound effect 4
# only show cards that are relevant (if Izak is in prison use this card - just ask the facilitator) 3 
# going to specific cards from the playing screen - in an easy way --- lowest priority 
# return to menu -> game (then it starts at the same card where it has been left off )
# readme text 2
# no hardcoded text -> textfile 1

# Wednesday 9 a.m. - lab 

import pygame
import time  
import sys
import os 
import random
pygame.init()

alertbox = pygame.transform.scale(pygame.image.load("images/gameimages/alertbox.png"), (210,60))
alertbox2 = pygame.transform.scale(pygame.image.load("images/gameimages/alertbox.png"), (210,60))
alertbox3 = pygame.transform.scale(pygame.image.load("images/gameimages/alertbox.png"), (210,60))
b = pygame.transform.scale(pygame.image.load("images/gameimages/b.png"), (210,200))

next2 = pygame.transform.scale(pygame.image.load("images/gameimages/next.png"), (30,30))

sound = pygame.transform.scale(pygame.image.load("images/gameimages/sound.png"), (40,40))
risk = pygame.transform.scale(pygame.image.load("images/gameimages/risk.png"), (230,110))
background = pygame.transform.scale(pygame.image.load("images/gameimages/back_intro.png"), (1200, 900))
backgroundImg = pygame.transform.scale(pygame.image.load("images/mainbg.png"), (1200,900))
instructionImg = pygame.transform.scale(pygame.image.load("images/gameimages/back_instruction.png"), (230,80))
playImg = pygame.transform.scale(pygame.image.load("images/gameimages/back_play.png"), (230,80))
next = pygame.transform.scale(pygame.image.load("images/gameimages/next.png"), (30,30))
prevImg = pygame.transform.scale(pygame.image.load("images/gameimages/goback.png"), (30,30))
cardBg = pygame.transform.scale(pygame.image.load("images/cardbackgroundImg.png"), (1200,900))
logoTextImg = pygame.transform.scale(pygame.image.load("images/mainlogo.png"), (400,100))
dir1 = pygame.transform.scale(pygame.image.load("images/dir/1.png"), (330,550))
dir2 = pygame.transform.scale(pygame.image.load("images/dir/2.png"), (330,550))
dir3 = pygame.transform.scale(pygame.image.load("images/dir/3.png"), (330,550))
dir4 = pygame.transform.scale(pygame.image.load("images/dir/4.png"), (330,550))
dir5 = pygame.transform.scale(pygame.image.load("images/dir/5.png"), (330,550))
dir6 = pygame.transform.scale(pygame.image.load("images/dir/6.png"), (330,550))
dir7a = pygame.transform.scale(pygame.image.load("images/dir/7a.png"), (330,550))
dir7b = pygame.transform.scale(pygame.image.load("images/dir/7b.png"), (330,550))
dir8 = pygame.transform.scale(pygame.image.load("images/dir/8.png"), (330,550))
dir9 = pygame.transform.scale(pygame.image.load("images/dir/9.png"), (330,550))
dir10 = pygame.transform.scale(pygame.image.load("images/dir/10.png"), (330,550))
dir11 = pygame.transform.scale(pygame.image.load("images/dir/11.png"), (330,550))
dir12 = pygame.transform.scale(pygame.image.load("images/dir/12.png"), (330,550))
dir13a = pygame.transform.scale(pygame.image.load("images/dir/13a.png"), (330,550))
dir13b = pygame.transform.scale(pygame.image.load("images/dir/13b.png"), (330,550))
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
dir27a = pygame.transform.scale(pygame.image.load("images/dir/27a.png"), (330,550))
dir27b = pygame.transform.scale(pygame.image.load("images/dir/27b.png"), (330,550))
dir28a = pygame.transform.scale(pygame.image.load("images/dir/28a.png"), (330,550))
dir28b = pygame.transform.scale(pygame.image.load("images/dir/28b.png"), (330,550))
dir29 = pygame.transform.scale(pygame.image.load("images/dir/29.png"), (330,550))
dir30 = pygame.transform.scale(pygame.image.load("images/dir/30.png"), (330,550))
dir31 = pygame.transform.scale(pygame.image.load("images/dir/31.png"), (330,550))
dir32 = pygame.transform.scale(pygame.image.load("images/dir/32.png"), (330,550))
dir33 = pygame.transform.scale(pygame.image.load("images/dir/33.png"), (330,550))
dir34 = pygame.transform.scale(pygame.image.load("images/dir/34.png"), (330,550))
dir35a = pygame.transform.scale(pygame.image.load("images/dir/35a.png"), (330,550))
dir35b = pygame.transform.scale(pygame.image.load("images/dir/35b.png"), (330,550))
dir35c = pygame.transform.scale(pygame.image.load("images/dir/35c.png"), (330,550))
dir35d = pygame.transform.scale(pygame.image.load("images/dir/35d.png"), (330,550))
dir35e = pygame.transform.scale(pygame.image.load("images/dir/35e.png"), (330,550))
dir35f = pygame.transform.scale(pygame.image.load("images/dir/35f.png"), (330,550))
dir36 = pygame.transform.scale(pygame.image.load("images/dir/36.png"), (330,550))
dir37 = pygame.transform.scale(pygame.image.load("images/dir/37.png"), (330,550))
dir38 = pygame.transform.scale(pygame.image.load("images/dir/38.png"), (330,550))
dir39 = pygame.transform.scale(pygame.image.load("images/dir/39.png"), (330,550))
dir40 = pygame.transform.scale(pygame.image.load("images/dir/40.png"), (330,550))
dir41 = pygame.transform.scale(pygame.image.load("images/dir/41.png"), (330,550))
dir42 = pygame.transform.scale(pygame.image.load("images/dir/42.png"), (330,550))
dir43a = pygame.transform.scale(pygame.image.load("images/dir/43a.png"), (330,550))
dir43b = pygame.transform.scale(pygame.image.load("images/dir/43b.png"), (330,550))
dir44 = pygame.transform.scale(pygame.image.load("images/dir/44.png"), (330,550))
dir45 = pygame.transform.scale(pygame.image.load("images/dir/45.png"), (330,550))
dir46 = pygame.transform.scale(pygame.image.load("images/dir/46.png"), (330,550))
dir47 = pygame.transform.scale(pygame.image.load("images/dir/47.png"), (330,550))
dir48 = pygame.transform.scale(pygame.image.load("images/dir/48.png"), (330,550))
dir49 = pygame.transform.scale(pygame.image.load("images/dir/49.png"), (330,550))
dir50 = pygame.transform.scale(pygame.image.load("images/dir/50.png"), (330,550))
dir51 = pygame.transform.scale(pygame.image.load("images/dir/51.png"), (330,550))
dir52 = pygame.transform.scale(pygame.image.load("images/dir/52.png"), (330,550))
dir53 = pygame.transform.scale(pygame.image.load("images/dir/53.png"), (330,550))
dir54 = pygame.transform.scale(pygame.image.load("images/dir/54.png"), (330,550))
dir55 = pygame.transform.scale(pygame.image.load("images/dir/55.png"), (330,550))
dir56 = pygame.transform.scale(pygame.image.load("images/dir/56.png"), (330,550))
dir57a = pygame.transform.scale(pygame.image.load("images/dir/57a.png"), (330,550))
dir57b = pygame.transform.scale(pygame.image.load("images/dir/57b.png"), (330,550))
dir58 = pygame.transform.scale(pygame.image.load("images/dir/58.png"), (330,550))
dir59 = pygame.transform.scale(pygame.image.load("images/dir/59.png"), (330,550))
dir60 = pygame.transform.scale(pygame.image.load("images/dir/60.png"), (330,550))
dir61 = pygame.transform.scale(pygame.image.load("images/dir/61.png"), (330,550))
dir62 = pygame.transform.scale(pygame.image.load("images/dir/62.png"), (330,550))
dir63 = pygame.transform.scale(pygame.image.load("images/dir/63.png"), (330,550))
dir64 = pygame.transform.scale(pygame.image.load("images/dir/64.png"), (330,550))
dir65a = pygame.transform.scale(pygame.image.load("images/dir/65a.png"), (330,550))
dir65b = pygame.transform.scale(pygame.image.load("images/dir/65b.png"), (330,550))
dir66 = pygame.transform.scale(pygame.image.load("images/dir/66.png"), (330,550))
dir67 = pygame.transform.scale(pygame.image.load("images/dir/67.png"), (330,550))
dir68 = pygame.transform.scale(pygame.image.load("images/dir/68.png"), (330,550))
dir69a = pygame.transform.scale(pygame.image.load("images/dir/69a.png"), (330,550))
dir69b = pygame.transform.scale(pygame.image.load("images/dir/69b.png"), (330,550))
dir70 = pygame.transform.scale(pygame.image.load("images/dir/70.png"), (330,550))
dir71 = pygame.transform.scale(pygame.image.load("images/dir/71.png"), (330,550))
dir72 = pygame.transform.scale(pygame.image.load("images/dir/72.png"), (330,550))
dir73 = pygame.transform.scale(pygame.image.load("images/dir/73.png"), (330,550))
dir74 = pygame.transform.scale(pygame.image.load("images/dir/74.png"), (330,550))
dir75 = pygame.transform.scale(pygame.image.load("images/dir/75.png"), (330,550))
dir76 = pygame.transform.scale(pygame.image.load("images/dir/76.png"), (330,550))
dir77 = pygame.transform.scale(pygame.image.load("images/dir/77.png"), (330,550))
dir78 = pygame.transform.scale(pygame.image.load("images/dir/78.png"), (330,550))
dir79 = pygame.transform.scale(pygame.image.load("images/dir/79.png"), (330,550))
dir80 = pygame.transform.scale(pygame.image.load("images/dir/80.png"), (330,550))
dir81 = pygame.transform.scale(pygame.image.load("images/dir/81.png"), (330,550))
dir82 = pygame.transform.scale(pygame.image.load("images/dir/82.png"), (330,550))
dir83 = pygame.transform.scale(pygame.image.load("images/dir/83.png"), (330,550))
dir84 = pygame.transform.scale(pygame.image.load("images/dir/84.png"), (330,550))
dir85 = pygame.transform.scale(pygame.image.load("images/dir/85.png"), (330,550))
dir86 = pygame.transform.scale(pygame.image.load("images/dir/86.png"), (330,550))
dir87 = pygame.transform.scale(pygame.image.load("images/dir/87.png"), (330,550))
dir88 = pygame.transform.scale(pygame.image.load("images/dir/88.png"), (330,550))
dir89 = pygame.transform.scale(pygame.image.load("images/dir/89.png"), (330,550))
dir90 = pygame.transform.scale(pygame.image.load("images/dir/90.png"), (330,550))

dirArray = [0, dir1, dir2, dir3, dir4, dir5, dir6, dir7a, dir8, dir9, dir10, dir11, dir12, dir13a, 
dir14, dir15, dir16, dir17, dir18, dir19, dir20, dir21, dir22, dir23, dir24, dir25, dir26, dir27a, dir28a, 
dir29, dir30, dir31, dir32, dir33, dir34, dir35a, dir36, dir37, dir38, dir39, 
dir40, dir41, dir42, dir43a, dir44, dir45, dir46, dir47, dir48, dir49, dir50, dir51, dir52, dir53, dir54, dir55, dir56, dir57a, dir58, 
dir59, dir60, dir61, dir62, dir63, dir64, dir65a, dir66, dir67, dir68, dir69a, dir70, dir71, dir72, dir73,
dir74, dir75, dir76, dir77, dir78, dir79, dir80, dir81, dir82, dir83, dir84, dir85, dir86, dir87, dir88, 
dir89, dir90]

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

CARD_INDEX = 0
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

screen = pygame.display.set_mode((1200, 800))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)



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
        self.updated = False
        self.exempt = False

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
                #self.txt_surface = FONT.render(self.text, True, self.color)


    # def update(self):
    #     # Resize the box if the text is too long.
    #     width = max(200, self.txt_surface.get_width()+10)
    #     self.rect.w = width

    def draw(self, screen):
        character1= FONT.render("Izak", True, COLOR_INACTIVE)
        screen.blit(character1,(500,50))

        character1= FONT.render("Josef", True, COLOR_INACTIVE)
        screen.blit(character1,(650,50))

        character1= FONT.render("Kurt", True, COLOR_INACTIVE)
        screen.blit(character1,(800,50))

        character1= FONT.render("Max", True, COLOR_INACTIVE)
        screen.blit(character1,(950,50))

        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        screen.blit(FONT.render(self.name, True, self.color), (self.rect.x-500, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(prevImg, (0,0))

		########################################################
		#risk matrix boxes
		#risk matrix boxes
script170 = open("scripts/script170.txt", "r")
script171 = open("scripts/script171.txt", "r")
script172 = open("scripts/script172.txt", "r")
script173 = open("scripts/script173.txt", "r")
script174 = open("scripts/script174.txt", "r")
script175 = open("scripts/script175.txt", "r")
script176 = open("scripts/script176.txt", "r")
script177 = open("scripts/script177.txt", "r")
input_box1 = InputBox(500, 100, 50, 32, script170.read())
input_box2 = InputBox(500, 150, 50, 32, script171.read())
input_box3 = InputBox(500, 200, 50, 32, script172.read())
input_box4 = InputBox(500, 250, 50, 32, script173.read())
input_box5 = InputBox(500, 300, 50, 32, script174.read())
input_box6 = InputBox(500, 350, 50, 32, script175.read())
input_box7 = InputBox(500, 400, 50, 32, script176.read())
input_box8 = InputBox(500, 450, 50, 32, "Total Score")
input_boxExempt1 = InputBox(500,550, 50, 32, script177.read())
input_boxExempt1.txt_surface = FONT.render("No", False, input_boxExempt1.color)
input_box9 = InputBox(650, 100, 50, 32, "")
input_box10 = InputBox(650, 150, 50, 32, "")
input_box11 = InputBox(650, 200, 50, 32, "")
input_box12 = InputBox(650, 250, 50, 32, "")
input_box13 = InputBox(650, 300, 50, 32, "")
input_box14 = InputBox(650, 350, 50, 32, "")
input_box15 = InputBox(650, 400, 50, 32, "")
input_box16 = InputBox(650, 450, 50, 32, "")
input_boxExempt2 = InputBox(650, 550, 50, 32, "")
input_boxExempt2.txt_surface = FONT.render("No", False, input_boxExempt2.color)
input_box17 = InputBox(800, 100, 50, 32, "")
input_box18 = InputBox(800, 150, 50, 32, "")
input_box19 = InputBox(800, 200, 50, 32, "")
input_box20 = InputBox(800, 250, 50, 32, "")
input_box21 = InputBox(800, 300, 50, 32, "")
input_box22 = InputBox(800, 350, 50, 32, "")
input_box23 = InputBox(800, 400, 50, 32, "")
input_box24 = InputBox(800, 450, 50, 32, "")
input_boxExempt3 = InputBox(800, 550, 50, 32, "")
input_boxExempt3.txt_surface = FONT.render("No", False, input_boxExempt3.color)
input_box25 = InputBox(950, 100, 50, 32, "")
input_box26 = InputBox(950, 150, 50, 32, "")
input_box27 = InputBox(950, 200, 50, 32, "")
input_box28 = InputBox(950, 250, 50, 32, "")
input_box29 = InputBox(950, 300, 50, 32, "")
input_box30 = InputBox(950, 350, 50, 32, "")
input_box31 = InputBox(950, 400, 50, 32, "")
input_box32 = InputBox(950, 450, 50, 32, "")
input_boxExempt4 = InputBox(950, 550, 50,  32, "")
input_boxExempt4.txt_surface = FONT.render("No", False, input_boxExempt4.color)

input_boxes = [input_box1, input_box2, input_box3, input_box4, input_box5, input_box6, input_box7, input_box8,
		       input_box9, input_box10,input_box11, input_box12, input_box13, input_box14, input_box15, input_box16,
		       input_box17, input_box18,input_box19, input_box20, input_box21, input_box22, input_box23, input_box24,
		       input_box25, input_box26,input_box27, input_box28, input_box29, input_box30, input_box31, input_box32,
		       input_boxExempt1, input_boxExempt2, input_boxExempt3, input_boxExempt4]


class Menu(object): 
    def __init__(self):  
        self.instructionBox = pygame.Rect(185, 640, 230, 80)  
        self.playBox = pygame.Rect(785, 640, 230, 80)    
        homeScreen = True


    #risk matrix stuff 
    def display_risk(self, index):
        num = index
        clock = pygame.time.Clock()
        screen.blit
        self.backBox = pygame.Rect(0,0, 100,100)
        #creates risk matrixes for each character        
        done = False
        text = '0'
        while not done:
            for event in pygame.event.get():
                mouseposition = pygame.mouse.get_pos()  
                mousepressed = pygame.mouse.get_pressed()
                if self.backBox.collidepoint(mouseposition) and mousepressed[0] == 1: 
                    self.playGame(num)
                if event.type == pygame.QUIT:
                    done = True
                for box in input_boxes:
                    box.handle_event(event)
                    if input_box1.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '10'
                    if input_box2.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '5'
                    if input_box3.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '-5'
                    if input_box4.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '-3'
                    if input_box5.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '2'
                    if input_box6.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '3'
                    if input_box7.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '2'
                    if input_box8.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '0'

                    if input_box9.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '10'
                    if input_box10.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '5'
                    if input_box11.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '-5'
                    if input_box12.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '-3'
                    if input_box13.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '2'
                    if input_box14.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '3'
                    if input_box15.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '2'
                    if input_box16.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '0'


                    if input_box17.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '10'
                    if input_box18.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '5'
                    if input_box19.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '-5'
                    if input_box20.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '-3'
                    if input_box21.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '2'
                    if input_box22.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '3'
                    if input_box23.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '2'
                    if input_box24.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '0'



                    if input_box25.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '10'
                    if input_box26.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '5'
                    if input_box27.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '-5'
                    if input_box28.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '-3'
                    if input_box29.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '2'
                    if input_box30.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '3'
                    if input_box31.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '2'
                    if input_box32.active == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                my_text = '0'



                if event.type == pygame.KEYDOWN and input_box1.updated == False and input_box1.active == True:    
                    input_box1.txt_surface = FONT.render(my_text, True, input_box1.color)
                    my_text = "10"
                    input_box1.txt_surface = FONT.render(my_text, True, input_box1.color)
                    input_box8.sum += int(my_text)
                    sum = str(input_box8.sum)
                    if input_box1.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box1.color)
                    input_box1.updated = True
                elif event.type == pygame.KEYDOWN and input_box1.updated == True and input_box1.active == True: 
                    my_text = '-10'   
                    input_box1.txt_surface = FONT.render('0', True, input_box1.color)
                    input_box8.sum += int(my_text)
                    sum = str(input_box8.sum)
                    if input_box1.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box1.color)
                    input_box1.updated = False
                elif event.type == pygame.KEYDOWN and input_box2.updated == False and input_box2.active == True:    
                    input_box2.txt_surface = FONT.render(my_text, True, input_box2.color)
                    input_box8.sum += int(my_text)
                    sum = str(input_box8.sum)
                    if input_box2.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box2.color)
                    input_box2.updated = True
                elif event.type == pygame.KEYDOWN and input_box2.updated == True and input_box2.active == True: 
                    # my_text = '-5'   
                    input_box2.txt_surface = FONT.render('0', True, input_box2.color)
                    input_box8.sum += -5
                    sum = str(input_box8.sum)
                    if input_box2.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box2.color)
                    input_box2.updated = False
                elif event.type == pygame.KEYDOWN and input_box3.updated == False and input_box3.active == True:    
                    input_box3.txt_surface = FONT.render(my_text, True, input_box3.color)
                    input_box8.sum += int(my_text)
                    sum = str(input_box8.sum)
                    if input_box3.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box3.color)
                    input_box3.updated = True
                elif event.type == pygame.KEYDOWN and input_box3.updated == True and input_box3.active == True: 
                    # my_text = '-5'   
                    input_box3.txt_surface = FONT.render('0', True, input_box3.color)
                    input_box8.sum += 5
                    sum = str(input_box8.sum)
                    if input_box3.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box3.color)
                    input_box3.updated = False
                elif event.type == pygame.KEYDOWN and input_box4.updated == False and input_box4.active == True:    
                    input_box4.txt_surface = FONT.render(my_text, True, input_box4.color)
                    input_box8.sum += int(my_text)
                    sum = str(input_box8.sum)
                    if input_box4.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box4.color)
                    input_box4.updated = True
                elif event.type == pygame.KEYDOWN and input_box4.updated == True and input_box4.active == True: 
                    # my_text = '-5'   
                    input_box4.txt_surface = FONT.render('0', True, input_box4.color)
                    input_box8.sum += 3
                    sum = str(input_box8.sum)
                    if input_box4.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box4.color)
                    input_box4.updated = False
                elif event.type == pygame.KEYDOWN and input_box5.updated == False and input_box5.active == True:    
                    input_box5.txt_surface = FONT.render(my_text, True, input_box5.color)
                    input_box8.sum += int(my_text)
                    sum = str(input_box8.sum)
                    if input_box5.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box5.color)
                    input_box5.updated = True
                elif event.type == pygame.KEYDOWN and input_box5.updated == True and input_box5.active == True: 
                    # my_text = '-5'   
                    input_box5.txt_surface = FONT.render('0', True, input_box5.color)
                    input_box8.sum += -2
                    sum = str(input_box8.sum)
                    if input_box5.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box5.color)
                    input_box5.updated = False
                elif event.type == pygame.KEYDOWN and input_box6.updated == False and input_box6.active == True:    
                    input_box6.txt_surface = FONT.render(my_text, True, input_box6.color)
                    input_box8.sum += int(my_text)
                    sum = str(input_box8.sum)
                    if input_box6.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box6.color)
                    input_box6.updated = True
                elif event.type == pygame.KEYDOWN and input_box6.updated == True and input_box6.active == True: 
                    # my_text = '-5'   
                    input_box6.txt_surface = FONT.render('0', True, input_box6.color)
                    input_box8.sum += -3
                    sum = str(input_box8.sum)
                    if input_box6.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box6.color)
                    input_box6.updated = False
                elif event.type == pygame.KEYDOWN and input_box7.updated == False and input_box7.active == True:    
                    input_box7.txt_surface = FONT.render(my_text, True, input_box7.color)
                    input_box8.sum += int(my_text)
                    sum = str(input_box8.sum)
                    if input_box7.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box7.color)
                    input_box7.updated = True
                elif event.type == pygame.KEYDOWN and input_box7.updated == True and input_box7.active == True: 
                    # my_text = '-5'   
                    input_box7.txt_surface = FONT.render('0', True, input_box7.color)
                    input_box8.sum += -2
                    sum = str(input_box8.sum)
                    if input_box7.exempt == True:
                        sum = '0'
                    input_box8.txt_surface = FONT.render(sum, True, input_box7.color)
                    input_box7.updated = False
                elif event.type == pygame.KEYDOWN and input_box8.updated == False and input_box8.active == True:    
                    input_box8.txt_surface = FONT.render(my_text, True, input_box8.color)
                    input_box8.sum += int(my_text)
                    sum = str(input_box8.sum)
                    input_box8.txt_surface = FONT.render(sum, True, input_box8.color)
                    input_box8.updated = True
                elif event.type == pygame.KEYDOWN and input_boxExempt1.updated == False and input_boxExempt1.active == True:
                    input_box1.exempt = True
                    input_box1.txt_surface = FONT.render('0', True, input_box1.color)
                    input_box2.exempt = True
                    input_box2.txt_surface = FONT.render('0', True, input_box2.color)
                    input_box3.exempt = True
                    input_box3.txt_surface = FONT.render('0', True, input_box3.color)
                    input_box4.exempt = True
                    input_box4.txt_surface = FONT.render('0', True, input_box4.color)
                    input_box5.exempt = True
                    input_box5.txt_surface = FONT.render('0', True, input_box5.color)
                    input_box6.exempt = True
                    input_box6.txt_surface = FONT.render('0', True, input_box6.color)
                    input_box7.exempt = True
                    input_box7.txt_surface = FONT.render('0', True, input_box7.color)
                    input_box8.txt_surface = FONT.render('0', True, input_box1.color)
                    input_boxExempt1.txt_surface = FONT.render('Yes', True, input_boxExempt1.color)




                elif event.type == pygame.KEYDOWN and input_box9.updated == False and input_box9.active == True:    
                    input_box9.txt_surface = FONT.render(my_text, True, input_box9.color)
                    input_box16.sum += int(my_text)
                    sum = str(input_box16.sum)
                    if input_box9.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box9.color)
                    input_box9.updated = True
                elif event.type == pygame.KEYDOWN and input_box9.updated == True and input_box9.active == True: 
                    input_box9.txt_surface = FONT.render('0', True, input_box9.color)
                    input_box16.sum += -10
                    sum = str(input_box16.sum)
                    if input_box9.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box9.color)
                    input_box9.updated = False
                elif event.type == pygame.KEYDOWN and input_box10.updated == False and input_box10.active == True:    
                    input_box10.txt_surface = FONT.render(my_text, True, input_box10.color)
                    input_box16.sum += int(my_text)
                    sum = str(input_box16.sum)
                    if input_box10.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box10.color)
                    input_box10.updated = True
                elif event.type == pygame.KEYDOWN and input_box10.updated == True and input_box10.active == True: 
                    input_box10.txt_surface = FONT.render('0', True, input_box10.color)
                    input_box16.sum += -5
                    sum = str(input_box16.sum)
                    if input_box10.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box10.color)
                    input_box10.updated = False
                elif event.type == pygame.KEYDOWN and input_box11.updated == False and input_box11.active == True:    
                    input_box11.txt_surface = FONT.render(my_text, True, input_box11.color)
                    input_box16.sum += int(my_text)
                    sum = str(input_box16.sum)
                    if input_box11.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box11.color)
                    input_box11.updated = True
                elif event.type == pygame.KEYDOWN and input_box11.updated == True and input_box11.active == True: 
                    input_box11.txt_surface = FONT.render('0', True, input_box11.color)
                    input_box16.sum += 5
                    sum = str(input_box16.sum)
                    if input_box11.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box11.color)
                    input_box11.updated = False
                elif event.type == pygame.KEYDOWN and input_box12.updated == False and input_box12.active == True:    
                    input_box12.txt_surface = FONT.render(my_text, True, input_box12.color)
                    input_box16.sum += int(my_text)
                    sum = str(input_box16.sum)
                    if input_box12.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box12.color)
                    input_box12.updated = True
                elif event.type == pygame.KEYDOWN and input_box12.updated == True and input_box12.active == True: 
                    input_box12.txt_surface = FONT.render('0', True, input_box12.color)
                    input_box16.sum += 3
                    sum = str(input_box16.sum)
                    if input_box12.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box12.color)
                    input_box12.updated = False
                elif event.type == pygame.KEYDOWN and input_box13.updated == False and input_box13.active == True:    
                    input_box13.txt_surface = FONT.render(my_text, True, input_box13.color)
                    input_box16.sum += int(my_text)
                    sum = str(input_box16.sum)
                    if input_box13.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box13.color)
                    input_box13.updated = True
                elif event.type == pygame.KEYDOWN and input_box13.updated == True and input_box13.active == True: 
                    input_box13.txt_surface = FONT.render('0', True, input_box13.color)
                    input_box16.sum += -2
                    sum = str(input_box16.sum)
                    if input_box13.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box13.color)
                    input_box13.updated = False
                elif event.type == pygame.KEYDOWN and input_box14.updated == False and input_box14.active == True:    
                    input_box14.txt_surface = FONT.render(my_text, True, input_box14.color)
                    input_box16.sum += int(my_text)
                    sum = str(input_box16.sum)
                    if input_box14.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box14.color)
                    input_box14.updated = True
                elif event.type == pygame.KEYDOWN and input_box14.updated == True and input_box14.active == True: 
                    input_box14.txt_surface = FONT.render('0', True, input_box14.color)
                    input_box16.sum += -3
                    sum = str(input_box16.sum)
                    if input_box14.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box14.color)
                    input_box14.updated = False
                elif event.type == pygame.KEYDOWN and input_box15.updated == False and input_box15.active == True:    
                    input_box15.txt_surface = FONT.render(my_text, True, input_box15.color)
                    input_box16.sum += int(my_text)
                    sum = str(input_box16.sum)
                    if input_box15.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box15.color)
                    input_box15.updated = True
                elif event.type == pygame.KEYDOWN and input_box15.updated == True and input_box15.active == True: 
                    input_box15.txt_surface = FONT.render('0', True, input_box15.color)
                    input_box16.sum += -2
                    sum = str(input_box16.sum)
                    if input_box15.exempt == True:
                        sum = '0'
                    input_box16.txt_surface = FONT.render(sum, True, input_box15.color)
                    input_box15.updated = False
                elif event.type == pygame.KEYDOWN and input_box16.updated == False and input_box16.active == True:    
                    input_box16.txt_surface = FONT.render(my_text, True, input_box16.color)
                    input_box16.sum += int(my_text)
                    sum = str(input_box16.sum)
                    input_box16.txt_surface = FONT.render(sum, True, input_box16.color)
                    input_box16.updated = True
                elif event.type == pygame.KEYDOWN and input_boxExempt2.updated == False and input_boxExempt2.active == True:
                    input_box9.exempt = True
                    input_box9.txt_surface = FONT.render('0', True, input_box9.color)
                    input_box10.exempt = True
                    input_box10.txt_surface = FONT.render('0', True, input_box10.color)
                    input_box11.exempt = True
                    input_box11.txt_surface = FONT.render('0', True, input_box11.color)
                    input_box12.exempt = True
                    input_box12.txt_surface = FONT.render('0', True, input_box12.color)
                    input_box13.exempt = True
                    input_box13.txt_surface = FONT.render('0', True, input_box13.color)
                    input_box14.exempt = True
                    input_box14.txt_surface = FONT.render('0', True, input_box14.color)
                    input_box15.exempt = True
                    input_box15.txt_surface = FONT.render('0', True, input_box15.color)
                    input_box16.txt_surface = FONT.render('0', True, input_box16.color)
                    input_boxExempt2.txt_surface = FONT.render('Yes', True, input_boxExempt2.color)

                elif event.type == pygame.KEYDOWN and input_box17.updated == False and input_box17.active == True:    
                    input_box17.txt_surface = FONT.render(my_text, True, input_box17.color)
                    input_box24.sum += int(my_text)
                    sum = str(input_box24.sum)
                    if input_box17.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box17.color)
                    input_box17.updated = True
                elif event.type == pygame.KEYDOWN and input_box17.updated == True and input_box17.active == True: 
                    input_box17.txt_surface = FONT.render('0', True, input_box17.color)
                    input_box24.sum += -10
                    sum = str(input_box24.sum)
                    if input_box17.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box17.color)
                    input_box17.updated = False
                elif event.type == pygame.KEYDOWN and input_box18.updated == False and input_box18.active == True:    
                    input_box18.txt_surface = FONT.render(my_text, True, input_box18.color)
                    input_box24.sum += int(my_text)
                    sum = str(input_box24.sum)
                    if input_box18.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box18.color)
                    input_box18.updated = True
                elif event.type == pygame.KEYDOWN and input_box18.updated == True and input_box18.active == True: 
                    input_box18.txt_surface = FONT.render('0', True, input_box18.color)
                    input_box24.sum += -5
                    sum = str(input_box24.sum)
                    if input_box18.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box18.color)
                    input_box18.updated = False
                elif event.type == pygame.KEYDOWN and input_box19.updated == False and input_box19.active == True:    
                    input_box19.txt_surface = FONT.render(my_text, True, input_box19.color)
                    input_box24.sum += int(my_text)
                    sum = str(input_box24.sum)
                    if input_box19.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box19.color)
                    input_box19.updated = True
                elif event.type == pygame.KEYDOWN and input_box19.updated == True and input_box19.active == True: 
                    input_box19.txt_surface = FONT.render('0', True, input_box19.color)
                    input_box24.sum += 5
                    sum = str(input_box24.sum)
                    if input_box9.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box19.color)
                    input_box19.updated = False
                elif event.type == pygame.KEYDOWN and input_box20.updated == False and input_box20.active == True:    
                    input_box20.txt_surface = FONT.render(my_text, True, input_box20.color)
                    input_box24.sum += int(my_text)
                    sum = str(input_box24.sum)
                    if input_box20.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box20.color)
                    input_box20.updated = True
                elif event.type == pygame.KEYDOWN and input_box20.updated == True and input_box20.active == True: 
                    input_box20.txt_surface = FONT.render('0', True, input_box20.color)
                    input_box24.sum += 3
                    sum = str(input_box24.sum)
                    if input_box20.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box20.color)
                    input_box20.updated = False
                elif event.type == pygame.KEYDOWN and input_box21.updated == False and input_box21.active == True:    
                    input_box21.txt_surface = FONT.render(my_text, True, input_box21.color)
                    input_box24.sum += int(my_text)
                    sum = str(input_box24.sum)
                    if input_box21.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box21.color)
                    input_box21.updated = True
                elif event.type == pygame.KEYDOWN and input_box21.updated == True and input_box21.active == True: 
                    input_box21.txt_surface = FONT.render('0', True, input_box21.color)
                    input_box24.sum += -2
                    sum = str(input_box24.sum)
                    if input_box21.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box21.color)
                    input_box21.updated = False
                elif event.type == pygame.KEYDOWN and input_box22.updated == False and input_box22.active == True:    
                    input_box22.txt_surface = FONT.render(my_text, True, input_box22.color)
                    input_box24.sum += int(my_text)
                    sum = str(input_box24.sum)
                    if input_box22.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box22.color)
                    input_box22.updated = True
                elif event.type == pygame.KEYDOWN and input_box22.updated == True and input_box22.active == True: 
                    input_box22.txt_surface = FONT.render('0', True, input_box22.color)
                    input_box24.sum += -3
                    sum = str(input_box24.sum)
                    if input_box22.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box22.color)
                    input_box22.updated = False
                elif event.type == pygame.KEYDOWN and input_box23.updated == False and input_box23.active == True:    
                    input_box23.txt_surface = FONT.render(my_text, True, input_box23.color)
                    input_box24.sum += int(my_text)
                    sum = str(input_box24.sum)
                    if input_box23.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box23.color)
                    input_box23.updated = True
                elif event.type == pygame.KEYDOWN and input_box23.updated == True and input_box23.active == True: 
                    input_box23.txt_surface = FONT.render('0', True, input_box23.color)
                    input_box24.sum += -2
                    sum = str(input_box24.sum)
                    if input_box23.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box23.color)
                    input_box23.updated = False
                elif event.type == pygame.KEYDOWN and input_box24.updated == False and input_box24.active == True:    
                    input_box24.txt_surface = FONT.render(my_text, True, input_box24.color)
                    input_box24.sum += int(my_text)
                    sum = str(input_box24.sum)
                    if input_box24.exempt == True:
                        sum = '0'
                    input_box24.txt_surface = FONT.render(sum, True, input_box24.color)
                    input_box24.updated = True
                elif event.type == pygame.KEYDOWN and input_boxExempt3.updated == False and input_boxExempt3.active == True:
                    input_box16.exempt = True
                    input_box16.txt_surface = FONT.render('0', True, input_box16.color)
                    input_box17.exempt = True
                    input_box17.txt_surface = FONT.render('0', True, input_box17.color)
                    input_box18.exempt = True
                    input_box18.txt_surface = FONT.render('0', True, input_box18.color)
                    input_box19.exempt = True
                    input_box19.txt_surface = FONT.render('0', True, input_box19.color)
                    input_box20.exempt = True
                    input_box20.txt_surface = FONT.render('0', True, input_box20.color)
                    input_box21.exempt = True
                    input_box21.txt_surface = FONT.render('0', True, input_box21.color)
                    input_box22.exempt = True
                    input_box22.txt_surface = FONT.render('0', True, input_box22.color)
                    input_box23.exempt = True
                    input_box23.txt_surface = FONT.render('0', True, input_box23.color)
                    input_box24.txt_surface = FONT.render('0', True, input_box24.color)
                    input_boxExempt3.txt_surface = FONT.render('Yes', True, input_boxExempt3.color)

                elif event.type == pygame.KEYDOWN and input_box25.updated == False and input_box25.active == True:    
                    input_box25.txt_surface = FONT.render(my_text, True, input_box25.color)
                    input_box32.sum += int(my_text)
                    sum = str(input_box32.sum)
                    if input_box25.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box25.color)
                    input_box25.updated = True
                elif event.type == pygame.KEYDOWN and input_box25.updated == True and input_box25.active == True: 
                    input_box25.txt_surface = FONT.render('0', True, input_box25.color)
                    input_box32.sum += -10
                    sum = str(input_box32.sum)
                    if input_box25.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box25.color)
                    input_box25.updated = False
                elif event.type == pygame.KEYDOWN and input_box26.updated == False and input_box26.active == True:    
                    input_box26.txt_surface = FONT.render(my_text, True, input_box26.color)
                    input_box32.sum += int(my_text)
                    sum = str(input_box32.sum)
                    if input_box26.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box26.color)
                    input_box26.updated = True
                elif event.type == pygame.KEYDOWN and input_box26.updated == True and input_box26.active == True: 
                    input_box26.txt_surface = FONT.render('0', True, input_box26.color)
                    input_box32.sum += -5
                    sum = str(input_box32.sum)
                    if input_box26.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box26.color)
                    input_box26.updated = False
                elif event.type == pygame.KEYDOWN and input_box27.updated == False and input_box27.active == True:    
                    input_box27.txt_surface = FONT.render(my_text, True, input_box27.color)
                    input_box32.sum += int(my_text)
                    sum = str(input_box32.sum)
                    if input_box27.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box27.color)
                    input_box27.updated = True
                elif event.type == pygame.KEYDOWN and input_box27.updated == True and input_box27.active == True: 
                    input_box27.txt_surface = FONT.render('0', True, input_box27.color)
                    input_box32.sum += 5
                    sum = str(input_box32.sum)
                    if input_box27.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box27.color)
                    input_box27.updated = False
                elif event.type == pygame.KEYDOWN and input_box28.updated == False and input_box28.active == True:    
                    input_box28.txt_surface = FONT.render(my_text, True, input_box28.color)
                    input_box32.sum += int(my_text)
                    sum = str(input_box32.sum)
                    if input_box28.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box28.color)
                    input_box28.updated = True
                elif event.type == pygame.KEYDOWN and input_box28.updated == True and input_box28.active == True: 
                    input_box28.txt_surface = FONT.render('0', True, input_box28.color)
                    input_box32.sum += 3
                    sum = str(input_box32.sum)
                    if input_box28.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box28.color)
                    input_box28.updated = False
                elif event.type == pygame.KEYDOWN and input_box29.updated == False and input_box29.active == True:    
                    input_box29.txt_surface = FONT.render(my_text, True, input_box29.color)
                    input_box32.sum += int(my_text)
                    sum = str(input_box32.sum)
                    if input_box29.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box29.color)
                    input_box29.updated = True
                elif event.type == pygame.KEYDOWN and input_box29.updated == True and input_box29.active == True: 
                    input_box29.txt_surface = FONT.render('0', True, input_box29.color)
                    input_box32.sum += -2
                    sum = str(input_box32.sum)
                    if input_box29.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box29.color)
                    input_box29.updated = False
                elif event.type == pygame.KEYDOWN and input_box30.updated == False and input_box30.active == True:    
                    input_box30.txt_surface = FONT.render(my_text, True, input_box30.color)
                    input_box32.sum += int(my_text)
                    sum = str(input_box32.sum)
                    if input_box30.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box30.color)
                    input_box30.updated = True
                elif event.type == pygame.KEYDOWN and input_box30.updated == True and input_box30.active == True: 
                    input_box30.txt_surface = FONT.render('0', True, input_box30.color)
                    input_box32.sum += -3
                    sum = str(input_box32.sum)
                    if input_box30.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box30.color)
                    input_box30.updated = False
                elif event.type == pygame.KEYDOWN and input_box31.updated == False and input_box31.active == True:    
                    input_box31.txt_surface = FONT.render(my_text, True, input_box31.color)
                    input_box32.sum += int(my_text)
                    sum = str(input_box32.sum)
                    if input_box31.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box31.color)
                    input_box31.updated = True
                elif event.type == pygame.KEYDOWN and input_box31.updated == True and input_box31.active == True: 
                    input_box31.txt_surface = FONT.render('0', True, input_box31.color)
                    input_box32.sum += -2
                    sum = str(input_box32.sum)
                    if input_box31.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box31.color)
                    input_box31.updated = False
                elif event.type == pygame.KEYDOWN and input_box32.updated == False and input_box32.active == True:    
                    input_box32.txt_surface = FONT.render(my_text, True, input_box32.color)
                    input_box32.sum += int(my_text)
                    sum = str(input_box32.sum)
                    if input_box32.exempt == True:
                        sum = '0'
                    input_box32.txt_surface = FONT.render(sum, True, input_box32.color)
                    input_box32.updated = True
                elif event.type == pygame.KEYDOWN and input_boxExempt4.updated == False and input_boxExempt4.active == True:
                    input_box25.exempt = True
                    input_box25.txt_surface = FONT.render('0', True, input_box25.color)
                    input_box26.exempt = True
                    input_box26.txt_surface = FONT.render('0', True, input_box26.color)
                    input_box27.exempt = True
                    input_box27.txt_surface = FONT.render('0', True, input_box27.color)
                    input_box28.exempt = True
                    input_box28.txt_surface = FONT.render('0', True, input_box28.color)
                    input_box29.exempt = True
                    input_box29.txt_surface = FONT.render('0', True, input_box29.color)
                    input_box30.exempt = True
                    input_box30.txt_surface = FONT.render('0', True, input_box30.color)
                    input_box31.exempt = True
                    input_box31.txt_surface = FONT.render('0', True, input_box31.color)
                    input_box32.exempt = True
                    input_box32.txt_surface = FONT.render('0', True, input_box32.color)
                    input_boxExempt4.txt_surface = FONT.render('Yes', True, input_boxExempt4.color)

            screen.fill((30, 30, 30))
            for box in input_boxes:
                box.draw(screen)

            pygame.display.flip()
            clock.tick(30)

    def playGame(self,index): 
        # screen.fill(WHITE)
        self.riskBox = pygame.Rect(88, 440, 230, 80)    
        self.backBox = pygame.Rect(1100,0, 100,100)        
        self.nextBox = pygame.Rect(1000, 680, 40, 40)
        longercards = 7, 13, 27, 28, 35, 43, 57, 65, 69 
        riskCards = 15, 19, 26, 30, 31, 33, 34, 40, 45, 46, 47, 50, 54, 55
        screen.blit(cardBg, (0,0))
        screen.blit(alertbox2, (100, 525))
        screen.blit(alertbox3, (100, 590))
        screen.blit(prevImg, (1100, 0))
        screen.blit(risk, (88,440))

        

        events = pygame.event.get()  # this will return a que of events
        running = True 
        while running:  
            events = pygame.event.get()  
            for event in events: 
                if index >= 1 and index:
                        screen.blit(cardLArray[index], (100,100))  
                        screen.blit(cardRArray[index], (435,100))   
                        screen.blit(dirArray[index], (835,100))
                if event.type == pygame.QUIT: 
                    sys.exit(0) 
                if index == 2: 
					screen.blit(alertbox, (10, 580))
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_LEFT and index > 1: 
                        index -= 1 
                        screen.blit(cardLArray[index], (100,100))  
                        screen.blit(cardRArray[index], (435,100))
                        if index in longercards: 
                        	screen.blit(next, (1000,680))
                        else: 
                        	screen.blit(cardBg, (1000,680))
                    if event.key == pygame.K_RIGHT and index < 90: 
                        index += 1 
                        screen.blit(cardLArray[index], (100,100))  
                        screen.blit(cardRArray[index], (435,100)) 
                        screen.blit(dirArray[index], (835,100))
                        if index in longercards: 
                            screen.blit(next, (1000,680))                       	
                        else: 
                        	screen.blit(cardBg, (1000,680))
                    if event.key == pygame.K_DOWN and index == 7: 
                    	screen.blit(dir7b, (835, 100)) 
                    if event.key == pygame.K_DOWN and index == 13: 
                    	screen.blit(dir13b, (835, 100)) 
                    if event.key == pygame.K_DOWN and index == 27: 
                    	screen.blit(dir27b, (835, 100)) 
                    if event.key == pygame.K_DOWN and index == 28: 
                    	screen.blit(dir28b, (835, 100)) 
                    if event.key == pygame.K_DOWN and index == 35: 
                    	screen.blit(dir35b, (835, 100)) 
                    if event.key == pygame.K_DOWN and index == 43: 
                    	screen.blit(dir43b, (835, 100)) 
                    if event.key == pygame.K_DOWN and index == 57: 
                    	screen.blit(dir57b, (835, 100)) 
                    if event.key == pygame.K_DOWN and index == 65: 
                    	screen.blit(dir65b, (835, 100)) 
                    if event.key == pygame.K_DOWN and index == 69: 
                    	screen.blit(dir69b, (835, 100)) 

                
                if index in riskCards: 
           	 		screen.blit(alertbox, (100, 460))
           	 		screen.blit(risk, (88,440))
				





                mouseposition = pygame.mouse.get_pos()  
                mousepressed = pygame.mouse.get_pressed()
                if self.riskBox.collidepoint(mouseposition) and mousepressed[0] == 1: 
                    screen.blit(cardBg, (0,0)) 
                    self.display_risk(index)
                if self.backBox.collidepoint(mouseposition) and mousepressed[0] == 1: 
                    self.menu(index)
                # if self.nextBox.collidepoint(mouseposition) and mousepressed[0] == 1: 
                # 	print 'c'
            pygame.display.update()

#orientation stuff 


    

    def personal_context(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #all text found in files in script folder
        script = open("scripts/script.txt", "r")
        script1 = open("scripts/script1.txt", "r")
        script2 = open("scripts/script2.txt", "r")
        script3 = open("scripts/script3.txt", "r")
        script4 = open("scripts/script4.txt", "r")
        script5 = open("scripts/script5.txt", "r")
        script6 = open("scripts/script6.txt", "r")
        script7 = open("scripts/script7.txt", "r")
        script8 = open("scripts/script8.txt", "r")
        script9 = open("scripts/script9.txt", "r")
        script10 = open("scripts/script10.txt", "r")
        script11 = open("scripts/script11.txt", "r")
        script12 = open("scripts/script12.txt", "r")
        #renders the text
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script1.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script2.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script3.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script4.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script5.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script6.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script7.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script8.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script9.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script10.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script11.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script12.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        
        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()
                        
    def lineups_casting1(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #all text found in files in script folder
        script13 = open("scripts/script13.txt", "r")
        script14 = open("scripts/script14.txt", "r")
        script15 = open("scripts/script15.txt", "r")
        script16 = open("scripts/script16.txt", "r")
        script17 = open("scripts/script17.txt", "r")
        script18 = open("scripts/script18.txt", "r")
        script19 = open("scripts/script19.txt", "r")
        script20 = open("scripts/script20.txt", "r")
        script21 = open("scripts/script21.txt", "r")
        script22 = open("scripts/script22.txt", "r")
        script23 = open("scripts/script23.txt", "r")
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script13.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script14.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script15.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script16.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script17.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script18.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script19.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script20.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script21.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script22.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script23.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        

        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()
        

    def lineups_casting2(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #all text found in files in script folder
        script25 = open("scripts/script25.txt", "r")
        script26 = open("scripts/script26.txt", "r")
        script27 = open("scripts/script27.txt", "r")
        script28 = open("scripts/script28.txt", "r")
        script29 = open("scripts/script29.txt", "r")
        script30 = open("scripts/script30.txt", "r")
        script31 = open("scripts/script31.txt", "r")
        script32 = open("scripts/script32.txt", "r")
        script33 = open("scripts/script33.txt", "r")
        script34 = open("scripts/script34.txt", "r")
        script35 = open("scripts/script35.txt", "r")
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script25.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script26.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script27.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script28.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script29.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script30.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script31.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script32.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script33.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script34.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script35.read()
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
        
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #all text found in files in script folder
        script36 = open("scripts/script36.txt", "r")
        script37 = open("scripts/script37.txt", "r")
        script38 = open("scripts/script38.txt", "r")
        script39 = open("scripts/script39.txt", "r")
        script40 = open("scripts/script40.txt", "r")
        script41 = open("scripts/script41.txt", "r")
        script42 = open("scripts/script42.txt", "r")
        script43 = open("scripts/script43.txt", "r")
        script44 = open("scripts/script44.txt", "r")
        script45 = open("scripts/script45.txt", "r")
        script46 = open("scripts/script46.txt", "r")
        script47 = open("scripts/script47.txt", "r")
        script48 = open("scripts/script48.txt", "r")
        script49 = open("scripts/script49.txt", "r")
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script36.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script37.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script38.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script39.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script40.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script41.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script42.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script43.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script44.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script45.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script46.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script47.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script48.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script49.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,520))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        

        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()
        

    def lineups_casting4(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #all text found in files in script folder
        script50 = open("scripts/script50.txt", "r")
        script51 = open("scripts/script51.txt", "r")
        script52 = open("scripts/script52.txt", "r")
        script53 = open("scripts/script53.txt", "r")
        script54 = open("scripts/script54.txt", "r")
        script55 = open("scripts/script55.txt", "r")
        script56 = open("scripts/script56.txt", "r")
        script57 = open("scripts/script57.txt", "r")
        script58 = open("scripts/script58.txt", "r")
        script59 = open("scripts/script59.txt", "r")
        script60 = open("scripts/script60.txt", "r")
        script61 = open("scripts/script61.txt", "r")
        script62 = open("scripts/script62.txt", "r")
        script63 = open("scripts/script63.txt", "r")
        script64 = open("scripts/script64.txt", "r")
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script50.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script51.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script52.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script53.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script54.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script55.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script56.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script57.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script58.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script59.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script60.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script61.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script62.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script63.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,520))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script64.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,550))

        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()

    def lineups_casting5(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #all text found in files in script folder
        script65 = open("scripts/script65.txt", "r")
        script66 = open("scripts/script66.txt", "r")
        script67 = open("scripts/script67.txt", "r")
        script68 = open("scripts/script68.txt", "r")
        script69 = open("scripts/script69.txt", "r")
        script70 = open("scripts/script70.txt", "r")
        
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script65.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script66.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script67.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script68.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script69.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script70.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        

        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()
        

    def lineups_casting6(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
            
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #all text found in files in script folder
        script71 = open("scripts/script71.txt", "r")
        script72 = open("scripts/script72.txt", "r")
        script73 = open("scripts/script73.txt", "r")
        script74 = open("scripts/script74.txt", "r")
        script75 = open("scripts/script75.txt", "r")
        script76 = open("scripts/script76.txt", "r")
        script77 = open("scripts/script77.txt", "r")
        script78 = open("scripts/script78.txt", "r")
        script79 = open("scripts/script79.txt", "r")
        script80 = open("scripts/script80.txt", "r")
        script81 = open("scripts/script81.txt", "r")
        script82 = open("scripts/script82.txt", "r")
        script83 = open("scripts/script83.txt", "r")
        script84 = open("scripts/script84.txt", "r")
        script85 = open("scripts/script85.txt", "r")
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script71.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script72.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script73.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script74.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script75.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script76.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script77.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script78.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script79.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script80.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script81.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script82.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script83.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script84.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,520))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script85.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,550))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 20)
        

        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()
        

    def lineups_casting7(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #all text found in files in script folder
        script86 = open("scripts/script86.txt", "r")
        script87 = open("scripts/script87.txt", "r")
        script88 = open("scripts/script88.txt", "r")
        script89 = open("scripts/script89.txt", "r")
        script90 = open("scripts/script90.txt", "r")
        script91 = open("scripts/script91.txt", "r")
        script92 = open("scripts/script92.txt", "r")
        script93 = open("scripts/script93.txt", "r")
        script94 = open("scripts/script94.txt", "r")
        script95 = open("scripts/script95.txt", "r")
        script96 = open("scripts/script96.txt", "r")
        script97 = open("scripts/script97.txt", "r")
        script98 = open("scripts/script98.txt", "r")
        script99 = open("scripts/script99.txt", "r")
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script86.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script87.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script88.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script89.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script90.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script91.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script92.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script93.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script94.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script95.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script96.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script97.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script98.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script99.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,520))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        

        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()
        
    def lineups_casting8(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #all text found in files in script folder
        script100 = open("scripts/script100.txt", "r")
        script101 = open("scripts/script101.txt", "r")
        script102 = open("scripts/script102.txt", "r")
        script103 = open("scripts/script103.txt", "r")
        script104 = open("scripts/script104.txt", "r")
        script105 = open("scripts/script105.txt", "r")
        script106 = open("scripts/script106.txt", "r")
        script107 = open("scripts/script107.txt", "r")
        script108 = open("scripts/script108.txt", "r")
        script109 = open("scripts/script109.txt", "r")
        script110 = open("scripts/script110.txt", "r")
        script111 = open("scripts/script111.txt", "r")
        
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script100.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script101.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script102.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script103.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script104.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script105.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script106.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script107.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script108.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script109.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script110.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script111.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        

        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()
        


    def lineups_casting9(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #all text found in files in script folder
        script112 = open("scripts/script112.txt", "r")
        script113 = open("scripts/script113.txt", "r")
        script114 = open("scripts/script114.txt", "r")
        script115 = open("scripts/script115.txt", "r")
        script116 = open("scripts/script116.txt", "r")
        script117 = open("scripts/script117.txt", "r")
        script118 = open("scripts/script118.txt", "r")
        script119=  open("scripts/script119.txt", "r")
        script120 = open("scripts/script120.txt", "r")
        script121 = open("scripts/script121.txt", "r")
        script122 = open("scripts/script122.txt", "r")
        script123 = open("scripts/script123.txt", "r")
        script124 = open("scripts/script124.txt", "r")
        script125=  open("scripts/script125.txt", "r")
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script112.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script113.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script114.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script115.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script116.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script117.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script118.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script119.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script120.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script121.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script122.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script123.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script124.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script125.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,520))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        

        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()
        

    def lineups_casting10(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #all text found in files in script folder
        script126 = open("scripts/script126.txt", "r")
        script127 = open("scripts/script127.txt", "r")
        script128 = open("scripts/script128.txt", "r")
        script129 = open("scripts/script129.txt", "r")
        script130 = open("scripts/script130.txt", "r")
        script131 = open("scripts/script131.txt", "r")
        script132 = open("scripts/script132.txt", "r")
        script133 = open("scripts/script133.txt", "r")
        script134 = open("scripts/script134.txt", "r")
        script135 = open("scripts/script135.txt", "r")
        script136 = open("scripts/script136.txt", "r")
        script137 = open("scripts/script137.txt", "r")
        script138 = open("scripts/script138.txt", "r")
        script139 = open("scripts/script139.txt", "r")
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script126.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script127.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script128.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script129.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script130.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script131.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script132.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script133.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script134.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script135.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script136.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script137.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script138.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script139.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,520))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        

        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()
        


    def lineups_casting11(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
            
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #all text found in files in script folder
        script140 = open("scripts/script140.txt", "r")
        script141 = open("scripts/script141.txt", "r")
        script142 = open("scripts/script142.txt", "r")
        script143 = open("scripts/script143.txt", "r")
        script144 = open("scripts/script144.txt", "r")
        script145 = open("scripts/script145.txt", "r")
        script146 = open("scripts/script146.txt", "r")
        script147 = open("scripts/script147.txt", "r")
        script148 = open("scripts/script148.txt", "r")
        script149 = open("scripts/script149.txt", "r")
        script150 = open("scripts/script150.txt", "r")
        script151 = open("scripts/script151.txt", "r")
        script152 = open("scripts/script152.txt", "r")
        script153 = open("scripts/script153.txt", "r")
        script154 = open("scripts/script154.txt", "r")
        script155 = open("scripts/script155.txt", "r")
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script140.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script141.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script142.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script143.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script144.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script145.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script146.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script147.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script148.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script149.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script150.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script151.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script152.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script153.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,520))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script154.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,550))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script155.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,580))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        

        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()
        


    def lineups_casting12(self): 
        self.backgroundColor = pygame.Rect(0, 0, 1200, 700)
        pygame.draw.rect(screen, (0,0,128), self.backgroundColor)
        screen.blit(background, (0,-100))
        
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 90)
        #all text found in files in script folder
        script156 = open("scripts/script156.txt", "r")
        script157 = open("scripts/script157.txt", "r")
        script158 = open("scripts/script158.txt", "r")
        script159 = open("scripts/script159.txt", "r")
        script160 = open("scripts/script160.txt", "r")
        script161 = open("scripts/script161.txt", "r")
        script162 = open("scripts/script162.txt", "r")
        script163 = open("scripts/script163.txt", "r")
        script164 = open("scripts/script164.txt", "r")
        script165 = open("scripts/script165.txt", "r")
        script166 = open("scripts/script166.txt", "r")
        script167 = open("scripts/script167.txt", "r")
        script168 = open("scripts/script168.txt", "r")
        script169 = open("scripts/script169.txt", "r")
        
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script156.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,130))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script157.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,160))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script158.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,190))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script159.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,220))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script160.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,250))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script161.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,280))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script162.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,310))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script163.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,340))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script164.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,370))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script165.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,400))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script166.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,430))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script167.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,460))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script168.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,490))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        self.instructiontext = script169.read()
        self.instructionren = self.instructionfont.render(self.instructiontext,30,self.instructionfontcolor)
        screen.blit(self.instructionren,(180,520))
        self.instructionfontcolor = (255,255,255)
        self.instructionfont = pygame.font.SysFont('comicsansms', 15)
        

        mousepressed = pygame.mouse.get_pressed() 
        mouseposition = pygame.mouse.get_pos()

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

    def playInstructions(self):
        info_array = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
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
                    if event.key == pygame.K_RIGHT and instruction_index < len(info_array):
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
 
    def menu(self, index): 
        screen.blit(backgroundImg, (0,0))
        screen.blit(logoTextImg, (400,10))
        screen.blit(instructionImg, (185,640)) 
        screen.blit(playImg, (785,640)) 

        running = True 
        while running:  
            mouseposition = pygame.mouse.get_pos()  
            mousepressed = pygame.mouse.get_pressed()
            if self.instructionBox.collidepoint(mouseposition) and mousepressed[0] == 1:
                self.playInstructions()
            if self.playBox.collidepoint(mouseposition) and mousepressed[0] == 1:
                self.playGame(index)
    
            # --- Limit to 60 frames per second
            clock.tick(60)

            events = pygame.event.get()  
            for event in events: 
                if event.type == pygame.QUIT: 
                    sys.exit(0) 

            pygame.display.update() 

Menu().menu(1) # runs the menu of the page 