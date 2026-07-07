"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeQueriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.describe_queries_max_results
    import aws_sdk_cloudwatch_logs.types.log_group_name
    import aws_sdk_cloudwatch_logs.types.next_token
    import aws_sdk_cloudwatch_logs.types.query_language
    import aws_sdk_cloudwatch_logs.types.query_status


class DescribeQueriesRequest(TypedDict, closed=True):
    log_group_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>Limits the returned queries to only those for the specified log group.</p>"""
    status: NotRequired["aws_sdk_cloudwatch_logs.types.query_status.QueryStatus"]
    """<p>Limits the returned queries to only those that have the specified status. Valid values are <code>Cancelled</code>, <code>Complete</code>, <code>Failed</code>, <code>Running</code>, and <code>Scheduled</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_cloudwatch_logs.types.describe_queries_max_results.DescribeQueriesMaxResults"
    ]
    """<p>Limits the number of returned queries to the specified number.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    query_language: NotRequired[
        "aws_sdk_cloudwatch_logs.types.query_language.QueryLanguage"
    ]
    """<p>Limits the returned queries to only the queries that use the specified query language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeQueriesRequest) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "status" in value:
        import aws_sdk_cloudwatch_logs.types.query_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.query_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "query_language" in value:
        import aws_sdk_cloudwatch_logs.types.query_language

        out["queryLanguage"] = (
            aws_sdk_cloudwatch_logs.types.query_language.serialize_aws_json_1_1(
                value["query_language"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeQueriesRequest:
    out: DescribeQueriesRequest = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "status" in data:
        import aws_sdk_cloudwatch_logs.types.query_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.query_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "queryLanguage" in data:
        import aws_sdk_cloudwatch_logs.types.query_language

        out["query_language"] = (
            aws_sdk_cloudwatch_logs.types.query_language.deserialize_aws_json_1_1(
                data["queryLanguage"]
            )
        )
    return out
