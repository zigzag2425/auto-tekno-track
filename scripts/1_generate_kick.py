import pretty_midi
import os

def generate_kick(output_path="output/midi", bpm=160, length_bars=1):
    midi = pretty_midi.PrettyMIDI(initial_tempo=bpm)
    kick = pretty_midi.Instrument(program=0, is_drum=True, name="Kick")

    beat_duration = 60.0 / bpm
    for i in range(length_bars * 4):
        start = i * beat_duration
        note = pretty_midi.Note(velocity=120, pitch=36, start=start, end=start + 0.05)
        kick.notes.append(note)

    midi.instruments.append(kick)
    os.makedirs(output_path, exist_ok=True)
    midi.write(os.path.join(output_path, "kick.mid"))

if __name__ == "__main__":
    generate_kick()
