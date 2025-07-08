import pretty_midi
import os
import random

def auto_mix(input_file="output/midi/freeparty_track_160bpm.mid", output_path="output/mixed", bpm=160):
    midi = pretty_midi.PrettyMIDI(input_file=input_file, initial_tempo=bpm)

    for inst in midi.instruments:
        if "kick" in inst.name.lower():
            v_range = (110, 127)
        elif "bass" in inst.name.lower():
            v_range = (80, 100)
        elif "lead" in inst.name.lower():
            v_range = (60, 90)
        else:
            v_range = (70, 100)

        for note in inst.notes:
            note.velocity = random.randint(*v_range)

    os.makedirs(output_path, exist_ok=True)
    midi.write(os.path.join(output_path, "freeparty_track_160bpm_auto_mix.mid"))

if __name__ == "__main__":
    auto_mix()
