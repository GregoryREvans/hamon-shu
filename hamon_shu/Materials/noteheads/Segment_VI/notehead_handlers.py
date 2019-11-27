import evans
import abjad


notehead_handler_one = evans.NoteheadHandler(
    notehead_list=["harmonic-mixed", "default", "harmonic-mixed", "default"],
    transition=False,
    head_boolean_vector=[0],
    head_vector_continuous=True,
    continuous=True,
    name="notehead handler one",
)

notehead_handler_two = evans.NoteheadHandler(
    notehead_list=["default"],
    transition=False,
    head_boolean_vector=[1],
    head_vector_continuous=True,
    transition_boolean_vector=[1],
    transition_vector_continuous=True,
    continuous=False,
    count=-1,
    name="notehead handler two",
)

notehead_handler_three = evans.NoteheadHandler(
    notehead_list=["harmonic-mixed", "harmonic-mixed", "default",],
    transition=False,
    head_boolean_vector=[0, 0, 1, 0, 1, 0, 1],
    head_vector_continuous=True,
    transition_boolean_vector=[0],
    transition_vector_continuous=True,
    continuous=True,
    count=-1,
    name="notehead handler three",
)