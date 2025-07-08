import pretty_midi
import os

def generate_break(output_path="output/midi", bpm=160):
    midi = pretty_midi.PrettyMIDI(initial_tempo=bpm)
    drum = pretty_midi.Instrument(program=0, is_drum=True, name="Break")

    beat = 60.0 / bpm
    for i in range(8):
        t = i * beat / 2
        drum.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.1))
        if i % 2 == 0:
            drum.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1))

    midi.instruments.append(drum)
    os.makedirs(output_path, exist_ok=True)
    midi.write(os.path.join(output_path, "freeparty_break_160bpm.mid"))

if __name__ == "__main__":
    generate_break()
