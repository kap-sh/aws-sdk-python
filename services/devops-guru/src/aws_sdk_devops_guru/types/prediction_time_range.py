"""Generated from Smithy shape ``com.amazonaws.devopsguru#PredictionTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.timestamp


class PredictionTimeRange(TypedDict, closed=True):
    start_time: "aws_sdk_devops_guru.types.timestamp.Timestamp"
    """<p> The time range during which a metric limit is expected to be exceeded. This applies to proactive insights only. </p>"""
    end_time: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p> The time when the behavior in a proactive insight is expected to end. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictionTimeRange) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.timestamp

    out["StartTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["EndTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> PredictionTimeRange:
    out: PredictionTimeRange = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["start_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        raise DeserializationError("PredictionTimeRange.start_time required")
    if "EndTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["end_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["EndTime"]
        )
    return out
