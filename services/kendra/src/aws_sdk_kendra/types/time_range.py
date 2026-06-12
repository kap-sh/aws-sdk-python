"""Generated from Smithy shape ``com.amazonaws.kendra#TimeRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.timestamp


class TimeRange(TypedDict):
    start_time: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the beginning of the time range.</p>"""
    end_time: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the end of the time range.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeRange) -> dict:
    out: dict = {}
    if "start_time" in value:
        import aws_sdk_kendra.types.timestamp

        out["StartTime"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_kendra.types.timestamp

        out["EndTime"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeRange:
    out: TimeRange = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_kendra.types.timestamp

        out["start_time"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_kendra.types.timestamp

        out["end_time"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
