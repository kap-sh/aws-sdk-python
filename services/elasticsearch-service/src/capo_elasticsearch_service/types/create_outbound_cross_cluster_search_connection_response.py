"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CreateOutboundCrossClusterSearchConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.connection_alias
    import capo_elasticsearch_service.types.cross_cluster_search_connection_id
    import capo_elasticsearch_service.types.domain_information
    import capo_elasticsearch_service.types.outbound_cross_cluster_search_connection_status


class CreateOutboundCrossClusterSearchConnectionResponse(TypedDict, closed=True):
    source_domain_info: NotRequired[
        "capo_elasticsearch_service.types.domain_information.DomainInformation"
    ]
    """<p>Specifies the <code><a>DomainInformation</a></code> for the source Elasticsearch domain.</p>"""
    destination_domain_info: NotRequired[
        "capo_elasticsearch_service.types.domain_information.DomainInformation"
    ]
    """<p>Specifies the <code><a>DomainInformation</a></code> for the destination Elasticsearch domain.</p>"""
    connection_alias: NotRequired[
        "capo_elasticsearch_service.types.connection_alias.ConnectionAlias"
    ]
    """<p>Specifies the connection alias provided during the create connection request.</p>"""
    connection_status: NotRequired[
        "capo_elasticsearch_service.types.outbound_cross_cluster_search_connection_status.OutboundCrossClusterSearchConnectionStatus"
    ]
    """<p>Specifies the <code><a>OutboundCrossClusterSearchConnectionStatus</a></code> for the newly created connection.</p>"""
    cross_cluster_search_connection_id: NotRequired[
        "capo_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId"
    ]
    """<p>Unique id for the created outbound connection, which is used for subsequent operations on connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOutboundCrossClusterSearchConnectionResponse) -> dict:
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
    if "connection_alias" in value:
        out["ConnectionAlias"] = value["connection_alias"]
    if "connection_status" in value:
        import capo_elasticsearch_service.types.outbound_cross_cluster_search_connection_status

        out["ConnectionStatus"] = (
            capo_elasticsearch_service.types.outbound_cross_cluster_search_connection_status.serialize_json(
                value["connection_status"]
            )
        )
    if "cross_cluster_search_connection_id" in value:
        out["CrossClusterSearchConnectionId"] = value[
            "cross_cluster_search_connection_id"
        ]
    return out


def deserialize_json(data: dict) -> CreateOutboundCrossClusterSearchConnectionResponse:
    out: CreateOutboundCrossClusterSearchConnectionResponse = {}  # type: ignore[typeddict-item]
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
    if "ConnectionAlias" in data:
        out["connection_alias"] = data["ConnectionAlias"]
    if "ConnectionStatus" in data:
        import capo_elasticsearch_service.types.outbound_cross_cluster_search_connection_status

        out["connection_status"] = (
            capo_elasticsearch_service.types.outbound_cross_cluster_search_connection_status.deserialize_json(
                data["ConnectionStatus"]
            )
        )
    if "CrossClusterSearchConnectionId" in data:
        out["cross_cluster_search_connection_id"] = data[
            "CrossClusterSearchConnectionId"
        ]
    return out
