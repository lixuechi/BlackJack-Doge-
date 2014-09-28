# Blackjack
# author: Xuechi Li

import pygame, sys, random
import math
from pygame.locals import *

# constant variables here
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
POWDERBLUE = (176, 224, 230)
PALEGREEN = (152, 251, 152)
TAN = (210, 180, 140)
SALMON = (250, 128, 114)
FPS = 30
WIDTH = 600
HEIGHT = 400
cardpileX = 170
cardpileY = 110
cardpileWidth = 60
cardpileHeight = 80
cardWidth = 30
cardHeight = 40
# show the sum of points:
playerSumCoords = (30, 300)
computerSumCoords = (30, 20)
# card positions:
# (30, 30) (80, 30)  (130, 30)
# (30, 320)  (80, 320)  (130, 320)
CC1 = (30, 40)  # computer coordinates for placing cards
CC2 = (80, 40)
CC3 = (130, 40)
CC4 = (180, 40)
CC5 = (230, 40)
HC1 = (30, 320)  # human coordinates for placing cards
HC2 = (80, 320)
HC3 = (130, 320)
HC4 = (180, 320)
HC5 = (230, 320)



def main():
    # global variables here
    global DISPLAYSURF, symbolImg, symbol1Img, symbol2Img, symbol3Img, symbol4Img, numOfYOUWin, numOfIWin, humanCardBoolList, computerCardBoolList, fpsClock, dogeImg, cardpileImg, cardbackImg, clubAImg, club2Img, club3Img, club4Img, club5Img, club6Img, club7Img, club8Img, club9Img, club10Img, clubJImg, clubQImg, clubKImg, diamondAImg, diamond2Img, diamond3Img, diamond4Img, diamond5Img, diamond6Img, diamond7Img, diamond8Img, diamond9Img, diamond10Img, diamondJImg, diamondKImg, diamondQImg, heartAImg, heart2Img, heart3Img, heart4Img, heart5Img, heart6Img, heart7Img, heart8Img, heart9Img, heart10Img, heartJImg, heartKImg, heartQImg, spadeAImg, spade2Img, spade3Img, spade4Img, spade5Img, spade6Img, spade7Img, spade8Img, spade9Img, spade10Img, spadeJImg, spadeQImg, spadeKImg

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('*21*')
    fpsClock = pygame.time.Clock()

    #card imgs
    cardpileImg = pygame.image.load('cardpile.png')
    cardbackImg = pygame.image.load('cardback.png')
    dogeImg = pygame.image.load('cardbackSmall.png')
    clubAImg = pygame.image.load('clubA.jpg')     #value 1/11; label 1
    club2Img = pygame.image.load('club2.jpg')     #value 2 ; label 2 
    club3Img = pygame.image.load('club3.jpg')     #value 3 ; label 3
    club4Img = pygame.image.load('club4.jpg')     #value 4 ; label 4
    club5Img = pygame.image.load('club5.jpg')     #value 5 ; label 5
    club6Img = pygame.image.load('club6.jpg')     #value 6 ; label 6
    club7Img = pygame.image.load('club7.jpg')     #value 7 ; label 7
    club8Img = pygame.image.load('club8.jpg')     #value 8 ; label 8
    club9Img = pygame.image.load('club9.jpg')     #value 9 ; label 9
    club10Img = pygame.image.load('club10.jpg')     #value 10 ; label 10
    clubJImg = pygame.image.load('clubJ.jpg')     #value 10 ; label 11
    clubKImg = pygame.image.load('clubK.jpg')     #value 10 ; label 12
    clubQImg = pygame.image.load('clubQ.jpg')     #value 10 ; label 13
    diamondAImg = pygame.image.load('diamondA.jpg')     #value 1/11; label 14
    diamond2Img = pygame.image.load('diamond2.jpg')     #value 2 ; label 15 
    diamond3Img = pygame.image.load('diamond3.jpg')     #value 3 ; label 16
    diamond4Img = pygame.image.load('diamond4.jpg')     #value 4 ; label 17
    diamond5Img = pygame.image.load('diamond5.jpg')     #value 5 ; label 18
    diamond6Img = pygame.image.load('diamond6.jpg')     #value 6 ; label 19
    diamond7Img = pygame.image.load('diamond7.jpg')     #value 7 ; label 20
    diamond8Img = pygame.image.load('diamond8.jpg')     #value 8 ; label 21
    diamond9Img = pygame.image.load('diamond9.jpg')     #value 9 ; label 22
    diamond10Img = pygame.image.load('diamond10.jpg')     #value 10 ; label 23
    diamondJImg = pygame.image.load('diamondJ.jpg')     #value 10 ; label 24
    diamondKImg = pygame.image.load('diamondK.jpg')     #value 10 ; label 25
    diamondQImg = pygame.image.load('diamondQ.jpg')     #value 10 ; label 26
    heartAImg = pygame.image.load('heartA.jpg')     #value 1/11; label 27
    heart2Img = pygame.image.load('heart2.jpg')     #value 2 ; label 28 
    heart3Img = pygame.image.load('heart3.jpg')     #value 3 ; label 29
    heart4Img = pygame.image.load('heart4.jpg')     #value 4 ; label 30
    heart5Img = pygame.image.load('heart5.jpg')     #value 5 ; label 31
    heart6Img = pygame.image.load('heart6.jpg')     #value 6 ; label 32
    heart7Img = pygame.image.load('heart7.jpg')     #value 7 ; label 33
    heart8Img = pygame.image.load('heart8.jpg')     #value 8 ; label 34
    heart9Img = pygame.image.load('heart9.jpg')     #value 9 ; label 35
    heart10Img = pygame.image.load('heart10.jpg')     #value 10 ; label 36
    heartJImg = pygame.image.load('heartJ.jpg')     #value 10 ; label 37
    heartKImg = pygame.image.load('heartK.jpg')     #value 10 ; label 38
    heartQImg = pygame.image.load('heartQ.jpg')     #value 10 ; label 39
    spadeAImg = pygame.image.load('spadeA.jpg')     #value 1/11; label 40
    spade2Img = pygame.image.load('spade2.jpg')     #value 2 ; label 41 
    spade3Img = pygame.image.load('spade3.jpg')     #value 3 ; label 42
    spade4Img = pygame.image.load('spade4.jpg')     #value 4 ; label 43
    spade5Img = pygame.image.load('spade5.jpg')     #value 5 ; label 44
    spade6Img = pygame.image.load('spade6.jpg')     #value 6 ; label 45
    spade7Img = pygame.image.load('spade7.jpg')     #value 7 ; label 46
    spade8Img = pygame.image.load('spade8.jpg')     #value 8 ; label 47
    spade9Img = pygame.image.load('spade9.jpg')     #value 9 ; label 48
    spade10Img = pygame.image.load('spade10.jpg')     #value 10 ; label 49
    spadeJImg = pygame.image.load('spadeJ.jpg')     #value 10 ; label 50
    spadeKImg = pygame.image.load('spadeK.jpg')     #value 10 ; label 51
    spadeQImg = pygame.image.load('spadeQ.jpg')     #value 10 ; label 52

    symbolImg = pygame.image.load('symbol.png')
    symbol1Img = pygame.image.load('symbol1.png')
    symbol2Img = pygame.image.load('symbol2.png')
    symbol3Img = pygame.image.load('symbol3.png')
    symbol4Img = pygame.image.load('symbol4.png')

    # arrays storing humanCardBool AND computerCardBool values
    humanCardBool1 = False
    humanCardBool2 = False
    humanCardBool3 = False
    humanCardBool4 = False
    humanCardBool5 = False
    computerCardBool1 = False
    computerCardBool2 = False
    computerCardBool3 = False
    computerCardBool4 = False
    computerCardBool5 = False
    humanCardBoolList = [humanCardBool1, humanCardBool2, humanCardBool3, humanCardBool4, humanCardBool5]
    computerCardBoolList = [computerCardBool1, computerCardBool2, computerCardBool3, computerCardBool4, computerCardBool5]

