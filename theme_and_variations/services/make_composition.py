from DataSounds.sounds import get_music, w2Midi
from composer import compose_variations, generate_theme_from_numbers
import midi
import random
import os


def make_files(segments):
    counter = 0
    for s in segments:
        w2Midi('theme_and_variations-{0}'.format(counter), s)
        counter += 1
    return len(segments)


def generate_composition(number_of_tracks):
    head_of_file = []
    pattern = midi.Pattern()
    t = midi.Track()

    note_choices = [2, 4, 8, 16]
    note_durations = []
    for i in range(0, 54):
        note_durations.append(random.choice(note_choices))

    for i in range(0, number_of_tracks):
        counter = 0
        s = midi.read_midifile("theme_and_variations-{0}.midi".format(i))
        for note in s[1][1:-1]:
            note.tick = note_durations[counter]
            counter += 1
        midi.write_midifile("theme_and_variations-{0}.midi".format(i), s)

    for i in range(0, number_of_tracks):
        s = midi.read_midifile("theme_and_variations-{0}.midi".format(i))
        if i == 0:
            head_of_file = s[0]
            del head_of_file[-1]
            head_of_file[2] = midi.SetTempoEvent(tick=0, data=[11, 113, 176])
            head_of_file[0] = midi.TimeSignatureEvent(tick=0, data=[4, 2, 96, 8])
            del s[1][-1]
            t.extend(s[1])
        elif i == number_of_tracks - 1:
            del s[1][0]
            t.extend(s[1])
        else:
            del s[1][-1]
            del s[1][0]
            t.extend(s[1])
        os.remove("theme_and_variations-{0}.midi".format(i))
    pattern.resolution = 32
    pattern.format = 1
    pattern.append(head_of_file)
    pattern.append(t)
    print pattern
   
    # Make file and move it to download directory to present to user
    midi.write_midifile("Theme-And-Variations.midi", pattern)
    print " DONE! "


def print_test_file():
    test_file = midi.read_midifile("small-world.mid")
    print(test_file)


def make_composition():
    print " GENERATING THEME AND VARIATIONS "
    theme = generate_theme_from_numbers()
    segments = compose_variations(theme)
    number_of_tracks = make_files(segments)
    generate_composition(number_of_tracks)

if __name__ == '__main__':
    make_composition()



"""
This is what inside of track looks like:

midi.Track(\
  [midi.ControlChangeEvent(tick=0, channel=5, data=[0, 0]),
   midi.ProgramChangeEvent(tick=0, channel=5, data=[36]),
   midi.ControlChangeEvent(tick=0, channel=5, data=[10, 84]),
   midi.TimeSignatureEvent(tick=0, data=[4, 2, 96, 8]),
   midi.SetTempoEvent(tick=0, data=[11, 113, 176]),
   midi.NoteOnEvent(tick=192, channel=5, data=[48, 54]),
   midi.NoteOffEvent(tick=48, channel=5, data=[48, 0]),
   midi.NoteOnEvent(tick=2832, channel=5, data=[36, 54]),
   midi.NoteOffEvent(tick=48, channel=5, data=[36, 0]),
   midi.NoteOnEvent(tick=2448, channel=5, data=[43, 54]),
   midi.NoteOffEvent(tick=192, channel=5, data=[43, 0]),
   midi.NoteOnEvent(tick=0, channel=5, data=[47, 54]),
   midi.NoteOffEvent(tick=192, channel=5, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=5, data=[48, 54]),
   midi.NoteOffEvent(tick=96, channel=5, data=[48, 0]),
   midi.NoteOnEvent(tick=96, channel=5, data=[48, 54]),
   midi.NoteOffEvent(tick=48, channel=5, data=[48, 0]),
   midi.NoteOnEvent(tick=144, channel=5, data=[48, 54]),
   midi.NoteOffEvent(tick=48, channel=5, data=[48, 0]),
   midi.NoteOnEvent(tick=2832, channel=5, data=[36, 54]),
   midi.NoteOffEvent(tick=48, channel=5, data=[36, 0]),
   midi.NoteOnEvent(tick=2448, channel=5, data=[43, 18]),
   midi.NoteOffEvent(tick=192, channel=5, data=[43, 0]),
   midi.NoteOnEvent(tick=0, channel=5, data=[47, 15]),
   midi.NoteOffEvent(tick=192, channel=5, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=5, data=[48, 12]),
   midi.NoteOffEvent(tick=96, channel=5, data=[48, 0]),
   midi.NoteOnEvent(tick=96, channel=5, data=[48, 8]),
   midi.NoteOffEvent(tick=48, channel=5, data=[48, 0]),
   midi.EndOfTrackEvent(tick=0, data=[])])])
"""