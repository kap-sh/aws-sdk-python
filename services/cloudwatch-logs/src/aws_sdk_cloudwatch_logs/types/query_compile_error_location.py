"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryCompileErrorLocation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.query_char_offset


class QueryCompileErrorLocation(TypedDict):
    start_char_offset: NotRequired[
        "aws_sdk_cloudwatch_logs.types.query_char_offset.QueryCharOffset"
    ]
    """<p>Reserved.</p>"""
    end_char_offset: NotRequired[
        "aws_sdk_cloudwatch_logs.types.query_char_offset.QueryCharOffset"
    ]
    """<p>Reserved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryCompileErrorLocation) -> dict:
    out: dict = {}
    if "start_char_offset" in value:
        out["startCharOffset"] = value["start_char_offset"]
    if "end_char_offset" in value:
        out["endCharOffset"] = value["end_char_offset"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryCompileErrorLocation:
    out: QueryCompileErrorLocation = {}  # type: ignore[typeddict-item]
    if "startCharOffset" in data:
        out["start_char_offset"] = data["startCharOffset"]
    if "endCharOffset" in data:
        out["end_char_offset"] = data["endCharOffset"]
    return out
