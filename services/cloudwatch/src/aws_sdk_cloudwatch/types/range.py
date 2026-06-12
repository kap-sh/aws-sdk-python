"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Range``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.timestamp


class Range(TypedDict):
    start_time: NotRequired["aws_sdk_cloudwatch.types.timestamp.Timestamp"]
    """<p>The start time of the range to exclude. The format is <code>yyyy-MM-dd'T'HH:mm:ss</code>. For example, <code>2019-07-01T23:59:59</code>.</p>"""
    end_time: NotRequired["aws_sdk_cloudwatch.types.timestamp.Timestamp"]
    """<p>The end time of the range to exclude. The format is <code>yyyy-MM-dd'T'HH:mm:ss</code>. For example, <code>2019-07-01T23:59:59</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Range) -> dict:
    out: dict = {}
    if "start_time" in value:
        import aws_sdk_cloudwatch.types.timestamp

        out["StartTime"] = aws_sdk_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_cloudwatch.types.timestamp

        out["EndTime"] = aws_sdk_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Range:
    out: Range = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_cloudwatch.types.timestamp

        out["start_time"] = aws_sdk_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_cloudwatch.types.timestamp

        out["end_time"] = aws_sdk_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["EndTime"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(value: Range, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "start_time" in value:
        import aws_sdk_cloudwatch.types.timestamp

        aws_sdk_cloudwatch.types.timestamp.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import aws_sdk_cloudwatch.types.timestamp

        aws_sdk_cloudwatch.types.timestamp.serialize_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )


def deserialize_query(el: Element) -> Range:
    out: Range = {}  # type: ignore[typeddict-item]
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import aws_sdk_cloudwatch.types.timestamp

        out["start_time"] = aws_sdk_cloudwatch.types.timestamp.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import aws_sdk_cloudwatch.types.timestamp

        out["end_time"] = aws_sdk_cloudwatch.types.timestamp.deserialize_query(
            child_end_time
        )
    return out
