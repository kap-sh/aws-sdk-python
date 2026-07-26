"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeLookupTablesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.lookup_tables
    import capo_cloudwatch_logs.types.next_token


class DescribeLookupTablesResponse(TypedDict, closed=True):
    lookup_tables: NotRequired["capo_cloudwatch_logs.types.lookup_tables.LookupTables"]
    """<p>An array of structures, where each structure contains metadata about one lookup table.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLookupTablesResponse) -> dict:
    out: dict = {}
    if "lookup_tables" in value:
        import capo_cloudwatch_logs.types.lookup_tables

        out["lookupTables"] = (
            capo_cloudwatch_logs.types.lookup_tables.serialize_aws_json_1_1(
                value["lookup_tables"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLookupTablesResponse:
    out: DescribeLookupTablesResponse = {}  # type: ignore[typeddict-item]
    if "lookupTables" in data:
        import capo_cloudwatch_logs.types.lookup_tables

        out["lookup_tables"] = (
            capo_cloudwatch_logs.types.lookup_tables.deserialize_aws_json_1_1(
                data["lookupTables"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
