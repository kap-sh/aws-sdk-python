"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetQueryResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.get_query_results_max_items
    import aws_sdk_cloudwatch_logs.types.get_query_results_next_token
    import aws_sdk_cloudwatch_logs.types.query_id


class GetQueryResultsRequest(TypedDict, closed=True):
    query_id: "aws_sdk_cloudwatch_logs.types.query_id.QueryId"
    """<p>The ID number of the query.</p>"""
    next_token: NotRequired[
        "aws_sdk_cloudwatch_logs.types.get_query_results_next_token.GetQueryResultsNextToken"
    ]
    """<p>The token for the next set of items to return. The token expires after 1 hour.</p>"""
    max_items: NotRequired[
        "aws_sdk_cloudwatch_logs.types.get_query_results_max_items.GetQueryResultsMaxItems"
    ]
    """<p>The maximum number of log events to return in the response. The maximum is 10,000 log events per request. You can retrieve up to 100,000 log event results from a query by paginating with the <code>nextToken</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQueryResultsRequest) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_items" in value:
        out["maxItems"] = value["max_items"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQueryResultsRequest:
    out: GetQueryResultsRequest = {}  # type: ignore[typeddict-item]
    if "queryId" in data:
        out["query_id"] = data["queryId"]
    else:
        raise DeserializationError("GetQueryResultsRequest.query_id required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxItems" in data:
        out["max_items"] = data["maxItems"]
    return out
