"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AcceptInboundCrossClusterSearchConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_id


class AcceptInboundCrossClusterSearchConnectionRequest(TypedDict):
    cross_cluster_search_connection_id: "aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId"
    """<p>The id of the inbound connection that you want to accept.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptInboundCrossClusterSearchConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AcceptInboundCrossClusterSearchConnectionRequest:
    out: AcceptInboundCrossClusterSearchConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
