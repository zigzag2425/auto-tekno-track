import pretty_midi
import os

def arrange_track(output_path="output/midi", bpm=160):
    def load(filename, start_measure, beats_per_measure=4):
        midi = pretty_midi.PrettyMIDI(filename)
        shifted = []
        for inst in midi.instruments:
            new_inst = pretty_midi.Instrument(program=inst.program, is_drum=inst.is_drum, name=inst.name)
            for note in inst.notes:
                offset = start_measure * beats_per_measure * (60.0 / bpm)
                new_inst.notes.append(pretty_midi.Note(
                    velocity=note.velocity, pitch=note.pitch,
                    start=note.start + offset, end=note.end + offset))
            shifted.append(new_inst)
        return shifted

    structure = [
        (["kick.mid"], 0),          # intro
        (["kick.mid", "acid_bassline_160bpm.mid", "acid_rave_lead_160bpm.mid"], 4),
        (["freeparty_break_160bpm.mid"], 12),
        (["kick.mid", "acid_bassline_160bpm.mid", "acid_rave_lead_160bpm.mid"], 14),
        (["kick.mid"], 22)
    ]

    final = pretty_midi.PrettyMIDI(initial_tempo=bpm)
    for files, start in structure:
        for f in files:
            instruments = load(os.path.join("output/midi", f), start)
            for inst in instruments:
                final.instruments.append(inst)

    os.makedirs(output_path, exist_ok=True)
    final.write(os.path.join(output_path, "freeparty_track_160bpm.mid"))

if __name__ == "__main__":
    arrange_track()
