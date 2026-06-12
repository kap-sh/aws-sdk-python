"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#PointsOfInterest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.timestamp_ranges


class PointsOfInterest(TypedDict):
    timestamp_ranges: NotRequired[
        "aws_sdk_transcribe_streaming.types.timestamp_ranges.TimestampRanges"
    ]
    """<p>Contains the timestamp ranges (start time through end time) of matched categories and rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PointsOfInterest) -> dict:
    out: dict = {}
    if "timestamp_ranges" in value:
        import aws_sdk_transcribe_streaming.types.timestamp_ranges

        out["TimestampRanges"] = (
            aws_sdk_transcribe_streaming.types.timestamp_ranges.serialize_json(
                value["timestamp_ranges"]
            )
        )
    return out


def deserialize_json(data: dict) -> PointsOfInterest:
    out: PointsOfInterest = {}  # type: ignore[typeddict-item]
    if "TimestampRanges" in data:
        import aws_sdk_transcribe_streaming.types.timestamp_ranges

        out["timestamp_ranges"] = (
            aws_sdk_transcribe_streaming.types.timestamp_ranges.deserialize_json(
                data["TimestampRanges"]
            )
        )
    return out
