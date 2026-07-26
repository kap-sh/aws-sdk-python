"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeOutboundCrossClusterSearchConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.next_token
    import capo_elasticsearch_service.types.outbound_cross_cluster_search_connections


class DescribeOutboundCrossClusterSearchConnectionsResponse(TypedDict, closed=True):
    cross_cluster_search_connections: NotRequired[
        "capo_elasticsearch_service.types.outbound_cross_cluster_search_connections.OutboundCrossClusterSearchConnections"
    ]
    """<p>Consists of list of <code><a>OutboundCrossClusterSearchConnection</a></code> matching the specified filter criteria.</p>"""
    next_token: NotRequired["capo_elasticsearch_service.types.next_token.NextToken"]
    """<p>If more results are available and NextToken is present, make the next request to the same API with the received NextToken to paginate the remaining results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: DescribeOutboundCrossClusterSearchConnectionsResponse,
) -> dict:
    out: dict = {}
    if "cross_cluster_search_connections" in value:
        import capo_elasticsearch_service.types.outbound_cross_cluster_search_connections

        out["CrossClusterSearchConnections"] = (
            capo_elasticsearch_service.types.outbound_cross_cluster_search_connections.serialize_json(
                value["cross_cluster_search_connections"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(
    data: dict,
) -> DescribeOutboundCrossClusterSearchConnectionsResponse:
    out: DescribeOutboundCrossClusterSearchConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "CrossClusterSearchConnections" in data:
        import capo_elasticsearch_service.types.outbound_cross_cluster_search_connections

        out["cross_cluster_search_connections"] = (
            capo_elasticsearch_service.types.outbound_cross_cluster_search_connections.deserialize_json(
                data["CrossClusterSearchConnections"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
