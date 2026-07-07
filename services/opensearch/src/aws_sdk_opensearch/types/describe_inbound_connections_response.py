"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeInboundConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.inbound_connections
    import aws_sdk_opensearch.types.next_token


class DescribeInboundConnectionsResponse(TypedDict, closed=True):
    connections: NotRequired[
        "aws_sdk_opensearch.types.inbound_connections.InboundConnections"
    ]
    """<p>List of inbound connections.</p>"""
    next_token: NotRequired["aws_sdk_opensearch.types.next_token.NextToken"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInboundConnectionsResponse) -> dict:
    out: dict = {}
    if "connections" in value:
        import aws_sdk_opensearch.types.inbound_connections

        out["Connections"] = (
            aws_sdk_opensearch.types.inbound_connections.serialize_json(
                value["connections"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeInboundConnectionsResponse:
    out: DescribeInboundConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "Connections" in data:
        import aws_sdk_opensearch.types.inbound_connections

        out["connections"] = (
            aws_sdk_opensearch.types.inbound_connections.deserialize_json(
                data["Connections"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
