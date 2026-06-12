"""Generated from Smithy shape ``com.amazonaws.mediatailor#ClipRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__long


class ClipRange(TypedDict):
    end_offset_millis: "aws_sdk_mediatailor.types.__long.__long"
    """<p>The end offset of the clip range, in milliseconds, starting from the beginning of the VOD source associated with the program.</p>"""
    start_offset_millis: NotRequired["aws_sdk_mediatailor.types.__long.__long"]
    """<p>The start offset of the clip range, in milliseconds. This offset truncates the start at the number of milliseconds into the duration of the VOD source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClipRange) -> dict:
    out: dict = {}
    out["EndOffsetMillis"] = value.get("end_offset_millis", 0)
    if "start_offset_millis" in value:
        out["StartOffsetMillis"] = value["start_offset_millis"]
    return out


def deserialize_json(data: dict) -> ClipRange:
    out: ClipRange = {}  # type: ignore[typeddict-item]
    if "EndOffsetMillis" in data:
        out["end_offset_millis"] = data["EndOffsetMillis"]
    else:
        out["end_offset_millis"] = 0
    if "StartOffsetMillis" in data:
        out["start_offset_millis"] = data["StartOffsetMillis"]
    return out
