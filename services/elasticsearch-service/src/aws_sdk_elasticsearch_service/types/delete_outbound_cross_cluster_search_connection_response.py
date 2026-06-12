"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DeleteOutboundCrossClusterSearchConnectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection


class DeleteOutboundCrossClusterSearchConnectionResponse(TypedDict):
    cross_cluster_search_connection: NotRequired[
        "aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection.OutboundCrossClusterSearchConnection"
    ]
    """<p>Specifies the <code><a>OutboundCrossClusterSearchConnection</a></code> of deleted outbound connection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOutboundCrossClusterSearchConnectionResponse) -> dict:
    out: dict = {}
    if "cross_cluster_search_connection" in value:
        import aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection

        out["CrossClusterSearchConnection"] = (
            aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection.serialize_json(
                value["cross_cluster_search_connection"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteOutboundCrossClusterSearchConnectionResponse:
    out: DeleteOutboundCrossClusterSearchConnectionResponse = {}  # type: ignore[typeddict-item]
    if "CrossClusterSearchConnection" in data:
        import aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection

        out["cross_cluster_search_connection"] = (
            aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection.deserialize_json(
                data["CrossClusterSearchConnection"]
            )
        )
    return out