##    # the number of times when the player wins
##    numOfYOUWin = 0
##    # the number of times when the computer wins
##    numOfIWin = 0
        

    while True:
        runGame()



def gameOver():
    pygame.quit()
    sys.exit()


def runGame():

    # initialize boolean values
    pickCard = False
    dropCard = False
    mouseButtonDown = False
    mouseButtonUp = False
    mouseClicked = False

    humanCardBoolList[0] = False
    humanCardBoolList[1] = False
    humanCardBoolList[2] = False
    humanCardBoolList[3] = False
    humanCardBoolList[4] = False
    computerCardBoolList[0] = False
    computerCardBoolList[1] = False
    computerCardBoolList[2] = False
    computerCardBoolList[3] = False
    computerCardBoolList[4] = False

    # initialize card values for the player and the enemy
    humanCardValue1 = 0
    humanCardValue2 = 0
    humanCardValue3 = 0
    humanCardValue4 = 0
    humanCardValue5 = 0

    computerCardValue1 = 0
    computerCardValue2 = 0
    computerCardValue3 = 0
    computerCardValue4 = 0
    computerCardValue5 = 0
    

    gambleOn = False
    showShuffleButton = True
    showDealButton = True
    showHitButton = False
    showStandButton = False
    freeGambleOn = False
    showYouBustedText = False
    showRegambleButton = False
    showLetMePlayButton = False

    hitOn = False
    standOn = False
    regamble = False
    lmp = False # let me play

    showComputerValue = False
    finish = False

    computerWin = False
    playerWin = False
    tie = False

    changeCounter = True
    playerBusted = False

    # determine if the player is playing or the machine is playing
    youMode = True # when the player is playing
    iMode = False # when letMePlay is being processed
   

    # treat those two as pointers that point to the next element
    CCBL_INDEX = 2 # the initial index of computerCardBoolList
    HCBL_INDEX = 2 # the initial index of humanCardBoolList

    mouseX, mouseY = (0, 0)
    cardX, cardY = (0, 0)

    TOPINDEX = 12 # 13 cards in total, the index of the card on top of cardpile 


    # labeling for cards (13 in total)
    # A:1; 2-9:2-9; 10:10; J:11; K:12; Q:13

    cardPile = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

    while True: # main game loop
        DISPLAYSURF.fill(PALEGREEN)
        DISPLAYSURF.blit(cardpileImg, (cardpileX, cardpileY))

        # showGameResult(numOfYOUWin, numOfIWin)

        # draw button "Shuffle"
        if showShuffleButton:
            drawButtonShuffle()
        # draw button "Deal"
        if showDealButton:
            drawButtonDeal()
        # draw button "Hit"
        if showHitButton:
            drawButtonHit()
        # draw button "Stand"
        if showStandButton:
            drawButtonStand()
        # draw button "Regamble"
        if showRegambleButton:
            drawButtonRegamble()
        # draw button "Let me play"
        if showLetMePlayButton:
            drawButtonLetMePlay()


   	# draw lines
        pygame.draw.line(DISPLAYSURF, BLACK, [0, 110], [600, 110], 2)
        pygame.draw.line(DISPLAYSURF, BLACK, [0, 275], [600, 275], 2)
