"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeInboundCrossClusterSearchConnectionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connections
    import aws_sdk_elasticsearch_service.types.next_token


class DescribeInboundCrossClusterSearchConnectionsResponse(TypedDict):
    cross_cluster_search_connections: NotRequired[
        "aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connections.InboundCrossClusterSearchConnections"
    ]
    """<p>Consists of list of <code><a>InboundCrossClusterSearchConnection</a></code> matching the specified filter criteria.</p>"""
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.next_token.NextToken"]
    """<p>If more results are available and NextToken is present, make the next request to the same API with the received NextToken to paginate the remaining results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInboundCrossClusterSearchConnectionsResponse) -> dict:
    out: dict = {}
    if "cross_cluster_search_connections" in value:
        import aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connections

        out["CrossClusterSearchConnections"] = (
            aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connections.serialize_json(
                value["cross_cluster_search_connections"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(
    data: dict,
) -> DescribeInboundCrossClusterSearchConnectionsResponse:
    out: DescribeInboundCrossClusterSearchConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "CrossClusterSearchConnections" in data:
        import aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connections

        out["cross_cluster_search_connections"] = (
            aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connections.deserialize_json(
                data["CrossClusterSearchConnections"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
