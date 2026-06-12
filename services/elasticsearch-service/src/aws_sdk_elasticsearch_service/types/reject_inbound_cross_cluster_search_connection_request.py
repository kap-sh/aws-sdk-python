"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#RejectInboundCrossClusterSearchConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_id


class RejectInboundCrossClusterSearchConnectionRequest(TypedDict):
    cross_cluster_search_connection_id: "aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId"
    """<p>The id of the inbound connection that you want to reject.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectInboundCrossClusterSearchConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RejectInboundCrossClusterSearchConnectionRequest:
    out: RejectInboundCrossClusterSearchConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
