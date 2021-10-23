Kostka = 0
A = 0
Typ = 6
Player = 1
def on_forever():
    global Typ, A, Kostka, Player
    if input.button_is_pressed(Button.B):
        if Player == 1:
            Player = 2
            basic.show_string("2P")
            basic.pause(500)
            basic.clear_screen()
        elif Player == 2:
            Player = 1
            basic.show_string("1P")
            basic.pause(500)
            basic.clear_screen()
    if input.logo_is_pressed():
        if Typ == 6:
            basic.show_number(10)
            basic.pause(300)
            basic.clear_screen()
            Typ = 10
        else:
            basic.show_number(6)
            basic.pause(300)
            basic.clear_screen()
            Typ = 6
    if input.button_is_pressed(Button.A):
        A = 1
        basic.show_number(1)
        basic.pause(500)
        basic.clear_screen()
    if input.is_gesture(Gesture.SHAKE):
        if A == 1 or A == 2:
            if Typ == 6:
                Kostka = randint(1, 6)
            elif Typ == 10:
                Kostka = randint(1, 10)
            basic.pause(100)
            if Kostka > 0:
                led.plot(0, 4)
            if Kostka > 1:
                led.plot(4, 4)
            if Kostka > 2:
                led.plot(0, 0)
            if Kostka > 3:
                led.plot(4, 0)
            if Kostka > 4:
                led.plot(2, 2)
            if Kostka > 5:
                led.plot(0, 2)
                led.plot(4, 2)
            if Kostka == 6:
                led.unplot(2, 2)
            if Kostka > 6:
                led.plot(4, 4)
            if Kostka > 7:
                led.plot(2, 4)
                led.plot(2, 0)
            if Kostka == 8:
                led.unplot(2, 2)
            if Kostka > 8:
                led.plot(2, 0)
            if Kostka > 9:
                led.unplot(2, 2)
                led.plot(1, 2)
                led.plot(3, 2)
            for index in range(Kostka):
                music.play_tone(500, music.beat(BeatFraction.EIGHTH))
                basic.pause(300)
            basic.pause(3000)
            basic.clear_screen()
            if A == 1 and Player == 2:
                A += 1
                basic.show_number(2)
                basic.pause(500)
                basic.clear_screen()
            else:
                basic.show_string("NEXT?")
                A = 0
basic.forever(on_forever)