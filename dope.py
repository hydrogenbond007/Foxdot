# Set up a basic beat
d1 >> play("<x* ><  h >", pan=(-0.5,0.5))

# Add a bassline
b1 >> bass(dur=1/4, sus=2, amp=[0.8, 0.9])

# Melodic synth line
p1 >> pluck(oct=6, dur=1/4, sus=4, amp=0.5).spread()

# Adding some effects
d1 >> play("<x* ><  h >", pan=(-0.5,0.5)).every(6, "stutter", 4, dur=3)

# Change the tempo
Clock.bpm = 150

# Variation in the bassline
b1.often("offadd", 4, ">", dur=3)

# Add some randomness
p1.every(8, "jump", cycle=range(4))
