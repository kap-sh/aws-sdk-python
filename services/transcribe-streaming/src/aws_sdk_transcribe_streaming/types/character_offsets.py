"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#CharacterOffsets``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.integer


class CharacterOffsets(TypedDict, closed=True):
    begin: NotRequired["aws_sdk_transcribe_streaming.types.integer.Integer"]
    """<p>Provides the character count of the first character where a match is identified. For example, the first character associated with an issue or a category match in a segment transcript.</p>"""
    end: NotRequired["aws_sdk_transcribe_streaming.types.integer.Integer"]
    """<p>Provides the character count of the last character where a match is identified. For example, the last character associated with an issue or a category match in a segment transcript.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CharacterOffsets) -> dict:
    out: dict = {}
    if "begin" in value:
        out["Begin"] = value["begin"]
    if "end" in value:
        out["End"] = value["end"]
    return out


def deserialize_json(data: dict) -> CharacterOffsets:
    out: CharacterOffsets = {}  # type: ignore[typeddict-item]
    if "Begin" in data:
        out["begin"] = data["Begin"]
    if "End" in data:
        out["end"] = data["End"]
    return out
