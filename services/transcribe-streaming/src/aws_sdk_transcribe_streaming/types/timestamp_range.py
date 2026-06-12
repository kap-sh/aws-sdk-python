"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#TimestampRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.long


class TimestampRange(TypedDict):
    begin_offset_millis: NotRequired["aws_sdk_transcribe_streaming.types.long.Long"]
    """<p>The time, in milliseconds, from the beginning of the audio stream to the start of the category match.</p>"""
    end_offset_millis: NotRequired["aws_sdk_transcribe_streaming.types.long.Long"]
    """<p>The time, in milliseconds, from the beginning of the audio stream to the end of the category match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimestampRange) -> dict:
    out: dict = {}
    if "begin_offset_millis" in value:
        out["BeginOffsetMillis"] = value["begin_offset_millis"]
    if "end_offset_millis" in value:
        out["EndOffsetMillis"] = value["end_offset_millis"]
    return out


def deserialize_json(data: dict) -> TimestampRange:
    out: TimestampRange = {}  # type: ignore[typeddict-item]
    if "BeginOffsetMillis" in data:
        out["begin_offset_millis"] = data["BeginOffsetMillis"]
    if "EndOffsetMillis" in data:
        out["end_offset_millis"] = data["EndOffsetMillis"]
    return out
