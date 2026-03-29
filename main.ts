radio.onReceivedNumber(function (receivedNumber) {
	
})
basic.forever(function () {
    basic.showLeds(`
        . . . . .
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showString("Hello!")
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    led.plotBarGraph(
    0,
    0
    )
})
