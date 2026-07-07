"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DeleteInboundCrossClusterSearchConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_id


class DeleteInboundCrossClusterSearchConnectionRequest(TypedDict, closed=True):
    cross_cluster_search_connection_id: "aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId"
    """<p>The id of the inbound connection that you want to permanently delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInboundCrossClusterSearchConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInboundCrossClusterSearchConnectionRequest:
    out: DeleteInboundCrossClusterSearchConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
