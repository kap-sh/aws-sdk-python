"""Generated from Smithy shape ``com.amazonaws.acm#TimestampRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm.types.t_stamp


class TimestampRange(TypedDict):
    start: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The start of the time range. This value is inclusive.</p>"""
    end: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The end of the time range. This value is inclusive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimestampRange) -> dict:
    out: dict = {}
    if "start" in value:
        import aws_sdk_acm.types.t_stamp

        out["Start"] = aws_sdk_acm.types.t_stamp.serialize_aws_json_1_1(value["start"])
    if "end" in value:
        import aws_sdk_acm.types.t_stamp

        out["End"] = aws_sdk_acm.types.t_stamp.serialize_aws_json_1_1(value["end"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TimestampRange:
    out: TimestampRange = {}  # type: ignore[typeddict-item]
    if "Start" in data:
        import aws_sdk_acm.types.t_stamp

        out["start"] = aws_sdk_acm.types.t_stamp.deserialize_aws_json_1_1(data["Start"])
    if "End" in data:
        import aws_sdk_acm.types.t_stamp

        out["end"] = aws_sdk_acm.types.t_stamp.deserialize_aws_json_1_1(data["End"])
    return out