##

##        # draw Rect
##        cardpileRect = pygame.Rect(cardpileX, cardpileY, cardpileWidth, cardpileHeight)
##        if cardpileRect.collidepoint(mouseX, mouseY) and mouseButtonDown:
##            pickCard = True
##
##        if pickCard and mouseButtonDown:
##            DISPLAYSURF.blit(cardbackImg, (mouseX - cardWidth/2, mouseY - cardHeight/2))
##
##        if pickCard and mouseButtonUp:
##            DISPLAYSURF.blit(cardbackImg, (mouseX - cardWidth/2, mouseY - cardHeight/2))
##            pickCard = False
##            mouseButtonUp = False
##            dropCard = True
##            cardX, cardY = (mouseX - cardWidth/2, mouseY - cardHeight/2)
##
##        if dropCard:
##            DISPLAYSURF.blit(cardbackImg, (cardX, cardY))

        if showShuffleButton:
            shuffleRect = pygame.Rect(385, 175, 70, 30)
            if shuffleRect.collidepoint(mouseX, mouseY):
                drawHighlightBox(385, 175, 70, 30, BLACK)
                if mouseClicked:
                    # shuffle, mess around cardPile
                    counter = 0
                    newCardPile = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    while counter < 52:
                        i = random.randint(0, 51)
                        if cardPile[i] != -1:
                            newCardPile[counter] = cardPile[i]
                            cardPile[i] = -1
                            counter += 1
                    cardPile = newCardPile
                    # for testing purpose
                    print cardPile[0]
                    showShuffleAnime()

        if showDealButton:
            dealRect = pygame.Rect(385, 225, 70, 30)
            if dealRect.collidepoint(mouseX, mouseY):
                drawHighlightBox(395, 225, 50, 30, BLACK)
                if mouseClicked:
                    # start, 2 cards for each
                    # gamble on!
                    # treat the cardpile list as a stack
                    # - the last item of the list is on the top of the stack
                    gambleOn = True
                    showShuffleButton = False
                    showDealButton = False

        if showHitButton:
            hitRect = pygame.Rect(405, 325, 30, 30)
            if hitRect.collidepoint(mouseX, mouseY):
                drawHighlightBox(405, 325, 30, 30, BLACK)
                if mouseClicked:
                    # hit!
                    hitOn = True

        
        if showStandButton:
            standRect = pygame.Rect(460, 325, 70, 30)
            if standRect.collidepoint(mouseX, mouseY):
                drawHighlightBox(460, 325, 60, 30, BLACK)
                if mouseClicked:
                    # stand!
                    standOn = True


        if showRegambleButton:
            regambleRect = pygame.Rect(20, 172, 102, 35)
            if regambleRect.collidepoint(mouseX, mouseY):
                drawHighlightBox(20, 172, 102, 35, BLACK)
                if mouseClicked:
                    # regamble~
                    regamble = True


        if showLetMePlayButton:
            lmpRect = pygame.Rect(12, 215, 118, 30)
            if lmpRect.collidepoint(mouseX, mouseY):
                drawHighlightBox(12, 215, 118, 30, BLACK)
                if mouseClicked:
                    # let the computer play for you
                    lmp = True
                    
                    

        # change 'gambleOn' to 'dealOn'
        if gambleOn:
            # from here, the TOPINDEX should be 51, so no further assertions

            # before starting, TOPINDEX should be asserted no less than 0
            #if TOPINDEX < 0:
            #    print 'There\'s no card available anymore.'
                # write an alert text here
            #else:
            humanCardBoolList[0] = True
            humanCardVal1 = cardPile[TOPINDEX]
            humanCardValue1 = identifyValue(humanCardVal1)
            TOPINDEX -= 1
            
            computerCardBoolList[0] = True
            computerCardVal1 = cardPile[TOPINDEX]
            computerCardValue1 = identifyValue(computerCardVal1) 
            TOPINDEX -= 1
            
            humanCardBoolList[1] = True
            humanCardVal2 = cardPile[TOPINDEX]
            humanCardValue2 = identifyValue(humanCardVal2)
            TOPINDEX -= 1

            computerCardBoolList[1] = True
            computerCardVal2 = cardPile[TOPINDEX]
            computerCardValue2 = identifyValue(computerCardVal2)
            TOPINDEX -= 1

            humanCardVal3 = cardPile[TOPINDEX]
            TOPINDEX -= 1
