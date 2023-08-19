import chorderator as cdt

def demo(output, inputKey):

    input_melody_path = 'MIDI/inputs/' + output + '/melody.mid'

    cdt.set_melody(input_melody_path)
    cdt.set_meta(tonic=inputKey)
    cdt.set_segmentation('A8B8A8B8')
    cdt.set_texture_prefilter((0, 2))
    cdt.set_note_shift(0)
    cdt.set_output_style(cdt.Style.POP_STANDARD)
    cdt.generate_save(output + '_output_results')
