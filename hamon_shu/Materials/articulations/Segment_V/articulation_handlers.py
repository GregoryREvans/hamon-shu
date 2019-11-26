import evans
import abjad


articulation_handler_one = evans.BendHandler(
        bend_amounts=[1, 2, -1, 3, -2, -1],
        bend_continuous=True,
        boolean_vector=[1, 0, 0],
        vector_continuous=True,
        name="articulation_handler_one",
)

articulation_handler_two = evans.GlissandoHandler(
    #glissando_style="hide_middle_note_heads",
    line_style=None,
    boolean_vector=[0, 1],
    continuous=True,
    name="articulation_handler_two",
)

articulation_handler_three = evans.BendHandler(
        bend_amounts=[5, 4, -3, 2, -1, -2, 3, -4, ],
        bend_continuous=True,
        boolean_vector=[1, 0, 0],
        vector_continuous=True,
        name="articulation_handler_three",
)