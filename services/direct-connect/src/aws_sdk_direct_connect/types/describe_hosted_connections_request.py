"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeHostedConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.connection_id
    import aws_sdk_direct_connect.types.max_result_set_size
    import aws_sdk_direct_connect.types.pagination_token


class DescribeHostedConnectionsRequest(TypedDict, closed=True):
    connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the interconnect or LAG.</p>"""
    max_results: NotRequired[
        "aws_sdk_direct_connect.types.max_result_set_size.MaxResultSetSize"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHostedConnectionsRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHostedConnectionsRequest:
    out: DescribeHostedConnectionsRequest = {}  # type: ignore[typeddict-item]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError(
            "DescribeHostedConnectionsRequest.connection_id required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
