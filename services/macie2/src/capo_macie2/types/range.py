"""Generated from Smithy shape ``com.amazonaws.macie2#Range``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__long


class Range(TypedDict, closed=True):
    end: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The number of lines from the beginning of the file to the end of the sensitive data.</p>"""
    start: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The number of lines from the beginning of the file to the beginning of the sensitive data.</p>"""
    start_column: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The number of characters, with spaces and starting from 1, from the beginning of the first line that contains the sensitive data (start) to the beginning of the sensitive data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Range) -> dict:
    out: dict = {}
    if "end" in value:
        out["end"] = value["end"]
    if "start" in value:
        out["start"] = value["start"]
    if "start_column" in value:
        out["startColumn"] = value["start_column"]
    return out


def deserialize_json(data: dict) -> Range:
    out: Range = {}  # type: ignore[typeddict-item]
    if "end" in data:
        out["end"] = data["end"]
    if "start" in data:
        out["start"] = data["start"]
    if "startColumn" in data:
        out["start_column"] = data["startColumn"]
    return out
