"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateLookupTableResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.timestamp


class CreateLookupTableResponse(TypedDict):
    lookup_table_arn: NotRequired["aws_sdk_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the lookup table that was created.</p>"""
    created_at: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time when the lookup table was created, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLookupTableResponse) -> dict:
    out: dict = {}
    if "lookup_table_arn" in value:
        out["lookupTableArn"] = value["lookup_table_arn"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLookupTableResponse:
    out: CreateLookupTableResponse = {}  # type: ignore[typeddict-item]
    if "lookupTableArn" in data:
        out["lookup_table_arn"] = data["lookupTableArn"]
    if "createdAt" in data:
        out["created_at"] = data["createdAt"]
    return out
