"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeLookupTablesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.describe_lookup_tables_max_results
    import aws_sdk_cloudwatch_logs.types.lookup_table_name
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeLookupTablesRequest(TypedDict, closed=True):
    lookup_table_name_prefix: NotRequired[
        "aws_sdk_cloudwatch_logs.types.lookup_table_name.LookupTableName"
    ]
    """<p>A prefix to filter lookup tables by name. Only tables whose names start with this prefix are returned. If you don't specify a prefix, all tables in the account and Region are returned.</p>"""
    max_results: "aws_sdk_cloudwatch_logs.types.describe_lookup_tables_max_results.DescribeLookupTablesMaxResults"
    """<p>The maximum number of lookup tables to return in the response. The default value is 50 and the maximum value is 100.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLookupTablesRequest) -> dict:
    out: dict = {}
    if "lookup_table_name_prefix" in value:
        out["lookupTableNamePrefix"] = value["lookup_table_name_prefix"]
    out["maxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLookupTablesRequest:
    out: DescribeLookupTablesRequest = {}  # type: ignore[typeddict-item]
    if "lookupTableNamePrefix" in data:
        out["lookup_table_name_prefix"] = data["lookupTableNamePrefix"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 0
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
