import abjad
from hamon_shu.Materials.timespans.Segment_I.make_timespans import rhythm_timespan_list

offset_counter = abjad.OffsetCounter(rhythm_timespan_list)

permitted_meters = abjad.MeterList(
    [(5, 4), (9, 8), (4, 4), (7, 8), (3, 4), (5, 8), (2, 4), (3, 8), (5, 16), (2, 8), (3, 16), (1, 8)]
)

fitted_meters = abjad.Meter.fit_meters(
    argument=offset_counter,
    meters=permitted_meters,
    # maximum_run_length=1
)

time_signatures = [abjad.TimeSignature(_) for _ in fitted_meters]

time_signatures.append(abjad.TimeSignature((1, 4)))  # for ending skip

bounds = abjad.mathtools.cumulative_sums([_.duration for _ in time_signatures])