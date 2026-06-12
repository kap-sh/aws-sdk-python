"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#InboundCrossClusterSearchConnections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connection

InboundCrossClusterSearchConnections: TypeAlias = list[
    "aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connection.InboundCrossClusterSearchConnection"
]


# --- restJson1 ser/de ---
def serialize_json(value: InboundCrossClusterSearchConnections) -> list:
    import aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connection

    out: list = []
    for item in value:
        out.append(
            aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connection.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InboundCrossClusterSearchConnections:
    import aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connection

    out: InboundCrossClusterSearchConnections = []
    for item in data:
        out.append(
            aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connection.deserialize_json(
                item
            )
        )
    return out
