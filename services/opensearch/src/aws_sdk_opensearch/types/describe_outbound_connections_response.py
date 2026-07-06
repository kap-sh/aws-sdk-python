"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeOutboundConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.next_token
    import aws_sdk_opensearch.types.outbound_connections


class DescribeOutboundConnectionsResponse(TypedDict, closed=True):
    connections: NotRequired[
        "aws_sdk_opensearch.types.outbound_connections.OutboundConnections"
    ]
    """<p>List of outbound connections that match the filter criteria.</p>"""
    next_token: NotRequired["aws_sdk_opensearch.types.next_token.NextToken"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOutboundConnectionsResponse) -> dict:
    out: dict = {}
    if "connections" in value:
        import aws_sdk_opensearch.types.outbound_connections

        out["Connections"] = (
            aws_sdk_opensearch.types.outbound_connections.serialize_json(
                value["connections"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeOutboundConnectionsResponse:
    out: DescribeOutboundConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "Connections" in data:
        import aws_sdk_opensearch.types.outbound_connections

        out["connections"] = (
            aws_sdk_opensearch.types.outbound_connections.deserialize_json(
                data["Connections"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
