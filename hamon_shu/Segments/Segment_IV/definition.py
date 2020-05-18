import pathlib

import evans
from hamon_shu.Materials.pitch.Segment_IV.clef_handlers import clef_handlers
from hamon_shu.Materials.score_structure.Segment_IV.time_signatures import (
    time_signatures,
)
from hamon_shu.Materials.score_structure.instruments import instruments as insts
from hamon_shu.Materials.score_structure.score_structure import score
from hamon_shu.Materials.timespans.Segment_IV.convert_timespans import (
    Segment_IV_rhythm_timespans,
    Segment_IV_timespans,
)

maker = evans.SegmentMaker(
    instruments=insts,
    names=["Violin I", "Violin II", "Viola", "Violoncello"],
    abbreviations=["vn. I", "vn. II", "va.", "vc."],
    rhythm_timespans=Segment_IV_rhythm_timespans,
    handler_timespans=Segment_IV_timespans,
    score_template=score,
    time_signatures=time_signatures,
    clef_handlers=clef_handlers,
    voicewise_persistent_indicators=[[], [], [], []],
    tuplet_bracket_noteheads=False,
    add_final_grand_pause=False,
    score_includes=[
        "/Users/evansdsg2/abjad/docs/source/_stylesheets/abjad.ily",
        "/Users/evansdsg2/Scores/hamon_shu/hamon_shu/Build/first_stylesheet.ily",
    ],
    parts_includes=[
        "/Users/evansdsg2/abjad/docs/source/_stylesheets/abjad.ily",
        "/Users/evansdsg2/Scores/hamon_shu/hamon_shu/Build/parts_stylesheet.ily",
    ],
    segment_name="Segment_IV",
    current_directory=pathlib.Path(__file__).parent,
    build_path=(pathlib.Path(__file__).parent / ".." / ".." / "Build").resolve(),
    cutaway=False,
    beam_pattern="meter",
    beam_rests=False,
    barline="||",
    tempo=((1, 4), 120),
    rehearsal_mark="C",
    page_break_counts=[2, 7, 8, 8, 7, 8, 7, 7],
    midi=False,
)

maker.build_segment()