##            humanCardValue3 = identifyValue(humanCardVal3)

            humanCardVal4 = cardPile[TOPINDEX]
            TOPINDEX -= 1
##            humanCardValue4 = identifyValue(humanCardVal4)
##            humanCardValue4 = 0

            humanCardVal5 = cardPile[TOPINDEX]
            TOPINDEX -= 1
##            humanCardValue5 = identifyValue(humanCardVal5)
            #humanCardValue5 = 0

            computerCardVal3 = cardPile[TOPINDEX]
            TOPINDEX -= 1
##            computerCardValue3 = identifyValue(computerCardVal3)
            #computerCardValue3 = 0

            computerCardVal4 = cardPile[TOPINDEX]
            TOPINDEX -= 1
##            computerCardValue4 = identifyValue(computerCardVal4)
            #computerCardValue4 = 0

            computerCardVal5 = cardPile[TOPINDEX]
            TOPINDEX -= 1
##            computerCardValue5 = identifyValue(computerCardVal5)
            #computerCardValue5 = 0

            # both of them now point to computerCardBool3 
            #HCBL_INDEX = 2
            #CCBL_INDEX = 2

            humanCardValue3 = 0
            # toggle on Hit and Stand
            showHitButton = True
            showStandButton = True
            # toggle off gambleOn
            gambleOn = False
            freeGambleOn = True

        # assert TOPINDEX < 52
        if TOPINDEX < 52:
            if humanCardBoolList[0]:
                identifyCard(humanCardVal1, HC1)
            if humanCardBoolList[1]:
                identifyCard(humanCardVal2, HC2)
            if humanCardBoolList[2]:
##                humanCardVal3 = cardPile[TOPINDEX]
##                TOPINDEX -= 1
                humanCardValue3 = identifyValue(humanCardVal3)
                identifyCard(humanCardVal3, HC3)
            if humanCardBoolList[3]:
##                humanCardVal4 = cardPile[TOPINDEX]
##                TOPINDEX -= 1
                humanCardValue4 = identifyValue(humanCardVal4)
                identifyCard(humanCardVal4, HC4)
            if humanCardBoolList[4]:
##                humanCardVal5 = cardPile[TOPINDEX]
##                TOPINDEX -= 1
                humanCardValue5 = identifyValue(humanCardVal5)
                identifyCard(humanCardVal5, HC5)
            if computerCardBoolList[0]:
                identifyCard(computerCardVal1, CC1)
                # only show the back of the card
                DISPLAYSURF.blit(dogeImg, CC1)
            if computerCardBoolList[1]:
                identifyCard(computerCardVal2, CC2)
            if computerCardBoolList[2]:
##                computerCardVal3 = cardPile[TOPINDEX]
##                TOPINDEX -= 1
                computerCardValue3 = identifyValue(computerCardVal3)
                identifyCard(computerCardVal3, CC3)
            if computerCardBoolList[3]:
##                computerCardVal4 = cardPile[TOPINDEX]
##                TOPINDEX -= 1
                computerCardValue4 = identifyValue(computerCardVal4)
                identifyCard(computerCardVal4, CC4)
            if computerCardBoolList[4]:
