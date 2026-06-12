"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DeleteOutboundCrossClusterSearchConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_id


class DeleteOutboundCrossClusterSearchConnectionRequest(TypedDict):
    cross_cluster_search_connection_id: "aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId"
    """<p>The id of the outbound connection that you want to permanently delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOutboundCrossClusterSearchConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteOutboundCrossClusterSearchConnectionRequest:
    out: DeleteOutboundCrossClusterSearchConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
