"""Generated from Smithy shape ``com.amazonaws.guardduty#ContinuousScanDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_guardduty.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.timestamp


class ContinuousScanDetails(TypedDict):
    start_time: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp representing the start of the time range to scan. Reserved for internal use.</p>"""
    end_time: "aws_sdk_guardduty.types.timestamp.Timestamp"
    """<p>The timestamp representing the end of the time range to scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContinuousScanDetails) -> dict:
    out: dict = {}
    if "start_time" in value:
        import aws_sdk_guardduty.types.timestamp

        out["startTime"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["start_time"]
        )
    import aws_sdk_guardduty.types.timestamp

    out["endTime"] = aws_sdk_guardduty.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> ContinuousScanDetails:
    out: ContinuousScanDetails = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_guardduty.types.timestamp

        out["start_time"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_guardduty.types.timestamp

        out["end_time"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("ContinuousScanDetails.end_time required")
    return out
