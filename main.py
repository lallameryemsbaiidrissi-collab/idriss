def on_forever():
    basic.show_leds("""music.play(music.string_playable("", 120), music.PlaybackMode.UNTIL_DONE)
        . . . . .
        # # # # #
        basic.showNumber(0)
        # # # # #
        # # # # #
        # # # # #
        """)
    basic.show_string("Hello!")
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
