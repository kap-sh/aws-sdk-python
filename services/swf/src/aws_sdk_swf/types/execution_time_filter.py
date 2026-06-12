"""Generated from Smithy shape ``com.amazonaws.swf#ExecutionTimeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.timestamp


class ExecutionTimeFilter(TypedDict):
    oldest_date: "aws_sdk_swf.types.timestamp.Timestamp"
    """<p>Specifies the oldest start or close date and time to return.</p>"""
    latest_date: NotRequired["aws_sdk_swf.types.timestamp.Timestamp"]
    """<p>Specifies the latest start or close date and time to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionTimeFilter) -> dict:
    out: dict = {}
    import aws_sdk_swf.types.timestamp

    out["oldestDate"] = aws_sdk_swf.types.timestamp.serialize_aws_json_1_0(
        value["oldest_date"]
    )
    if "latest_date" in value:
        import aws_sdk_swf.types.timestamp

        out["latestDate"] = aws_sdk_swf.types.timestamp.serialize_aws_json_1_0(
            value["latest_date"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecutionTimeFilter:
    out: ExecutionTimeFilter = {}  # type: ignore[typeddict-item]
    if "oldestDate" in data:
        import aws_sdk_swf.types.timestamp

        out["oldest_date"] = aws_sdk_swf.types.timestamp.deserialize_aws_json_1_0(
            data["oldestDate"]
        )
    else:
        raise DeserializationError("ExecutionTimeFilter.oldest_date required")
    if "latestDate" in data:
        import aws_sdk_swf.types.timestamp

        out["latest_date"] = aws_sdk_swf.types.timestamp.deserialize_aws_json_1_0(
            data["latestDate"]
        )
    return out
