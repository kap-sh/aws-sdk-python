"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#InboundCrossClusterSearchConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.cross_cluster_search_connection_id
    import capo_elasticsearch_service.types.domain_information
    import capo_elasticsearch_service.types.inbound_cross_cluster_search_connection_status


class InboundCrossClusterSearchConnection(TypedDict, closed=True):
    source_domain_info: NotRequired[
        "capo_elasticsearch_service.types.domain_information.DomainInformation"
    ]
    """<p>Specifies the <code><a>DomainInformation</a></code> for the source Elasticsearch domain.</p>"""
    destination_domain_info: NotRequired[
        "capo_elasticsearch_service.types.domain_information.DomainInformation"
    ]
    """<p>Specifies the <code><a>DomainInformation</a></code> for the destination Elasticsearch domain.</p>"""
    cross_cluster_search_connection_id: NotRequired[
        "capo_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId"
    ]
    """<p>Specifies the connection id for the inbound cross-cluster search connection.</p>"""
    connection_status: NotRequired[
        "capo_elasticsearch_service.types.inbound_cross_cluster_search_connection_status.InboundCrossClusterSearchConnectionStatus"
    ]
    """<p>Specifies the <code><a>InboundCrossClusterSearchConnectionStatus</a></code> for the outbound connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InboundCrossClusterSearchConnection) -> dict:
    out: dict = {}
    if "source_domain_info" in value:
        import capo_elasticsearch_service.types.domain_information

        out["SourceDomainInfo"] = (
            capo_elasticsearch_service.types.domain_information.serialize_json(
                value["source_domain_info"]
            )
        )
    if "destination_domain_info" in value:
        import capo_elasticsearch_service.types.domain_information

        out["DestinationDomainInfo"] = (
            capo_elasticsearch_service.types.domain_information.serialize_json(
                value["destination_domain_info"]
            )
        )
    if "cross_cluster_search_connection_id" in value:
        out["CrossClusterSearchConnectionId"] = value[
            "cross_cluster_search_connection_id"
        ]
    if "connection_status" in value:
        import capo_elasticsearch_service.types.inbound_cross_cluster_search_connection_status

        out["ConnectionStatus"] = (
            capo_elasticsearch_service.types.inbound_cross_cluster_search_connection_status.serialize_json(
                value["connection_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> InboundCrossClusterSearchConnection:
    out: InboundCrossClusterSearchConnection = {}  # type: ignore[typeddict-item]
    if "SourceDomainInfo" in data:
        import capo_elasticsearch_service.types.domain_information

        out["source_domain_info"] = (
            capo_elasticsearch_service.types.domain_information.deserialize_json(
                data["SourceDomainInfo"]
            )
        )
    if "DestinationDomainInfo" in data:
        import capo_elasticsearch_service.types.domain_information

        out["destination_domain_info"] = (
            capo_elasticsearch_service.types.domain_information.deserialize_json(
                data["DestinationDomainInfo"]
            )
        )
    if "CrossClusterSearchConnectionId" in data:
        out["cross_cluster_search_connection_id"] = data[
            "CrossClusterSearchConnectionId"
        ]
    if "ConnectionStatus" in data:
        import capo_elasticsearch_service.types.inbound_cross_cluster_search_connection_status

        out["connection_status"] = (
            capo_elasticsearch_service.types.inbound_cross_cluster_search_connection_status.deserialize_json(
                data["ConnectionStatus"]
            )
        )
    return out