##                computerCardVal5 = cardPile[TOPINDEX]
##                TOPINDEX -= 1
                computerCardValue5 = identifyValue(computerCardVal5)
                identifyCard(computerCardVal5, CC5)

        
        # Hit on!
        if hitOn:
            # pick the top card from the card pile to the player

            # assert TOPINDEX >= 0:
            #if TOPINDEX < 0:
            #    print 'There\'s no card available anymore.'
                # write that alert here aussi
            #else:
            if HCBL_INDEX <= 4:
                HCBL_INDEX = 2
                humanCardBoolList[HCBL_INDEX] = True
##                humanCardVal3 = cardPile[TOPINDEX]
##                humanCardValue3 = identifyValue(humanCardVal3)
                #HCBL_INDEX += 1
            else:
                HCBL_INDEX = 4
            hitOn = False


        # standOn
        if standOn:
            # the player's card now freezes
            # the computer starts to take cards

            # disenable showing hit button and stand button
            showStandButton = False
            showHitButton = False
            
            # show the first card
            
            if computerSum < 18:
                # continues taking cards from the cardpile
                # an array storing computerCardBool values
                CCBL_INDEX = 2
                computerCardBoolList[CCBL_INDEX] = True
                computerSum += computerCardValue3
##                if computerSum + computerCardValue3 < 18:
##                    CCBL_INDEX = 3
##                    computerCardBoolList[CCBL_INDEX] = True
            finish = True


        # finish == True
        if finish:
            if youMode:
                showComputerValue = True
                if computerSum > 21:
                    # player won
                    playerWin = True
                else:
                    # computerSum < 21;
                    # playerSum < 21;
                    if computerSum > playerSum:
                        # computer won
                        computerWin = True
                    elif playerSum > computerSum:
                        # player won
                        #numOfYOUWin += 1
                        playerWin = True
                    elif playerSum == computerSum:
                        # tie
                        tie = True
                showRegambleButton = True
                if youMode:
                    showLetMePlayButton = True
                finish = False
            if iMode:
                showComputerValue = True
                if computerSum > 21:
                    # player won
                    playerWin = True
                else:
                    # computerSum < 21;
                    # playerSum < 21;
                    if computerSum > (humanCardValue1 + humanCardValue2 + humanCardValue3):
                        # computer won
                        computerWin = True
                    elif (humanCardValue1 + humanCardValue2 + humanCardValue3) > computerSum:
                        # player won
                        #numOfYOUWin += 1
                        playerWin = True
                    elif (humanCardValue1 + humanCardValue2 + humanCardValue3) == computerSum:
                        # tie
                        tie = True
                showRegambleButton = True
                if youMode:
                    showLetMePlayButton = True
                finish = False


        if computerWin:
            if youMode:
                showComputerWin('You lose')
            elif iMode:
                showComputerWin(' I lose ')
        if playerWin:
            if youMode:
                showPlayerWin('You win')
            elif iMode:
                showPlayerWin(' I win ')
##            if changeCounter:  # just to forbidden looping increment of the counter
##                numOfYOUWin = incrementNumOfYOUWin(numOfYOUWin)
##                changeCounter = False
##                # this boolean value should be initialized as True each time
##                #      the user runs runGame()  
        if tie:
            showTie()
            # remember to show the first card of the computer
        

        if freeGambleOn:
            playerSum = 0
            computerSum = 0
            playerSum = humanCardValue1 + humanCardValue2 + humanCardValue3 + humanCardValue4 + humanCardValue5
            computerSum = computerCardValue1 + computerCardValue2 + computerCardValue3 + computerCardValue4 + computerCardValue5
            if showComputerValue:                
                showSumOfPoints(str(computerSum), computerSumCoords)
            if youMode:
                showSumOfPoints(str(playerSum), playerSumCoords)
            elif iMode and (humanCardValue1 + humanCardValue2) > 13:
                showSumOfPoints(str((humanCardValue1 + humanCardValue2)), playerSumCoords)
            elif iMode and (humanCardValue1 + humanCardValue2) < 13:
                showSumOfPoints(str((humanCardValue1 + humanCardValue2 + humanCardValue3)), playerSumCoords)
            if iMode:
                if (humanCardValue1 + humanCardValue2) > 13 and (humanCardValue1 + humanCardValue2) < 21:
                    # STAND
                    hitOn = False
                    standOn = True
                    gambleOn = False
                    #showMyMove('stand')
                elif (humanCardValue1 + humanCardValue2 + humanCardValue3) >= 21:
                    # busted
                    showYouBusted(' I busted ')
                    showLetMePlayButton = False
                    showRegambleButton = True
                else:
                    hitOn = True
                    gambleOn = False
                    #showMyMove('hit')
            
            # if busted
            if int(playerSum) > 21 and youMode:
                finish = True
                if youMode:
                    showYouBusted('You busted')
                    showLetMePlayButton = True
                    playerBusted = True
                # game over mode
                #gameOver()
                showHitButton = False
                showStandButton = False
                showRegambleButton = True
                drawButtonRegamble()
                showLetMePlayButton = True

        # if regamble
        if regamble:
            runGame()


        # if finished, let the computer show how it would have done
        if lmp:
            # change the mode to iMode
            iMode = True
            youMode = False
            finish = True
            # initialize the playerSum to the value in its former state
            if playerBusted:
                # if player busted, erase the 3rd card
                humanCardBoolList[2] = False
                playerSum -= humanCardValue3
                showSumOfPoints(str(playerSum), playerSumCoords)
                if playerSum - humanCardValue3 > 13:
                    standOn = True
                    hitOn = False
                else:
                    hitOn = True
                    standOn = False
            
            showRegambleButton = False
            # but regamble should be restored after "letmeplay"
            gambleOn = True
            freeGambleOn = True
            showDealButton = False
            showHitButton = False
            showStandButton = False
            #lmp = False # let me play
            #letMePlay(playerSum)
            if playerSum > 13:
                # STAND
                hitOn = False
                standOn = True
                gambleOn = False
                #showMyMove('stand')
            else:
                hitOn = True
                gambleOn = False
                #showMyMove('hit')
            
            showLetMePlayButton = False
            showRegambleButton = True

            lmp = False
        
                            

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouseButtonDown = True
                mouseClicked = True
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
                mouseButtonUp = True
                mouseButtonDown = False
                mouseClicked = False

        pygame.display.update()
        fpsClock.tick(FPS)


