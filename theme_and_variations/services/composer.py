from DataSounds.sounds import get_music
import numpy as np

OCTAVES = 2


# Use Random integer function to generate main theme
def generate_theme_from_numbers():
    theme = np.random.randn(16)
    # print("theme is of type {0}".format(theme))
    return theme


# Play Theme unaltered
def theme_initial_statement(theme):
    music = get_music(theme, key="C", mode="pentatonic", octaves=1, instruments=[1], period=1)
    # print("music is of type {0}".format(music))
    return music


# Restate theme in strings. Most MIDI players are not interpreting this correctly and still play in piano.
def theme_restatement(theme):
    music = get_music(theme, key="C", mode="pentatonic", octaves=OCTAVES, instruments=[49], period=1)
    return music


# Transpose them to minor
def minor_mode(theme):
    music = get_music(theme, key="C", mode="minor", octaves=OCTAVES, instruments=[49], period=1)
    return music


# Return a music object that is in a key 4th above
def modulate_theme(theme):
    music = get_music(theme, key="F", mode="pentatonic", octaves=OCTAVES, instruments=[41], period=1)
    # print "this is a {0}".format(music)
    return music


# Transpose theme to pentatonic variation in different instrument
def change_instrumentation(theme):
    music = get_music(theme, key="C", mode="pentatonic", octaves=OCTAVES, instruments=[43], period=1)
    return music


def reverse_theme(theme):
    reversed_theme = theme[::-1]
    music = get_music(reversed_theme, key="C", mode="major", octaves=OCTAVES, instruments=[1], period=1)
    return music


# Assemble variations
def compose_variations(theme):
    segments = [theme_initial_statement(theme), theme_restatement(theme), minor_mode(theme),
                modulate_theme(theme), change_instrumentation(theme), reverse_theme(theme),
                theme_initial_statement(theme)]
    # print("Segments is {0} long".format(len(segments)))
    return segments
