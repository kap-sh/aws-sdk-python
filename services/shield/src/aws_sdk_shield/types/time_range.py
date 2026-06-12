"""Generated from Smithy shape ``com.amazonaws.shield#TimeRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_shield.types.timestamp


class TimeRange(TypedDict):
    from_inclusive: NotRequired["aws_sdk_shield.types.timestamp.Timestamp"]
    """<p>The start time, in Unix time in seconds. </p>"""
    to_exclusive: NotRequired["aws_sdk_shield.types.timestamp.Timestamp"]
    """<p>The end time, in Unix time in seconds. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeRange) -> dict:
    out: dict = {}
    if "from_inclusive" in value:
        import aws_sdk_shield.types.timestamp

        out["FromInclusive"] = aws_sdk_shield.types.timestamp.serialize_aws_json_1_1(
            value["from_inclusive"]
        )
    if "to_exclusive" in value:
        import aws_sdk_shield.types.timestamp

        out["ToExclusive"] = aws_sdk_shield.types.timestamp.serialize_aws_json_1_1(
            value["to_exclusive"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeRange:
    out: TimeRange = {}  # type: ignore[typeddict-item]
    if "FromInclusive" in data:
        import aws_sdk_shield.types.timestamp

        out["from_inclusive"] = aws_sdk_shield.types.timestamp.deserialize_aws_json_1_1(
            data["FromInclusive"]
        )
    if "ToExclusive" in data:
        import aws_sdk_shield.types.timestamp

        out["to_exclusive"] = aws_sdk_shield.types.timestamp.deserialize_aws_json_1_1(
            data["ToExclusive"]
        )
    return out