def drawHighlightBox(leftX, topY, boxWidth, boxHeight, color):
    left = leftX
    top = topY
    pygame.draw.rect(DISPLAYSURF, color, (left, top, boxWidth, boxHeight), 2)


def drawButtonShuffle():
    shuffleText = 'Shuffle'    
    statusFontObjS = pygame.font.Font('JOKERMAN.ttf', 20)
    textSurfaceObjS = statusFontObjS.render(shuffleText, True, BLACK, POWDERBLUE)
    textRectObjS = textSurfaceObjS.get_rect()
    textRectObjS.center = (420, 190)
    DISPLAYSURF.blit(textSurfaceObjS, textRectObjS)


def drawButtonDeal():
    dealText = 'Deal'   
    statusFontObjSt = pygame.font.Font('JOKERMAN.ttf', 20)
    textSurfaceObjSt = statusFontObjSt.render(dealText, True, BLACK, POWDERBLUE)
    textRectObjSt = textSurfaceObjSt.get_rect()
    textRectObjSt.center = (420, 240)
    DISPLAYSURF.blit(textSurfaceObjSt, textRectObjSt)


def drawButtonHit():
    hitText = 'Hit'
    statusFontObjB = pygame.font.Font('JOKERMAN.ttf', 20)
    textSurfaceObjB = statusFontObjB.render(hitText, True, BLACK, POWDERBLUE)
    textRectObjB = textSurfaceObjB.get_rect()
    textRectObjB.center = (420, 340)
    DISPLAYSURF.blit(textSurfaceObjB, textRectObjB)


def drawButtonStand():
    standText = 'Stand'
    statusFontObjSta = pygame.font.Font('JOKERMAN.ttf', 20)
    textSurfaceObjSta = statusFontObjSta.render(standText, True, BLACK, POWDERBLUE)
    textRectObjSta = textSurfaceObjSta.get_rect()
    textRectObjSta.center = (490, 340)
    DISPLAYSURF.blit(textSurfaceObjSta, textRectObjSta)


def drawButtonRegamble():
    regambleText = 'Regamble'
    statusFontObjSta = pygame.font.Font('JOKERMAN.ttf', 20)
    textSurfaceObjSta = statusFontObjSta.render(regambleText, True, BLACK, POWDERBLUE)
    textRectObjSta = textSurfaceObjSta.get_rect()
    textRectObjSta.center = (70, 190)
    DISPLAYSURF.blit(textSurfaceObjSta, textRectObjSta)


def drawButtonLetMePlay():
    lmpText = 'Let me play'
    statusFontObjSta = pygame.font.Font('JOKERMAN.ttf', 20)
    textSurfaceObjSta = statusFontObjSta.render(lmpText, True, BLACK, POWDERBLUE)
    textRectObjSta = textSurfaceObjSta.get_rect()
    textRectObjSta.center = (70, 230)
    DISPLAYSURF.blit(textSurfaceObjSta, textRectObjSta)
    

