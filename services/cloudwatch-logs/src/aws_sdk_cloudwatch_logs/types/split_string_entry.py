"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SplitStringEntry``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.source
    import aws_sdk_cloudwatch_logs.types.split_string_delimiter


class SplitStringEntry(TypedDict):
    source: "aws_sdk_cloudwatch_logs.types.source.Source"
    """<p>The key of the field to split.</p>"""
    delimiter: (
        "aws_sdk_cloudwatch_logs.types.split_string_delimiter.SplitStringDelimiter"
    )
    """<p>The separator characters to split the string entry on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplitStringEntry) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["delimiter"] = value["delimiter"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SplitStringEntry:
    out: SplitStringEntry = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("SplitStringEntry.source required")
    if "delimiter" in data:
        out["delimiter"] = data["delimiter"]
    else:
        raise DeserializationError("SplitStringEntry.delimiter required")
    return out
