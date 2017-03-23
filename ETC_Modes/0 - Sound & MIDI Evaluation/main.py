import os
import pygame
import pygame.freetype

lines = []
string1 = unicode(" ")

trigger = False



def setup(screen, etc):
    pygame.freetype.init()
    pass

def draw(screen, etc):
    global string1, trigger
    # this is the user sound evaluation mode. 
    #Designed to help you understand how an oscillascope mode works, and how sonic events are turned to triggers
    # in this mode no knobs work, and the persist button except audio gain
    # with the etc recieving sound from via the audio input jack the black line will display the waveform of that audio.
    # if the amplitude of the audio reaches the red lines it will trigger
    # you can also set a trigger with the onboard trigger button.
    # the amplitude and trigger correspond to audio level meter and trigger box in the OSD
    pygame.draw.rect(screen, (255,255,255), ((0,0),(1280,720)), 0)
    
    font1 = pygame.freetype.Font(etc.mode_root + "/font.ttf", 50)
    (text1, textpos1) = font1.render(string1, (0,0,0))
    textpos1 = (950, 60)
    
    font2 = pygame.freetype.Font(etc.mode_root + "/font.ttf", 30)
    string2 = unicode("Sound Test Mode")
    (text2, textpos2) = font2.render(string2, (0,0,0))
    textpos2 = (20, 10)
    
    font3 = pygame.freetype.Font(etc.mode_root + "/font.ttf", 20)
    string3 = unicode("This mode is designed to help you understand Scopes and Triggers on the ETC.")
    (text3, textpos3) = font3.render(string3, (0,0,0))
    textpos3 = (20, 50)
    
    
    string4 = unicode("In this mode all knobs except the Audio Gain are disabled.")
    (text4, textpos4) = font3.render(string4, (0,0,0))
    textpos4 = (20, 75)
    
    
    string5 = unicode("The black line displays the continuous audio input used to generate visuals in Scope modes.")
    (text5, textpos5) = font3.render(string5, (0,0,0))
    textpos5 = (20, 100)
    
    
    string6 = unicode("If the amplitude of the audio reaches the red lines it will trigger events in Trigger modes.")
    (text6, textpos6) = font3.render(string6, (0,0,0))
    textpos6 = (20, 125)
    
    
    string7 = unicode("Pressing the Trigger button will artificially produce a trigger and waveform if no audio is connected.")
    (text7, textpos7) = font3.render(string7, (0,0,0))
    textpos7 = (20, 580)
    
    
    string8 = unicode("The sound level and trigger status can also be previewed on the on screen display (OSD).")
    (text8, textpos8) = font3.render(string8, (0,0,0))
    textpos8 = (20, 605)
    
    
    if trigger == False : string1 = unicode("")
    if etc.audio_trig or etc.midi_note_new : trigger = True
    if trigger == True : string1 = unicode("TRIGGER")
    
    lines = [(i*14, 360+((etc.audio_in[i]*0.00003052)*200)) for i in range(0,99)]
    trigger = False
    
    pygame.draw.aalines(screen, (0,0,0), False, lines, 1)
    pygame.draw.line(screen, (255,0,0), (0,239), (1280,239), 1)
    pygame.draw.line(screen, (255,0,0), (0,481), (1280,481), 1)
    
    screen.blit(text1, textpos1)
    screen.blit(text2, textpos2)
    screen.blit(text3, textpos3)
    screen.blit(text4, textpos4)
    screen.blit(text5, textpos5)
    screen.blit(text6, textpos6)
    screen.blit(text7, textpos7)
    screen.blit(text8, textpos8)
    
    
    
    
    
    



   