def identifyCard(label, cardPos):
    
    if label == 1:
        # A
        DISPLAYSURF.blit(clubAImg, cardPos)
    elif label == 2:
        # 2
        DISPLAYSURF.blit(club2Img, cardPos)
    elif label == 3:
        # 3
        DISPLAYSURF.blit(club3Img, cardPos)
    elif label == 4:
        # 4
        DISPLAYSURF.blit(club4Img, cardPos)
    elif label == 5:
        # 5
        DISPLAYSURF.blit(club5Img, cardPos)
    elif label == 6:
        # 6
        DISPLAYSURF.blit(club6Img, cardPos)
    elif label == 7:
        # 7
        DISPLAYSURF.blit(club7Img, cardPos)
    elif label == 8:
        # 8
        DISPLAYSURF.blit(club8Img, cardPos)
    elif label == 9:
        # 9
        DISPLAYSURF.blit(club9Img, cardPos)
    elif label == 10:
        # 10
        DISPLAYSURF.blit(club10Img, cardPos)
    elif label == 11:
        # 11
        DISPLAYSURF.blit(clubJImg, cardPos)
    elif label == 12:
        # 12
        DISPLAYSURF.blit(clubQImg, cardPos)
    elif label == 13:
        # 13
        DISPLAYSURF.blit(clubKImg, cardPos)
    elif label == 14:
        # diamondA
        DISPLAYSURF.blit(diamondAImg, cardPos)
    elif label == 15:
        # diamond2
        DISPLAYSURF.blit(diamond2Img, cardPos)
    elif label == 16:
        # diamond3
        DISPLAYSURF.blit(diamond3Img, cardPos)
    elif label == 17:
        # diamond4
        DISPLAYSURF.blit(diamond4Img, cardPos)
    elif label == 18:
        # diamond5
        DISPLAYSURF.blit(diamond5Img, cardPos)
    elif label == 19:
        # diamond6
        DISPLAYSURF.blit(diamond6Img, cardPos)
    elif label == 20:
        # diamond7
        DISPLAYSURF.blit(diamond7Img, cardPos)
    elif label == 21:
        # diamond8
        DISPLAYSURF.blit(diamond8Img, cardPos)
    elif label == 22:
        # diamond9
        DISPLAYSURF.blit(diamond9Img, cardPos)
    elif label == 23:
        # diamond10
        DISPLAYSURF.blit(diamond10Img, cardPos)
    elif label == 24:
        # diamondJ
        DISPLAYSURF.blit(diamondJImg, cardPos)
    elif label == 25:
        # diamondQ
        DISPLAYSURF.blit(diamondQImg, cardPos)
    elif label == 26:
        # DiamondK
        DISPLAYSURF.blit(diamondKImg, cardPos)
    elif label == 27:
        # heartA
        DISPLAYSURF.blit(heartAImg, cardPos)
    elif label == 28:
        # heart2
        DISPLAYSURF.blit(heart2Img, cardPos)
    elif label == 29:
        # heart3
        DISPLAYSURF.blit(heart3Img, cardPos)
    elif label == 30:
        # heart4
        DISPLAYSURF.blit(heart4Img, cardPos)
    elif label == 31:
        # heart5
        DISPLAYSURF.blit(heart5Img, cardPos)
    elif label == 32:
        # heart6
        DISPLAYSURF.blit(heart6Img, cardPos)
    elif label == 33:
        # heart7
        DISPLAYSURF.blit(heart7Img, cardPos)
    elif label == 34:
        # heart8
        DISPLAYSURF.blit(heart8Img, cardPos)
    elif label == 35:
        # heart9
        DISPLAYSURF.blit(heart9Img, cardPos)
    elif label == 36:
        # heart10
        DISPLAYSURF.blit(heart10Img, cardPos)
    elif label == 37:
        # heartJ
        DISPLAYSURF.blit(heartJImg, cardPos)
    elif label == 38:
        # heartQ
        DISPLAYSURF.blit(heartQImg, cardPos)
    elif label == 39:
        # heartK
        DISPLAYSURF.blit(heartKImg, cardPos)
    elif label == 40:
        # spadeA
        DISPLAYSURF.blit(spadeAImg, cardPos)
    elif label == 41:
        # spade2
        DISPLAYSURF.blit(spade2Img, cardPos)
    elif label == 42:
        # spade3
        DISPLAYSURF.blit(spade3Img, cardPos)
    elif label == 43:
        # spade4
        DISPLAYSURF.blit(spade4Img, cardPos)
    elif label == 44:
        # spade5
        DISPLAYSURF.blit(spade5Img, cardPos)
    elif label == 45:
        # spade6
        DISPLAYSURF.blit(spade6Img, cardPos)
    elif label == 46:
        # spade7
        DISPLAYSURF.blit(spade7Img, cardPos)
    elif label == 47:
        # spade8
        DISPLAYSURF.blit(spade8Img, cardPos)
    elif label == 48:
        # spade9
        DISPLAYSURF.blit(spade9Img, cardPos)
    elif label == 49:
        # spade10
        DISPLAYSURF.blit(spade10Img, cardPos)
    elif label == 50:
        # spadeJ
        DISPLAYSURF.blit(spadeJImg, cardPos)
    elif label == 51:
        # spadeQ
        DISPLAYSURF.blit(spadeQImg, cardPos)
    elif label == 52:
        # spadeK
        DISPLAYSURF.blit(spadeKImg, cardPos)


