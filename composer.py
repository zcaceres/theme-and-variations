from DataSounds.sounds import get_music, w2Midi
import numpy as np

OCTAVES = 2

# Use Random integer function to generate main theme
def generate_theme_from_numbers():
    theme = np.random.randn(16)
    print("theme is of type {0}".format(theme))
    return theme

# Play Theme unaltered
def theme_initial_statement(theme):
    music = get_music(theme, key="C", mode="pentatonic", octaves=1, instruments=[1], period=1)
    print("music is of type {0}".format(music))
    return music

# Restate theme in strings (NOT WORKING YET!)
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
    print "this is a {0}".format(music)
    return music

# Transpose theme to pentatonic variation in different instrument
def change_instrumentation(theme):
    music = get_music(theme, key="C", mode="pentatonic", octaves=OCTAVES, instruments=[43], period=1)
    return music


# Reverse theme
def reverse_theme(theme):
    reversed_theme = theme[::-1]
    music = get_music(reversed_theme, key="C", mode="major", octaves=OCTAVES, instruments=[1], period=1)
    return music


# Assemble variations
def compose_variations(theme):
    segments = []
    segments.append(theme_initial_statement(theme))
    segments.append(theme_restatement(theme))
    segments.append(minor_mode(theme))
    segments.append(modulate_theme(theme))
    segments.append(change_instrumentation(theme))
    segments.append(reverse_theme(theme))
    # print("Segments is {0} long".format(len(segments)))
    return segments










# def add_segment_to_composition(segments):
#     final_piece = BytesIO()
#     with open('music.midi', 'wb') as music:
#         for s in segments:
#             print("writing segment {0}".format(s))
#             s.write(bytes(final_piece))
#             music.write(s.getvalue())
#             print("added segment: {0}".format(s.getvalue()))
        # print ("FINAL PIECE IS: {0}".format(final_piece.getvalue()))
        # music.write(final_piece.getvalue())
    # with open ('music.midi', 'wb') as music_bytes:
        # byt = music_bytes.read()
        # return BytesIO(byt)

    # BytesIO(BufferedReader.read(music))
    # return music