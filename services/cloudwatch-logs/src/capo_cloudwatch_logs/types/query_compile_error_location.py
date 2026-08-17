"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryCompileErrorLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.query_char_offset


class QueryCompileErrorLocation(TypedDict, closed=True):
    start_char_offset: NotRequired[
        "capo_cloudwatch_logs.types.query_char_offset.QueryCharOffset"
    ]
    """<p>Reserved.</p>"""
    end_char_offset: NotRequired[
        "capo_cloudwatch_logs.types.query_char_offset.QueryCharOffset"
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
    if data.get("startCharOffset") is not None:
        out["start_char_offset"] = data["startCharOffset"]
    if data.get("endCharOffset") is not None:
        out["end_char_offset"] = data["endCharOffset"]
    return out
