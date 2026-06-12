"""Generated from Smithy shape ``com.amazonaws.inspector#TimestampRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector.types.timestamp


class TimestampRange(TypedDict):
    begin_date: NotRequired["aws_sdk_inspector.types.timestamp.Timestamp"]
    """<p>The minimum value of the timestamp range.</p>"""
    end_date: NotRequired["aws_sdk_inspector.types.timestamp.Timestamp"]
    """<p>The maximum value of the timestamp range.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimestampRange) -> dict:
    out: dict = {}
    if "begin_date" in value:
        import aws_sdk_inspector.types.timestamp

        out["beginDate"] = aws_sdk_inspector.types.timestamp.serialize_aws_json_1_1(
            value["begin_date"]
        )
    if "end_date" in value:
        import aws_sdk_inspector.types.timestamp

        out["endDate"] = aws_sdk_inspector.types.timestamp.serialize_aws_json_1_1(
            value["end_date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimestampRange:
    out: TimestampRange = {}  # type: ignore[typeddict-item]
    if "beginDate" in data:
        import aws_sdk_inspector.types.timestamp

        out["begin_date"] = aws_sdk_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["beginDate"]
        )
    if "endDate" in data:
        import aws_sdk_inspector.types.timestamp

        out["end_date"] = aws_sdk_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["endDate"]
        )
    return out
