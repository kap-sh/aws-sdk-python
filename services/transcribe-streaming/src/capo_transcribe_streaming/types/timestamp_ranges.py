"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#TimestampRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.timestamp_range

TimestampRanges: TypeAlias = list[
    "capo_transcribe_streaming.types.timestamp_range.TimestampRange"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimestampRanges) -> list:
    import capo_transcribe_streaming.types.timestamp_range

    out: list = []
    for item in value:
        out.append(capo_transcribe_streaming.types.timestamp_range.serialize_json(item))
    return out


def deserialize_json(data: list) -> TimestampRanges:
    import capo_transcribe_streaming.types.timestamp_range

    out: TimestampRanges = []
    for item in data:
        out.append(
            capo_transcribe_streaming.types.timestamp_range.deserialize_json(item)
        )
    return out
