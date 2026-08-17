"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateLookupTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.timestamp


class CreateLookupTableResponse(TypedDict, closed=True):
    lookup_table_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the lookup table that was created.</p>"""
    created_at: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
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
    if data.get("lookupTableArn") is not None:
        out["lookup_table_arn"] = data["lookupTableArn"]
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    return out
