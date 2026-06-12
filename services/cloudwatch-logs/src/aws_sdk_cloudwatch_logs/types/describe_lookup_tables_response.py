"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeLookupTablesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.lookup_tables
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeLookupTablesResponse(TypedDict):
    lookup_tables: NotRequired[
        "aws_sdk_cloudwatch_logs.types.lookup_tables.LookupTables"
    ]
    """<p>An array of structures, where each structure contains metadata about one lookup table.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLookupTablesResponse) -> dict:
    out: dict = {}
    if "lookup_tables" in value:
        import aws_sdk_cloudwatch_logs.types.lookup_tables

        out["lookupTables"] = (
            aws_sdk_cloudwatch_logs.types.lookup_tables.serialize_aws_json_1_1(
                value["lookup_tables"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLookupTablesResponse:
    out: DescribeLookupTablesResponse = {}  # type: ignore[typeddict-item]
    if "lookupTables" in data:
        import aws_sdk_cloudwatch_logs.types.lookup_tables

        out["lookup_tables"] = (
            aws_sdk_cloudwatch_logs.types.lookup_tables.deserialize_aws_json_1_1(
                data["lookupTables"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
