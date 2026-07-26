"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UpdateLookupTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.timestamp


class UpdateLookupTableResponse(TypedDict, closed=True):
    lookup_table_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the lookup table that was updated.</p>"""
    last_updated_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time when the lookup table was last updated, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLookupTableResponse) -> dict:
    out: dict = {}
    if "lookup_table_arn" in value:
        out["lookupTableArn"] = value["lookup_table_arn"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLookupTableResponse:
    out: UpdateLookupTableResponse = {}  # type: ignore[typeddict-item]
    if "lookupTableArn" in data:
        out["lookup_table_arn"] = data["lookupTableArn"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    return out
