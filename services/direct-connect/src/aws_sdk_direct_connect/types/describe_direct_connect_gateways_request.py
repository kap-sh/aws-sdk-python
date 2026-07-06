"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeDirectConnectGatewaysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway_id
    import aws_sdk_direct_connect.types.max_result_set_size
    import aws_sdk_direct_connect.types.pagination_token


class DescribeDirectConnectGatewaysRequest(TypedDict, closed=True):
    direct_connect_gateway_id: NotRequired[
        "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    ]
    """<p>The ID of the Direct Connect gateway.</p>"""
    max_results: NotRequired[
        "aws_sdk_direct_connect.types.max_result_set_size.MaxResultSetSize"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token provided in the previous call to retrieve the next page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDirectConnectGatewaysRequest) -> dict:
    out: dict = {}
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDirectConnectGatewaysRequest:
    out: DescribeDirectConnectGatewaysRequest = {}  # type: ignore[typeddict-item]
    if "directConnectGatewayId" in data:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
