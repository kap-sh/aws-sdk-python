"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#OutboundCrossClusterSearchConnections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection

OutboundCrossClusterSearchConnections: TypeAlias = list[
    "aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection.OutboundCrossClusterSearchConnection"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutboundCrossClusterSearchConnections) -> list:
    import aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection

    out: list = []
    for item in value:
        out.append(
            aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OutboundCrossClusterSearchConnections:
    import aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection

    out: OutboundCrossClusterSearchConnections = []
    for item in data:
        out.append(
            aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection.deserialize_json(
                item
            )
        )
    return out
