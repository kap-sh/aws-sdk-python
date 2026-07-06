"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationNote``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_note_string


class EvaluationNote(TypedDict, closed=True):
    value: NotRequired[
        "aws_sdk_connect.types.evaluation_note_string.EvaluationNoteString"
    ]
    """<p>The note for an item (section or question) in a contact evaluation.</p> <note> <p>Even though a note in an evaluation can have up to 3072 chars, there is also a limit on the total number of chars for all the notes in the evaluation combined. Assuming there are N questions in the evaluation being submitted, then the max char limit for all notes combined is N x 1024.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationNote) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> EvaluationNote:
    out: EvaluationNote = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
