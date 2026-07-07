"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeInboundConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.filter_list
    import aws_sdk_opensearch.types.max_results
    import aws_sdk_opensearch.types.next_token


class DescribeInboundConnectionsRequest(TypedDict, closed=True):
    filters: NotRequired["aws_sdk_opensearch.types.filter_list.FilterList"]
    """<p> A list of filters used to match properties for inbound cross-cluster connections.</p>"""
    max_results: "aws_sdk_opensearch.types.max_results.MaxResults"
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>"""
    next_token: NotRequired["aws_sdk_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>DescribeInboundConnections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeInboundConnections</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInboundConnectionsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_opensearch.types.filter_list

        out["Filters"] = aws_sdk_opensearch.types.filter_list.serialize_json(
            value["filters"]
        )
    out["MaxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeInboundConnectionsRequest:
    out: DescribeInboundConnectionsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_opensearch.types.filter_list

        out["filters"] = aws_sdk_opensearch.types.filter_list.deserialize_json(
            data["Filters"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
