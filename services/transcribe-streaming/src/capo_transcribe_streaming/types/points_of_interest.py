"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#PointsOfInterest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.timestamp_ranges


class PointsOfInterest(TypedDict, closed=True):
    timestamp_ranges: NotRequired[
        "capo_transcribe_streaming.types.timestamp_ranges.TimestampRanges"
    ]
    """<p>Contains the timestamp ranges (start time through end time) of matched categories and rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PointsOfInterest) -> dict:
    out: dict = {}
    if "timestamp_ranges" in value:
        import capo_transcribe_streaming.types.timestamp_ranges

        out["TimestampRanges"] = (
            capo_transcribe_streaming.types.timestamp_ranges.serialize_json(
                value["timestamp_ranges"]
            )
        )
    return out


def deserialize_json(data: dict) -> PointsOfInterest:
    out: PointsOfInterest = {}  # type: ignore[typeddict-item]
    if "TimestampRanges" in data:
        import capo_transcribe_streaming.types.timestamp_ranges

        out["timestamp_ranges"] = (
            capo_transcribe_streaming.types.timestamp_ranges.deserialize_json(
                data["TimestampRanges"]
            )
        )
    return out
