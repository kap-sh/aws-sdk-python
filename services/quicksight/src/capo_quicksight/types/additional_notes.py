"""Generated from Smithy shape ``com.amazonaws.quicksight#AdditionalNotes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.additional_notes_text


class AdditionalNotes(TypedDict, closed=True):
    text: NotRequired["capo_quicksight.types.additional_notes_text.AdditionalNotesText"]
    """<p>The additional notes text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalNotes) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    return out


def deserialize_json(data: dict) -> AdditionalNotes:
    out: AdditionalNotes = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    return out
