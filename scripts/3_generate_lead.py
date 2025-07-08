import pretty_midi
import random
import os

def generate_acid_bass(output_path="output/midi", bpm=160, bars=1):
    midi = pretty_midi.PrettyMIDI(initial_tempo=bpm)
    bass = pretty_midi.Instrument(program=38, name="AcidBass")

    scale = [36, 38, 41, 43, 46, 48]
    beat = 60.0 / bpm

    for i in range(bars * 4):
        start = i * beat
        pitch = random.choice(scale)
        bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

    midi.instruments.append(bass)
    os.makedirs(output_path, exist_ok=True)
    midi.write(os.path.join(output_path, "acid_bassline_160bpm.mid"))

if __name__ == "__main__":
    generate_acid_bass()