def showSumOfPoints(text, (centerX, centerY)):
    fontObj = pygame.font.Font('arial.ttf', 18)
    textSurfaceObj = fontObj.render(text, True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (centerX, centerY)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def identifyValue(value):
    if value % 13 > 1 and value % 13 < 10:
        return value % 13
    elif value % 13 == 1:
        return 11
    else:
        return 10
    


def showYouBusted(text):
    fontObj = pygame.font.Font('JOKERMAN.ttf', 18)
    textSurfaceObj = fontObj.render(text, True, BLACK, SALMON)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (300, 370)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def showComputerWin(text):
    fontObj = pygame.font.Font('JOKERMAN.ttf', 18)
    textSurfaceObj = fontObj.render(text, True, BLACK, SALMON)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (300, 370)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def showPlayerWin(text):
    fontObj = pygame.font.Font('JOKERMAN.ttf', 18)
    textSurfaceObj = fontObj.render(text, True, BLACK, SALMON)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (300, 370)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def showTie():
    fontObj = pygame.font.Font('JOKERMAN.ttf', 18)
    textSurfaceObj = fontObj.render('It\'s a tie', True, BLACK, SALMON)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (300, 370)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def showMyMove(text):
    fontObj = pygame.font.Font('JOKERMAN.ttf', 14)
    textSurfaceObj = fontObj.render(text, True, BLACK, SALMON)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (300, 370)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def showShuffleAnime():
    DISPLAYSURF.blit(symbol1Img, (470, 170))
    pygame.display.update()
    fpsClock.tick(FPS)
    DISPLAYSURF.blit(symbol2Img, (470, 170))
    pygame.display.update()
    fpsClock.tick(FPS)
    DISPLAYSURF.blit(symbol3Img, (470, 170))
    pygame.display.update()
    fpsClock.tick(FPS)
    DISPLAYSURF.blit(symbol4Img, (470, 170))
    pygame.display.update()
    fpsClock.tick(FPS)
    DISPLAYSURF.blit(symbolImg, (470, 170))
    pygame.display.update()
    fpsClock.tick(FPS)


##def showGameResult(pWinTimes, iWinTimes):
##    grText = 'You won ' + str(pWinTimes) + '; I won ' + str(iWinTimes)
##    fontObj = pygame.font.Font('JOKERMAN.ttf', 14)
##    textSurfaceObj = fontObj.render(grText, True, BLACK, PALEGREEN)
##    textRectObj = textSurfaceObj.get_rect()
##    textRectObj.center = (300, 70)
##    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
##
##
##def incrementNumOfYOUWin(pWinTimes):
##    return pWinTimes + 1
##
##def incrementNumOfIWin(iWinTimes):
##    return iWinTimes + 1


def letMePlay(playerSum):
    # let the computer show how it would play
    # ________________STATE 1:
    # restore everything before any HITs or STANDs happened
    # Ccard1, Ccard2 => the first 2 cards of the enemy
    # Pcard1, Pcard2 => the first 2 cards of the player
    humanCardBoolList[0] = True
    humanCardBoolList[1] = True
    humanCardBoolList[2] = False
    humanCardBoolList[3] = False
    humanCardBoolList[4] = False

    computerCardBoolList[0] = True
    computerCardBoolList[1] = True
    computerCardBoolList[2] = False
    computerCardBoolList[3] = False
    computerCardBoolList[4] = False

    # _______________STATE 2:
    # consider to HIT or STAND based on playerSum and computerSum(partial).
    if playerSum > 13:
        # STAND
        showMyMove('stand')
        standOn = True
    else:
        showMyMove('hit')
        hitOn = True
    


##def gambleOn(cardPile):
##    # send two cards each from the card pile
##    # treat the cardpile as a stack, the last item of the list is on the top
##    dogeX, dogeY = (cardpileX, cardpileY)
##    while dogeX > 230:
##        DISPLAYSURF.blit(dogeImg, (dogeX, dogeY))
##        pygame.display.update()
##        dogeX -= 1
##        dogeY += 4
##    DISPLAYSURF.blit(dogeImg, (dogeX, dogeY))

def gameOver():
    pygame.quit()
    sys.exit()

    
    
if __name__ == '__main__':
    main()
