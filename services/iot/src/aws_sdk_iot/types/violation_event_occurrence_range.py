"""Generated from Smithy shape ``com.amazonaws.iot#ViolationEventOccurrenceRange``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.timestamp


class ViolationEventOccurrenceRange(TypedDict):
    start_time: "aws_sdk_iot.types.timestamp.Timestamp"
    """<p> The start date and time of a time period in which violation events occurred. </p>"""
    end_time: "aws_sdk_iot.types.timestamp.Timestamp"
    """<p> The end date and time of a time period in which violation events occurred. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViolationEventOccurrenceRange) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.timestamp

    out["startTime"] = aws_sdk_iot.types.timestamp.serialize_json(value["start_time"])
    import aws_sdk_iot.types.timestamp

    out["endTime"] = aws_sdk_iot.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> ViolationEventOccurrenceRange:
    out: ViolationEventOccurrenceRange = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_iot.types.timestamp

        out["start_time"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("ViolationEventOccurrenceRange.start_time required")
    if "endTime" in data:
        import aws_sdk_iot.types.timestamp

        out["end_time"] = aws_sdk_iot.types.timestamp.deserialize_json(data["endTime"])
    else:
        raise DeserializationError("ViolationEventOccurrenceRange.end_time required")
    return out
