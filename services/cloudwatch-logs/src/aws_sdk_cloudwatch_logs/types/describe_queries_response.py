"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeQueriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.next_token
    import aws_sdk_cloudwatch_logs.types.query_info_list


class DescribeQueriesResponse(TypedDict, closed=True):
    queries: NotRequired["aws_sdk_cloudwatch_logs.types.query_info_list.QueryInfoList"]
    """<p>The list of queries that match the request.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeQueriesResponse) -> dict:
    out: dict = {}
    if "queries" in value:
        import aws_sdk_cloudwatch_logs.types.query_info_list

        out["queries"] = (
            aws_sdk_cloudwatch_logs.types.query_info_list.serialize_aws_json_1_1(
                value["queries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeQueriesResponse:
    out: DescribeQueriesResponse = {}  # type: ignore[typeddict-item]
    if "queries" in data:
        import aws_sdk_cloudwatch_logs.types.query_info_list

        out["queries"] = (
            aws_sdk_cloudwatch_logs.types.query_info_list.deserialize_aws_json_1_1(
                data["queries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
