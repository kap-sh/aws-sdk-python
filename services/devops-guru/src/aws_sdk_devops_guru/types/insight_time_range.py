"""Generated from Smithy shape ``com.amazonaws.devopsguru#InsightTimeRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.timestamp


class InsightTimeRange(TypedDict):
    start_time: "aws_sdk_devops_guru.types.timestamp.Timestamp"
    """<p> The time when the behavior described in an insight started. </p>"""
    end_time: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p> The time when the behavior described in an insight ended. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightTimeRange) -> dict:
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


def deserialize_json(data: dict) -> InsightTimeRange:
    out: InsightTimeRange = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["start_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        raise DeserializationError("InsightTimeRange.start_time required")
    if "EndTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["end_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["EndTime"]
        )
    return out
