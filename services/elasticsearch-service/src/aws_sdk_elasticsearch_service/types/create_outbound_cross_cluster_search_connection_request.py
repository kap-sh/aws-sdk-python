"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CreateOutboundCrossClusterSearchConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.connection_alias
    import aws_sdk_elasticsearch_service.types.domain_information


class CreateOutboundCrossClusterSearchConnectionRequest(TypedDict):
    source_domain_info: (
        "aws_sdk_elasticsearch_service.types.domain_information.DomainInformation"
    )
    """<p>Specifies the <code><a>DomainInformation</a></code> for the source Elasticsearch domain.</p>"""
    destination_domain_info: (
        "aws_sdk_elasticsearch_service.types.domain_information.DomainInformation"
    )
    """<p>Specifies the <code><a>DomainInformation</a></code> for the destination Elasticsearch domain.</p>"""
    connection_alias: (
        "aws_sdk_elasticsearch_service.types.connection_alias.ConnectionAlias"
    )
    """<p>Specifies the connection alias that will be used by the customer for this connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOutboundCrossClusterSearchConnectionRequest) -> dict:
    out: dict = {}
    import aws_sdk_elasticsearch_service.types.domain_information

    out["SourceDomainInfo"] = (
        aws_sdk_elasticsearch_service.types.domain_information.serialize_json(
            value["source_domain_info"]
        )
    )
    import aws_sdk_elasticsearch_service.types.domain_information

    out["DestinationDomainInfo"] = (
        aws_sdk_elasticsearch_service.types.domain_information.serialize_json(
            value["destination_domain_info"]
        )
    )
    out["ConnectionAlias"] = value["connection_alias"]
    return out


def deserialize_json(data: dict) -> CreateOutboundCrossClusterSearchConnectionRequest:
    out: CreateOutboundCrossClusterSearchConnectionRequest = {}  # type: ignore[typeddict-item]
    if "SourceDomainInfo" in data:
        import aws_sdk_elasticsearch_service.types.domain_information

        out["source_domain_info"] = (
            aws_sdk_elasticsearch_service.types.domain_information.deserialize_json(
                data["SourceDomainInfo"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOutboundCrossClusterSearchConnectionRequest.source_domain_info required"
        )
    if "DestinationDomainInfo" in data:
        import aws_sdk_elasticsearch_service.types.domain_information

        out["destination_domain_info"] = (
            aws_sdk_elasticsearch_service.types.domain_information.deserialize_json(
                data["DestinationDomainInfo"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOutboundCrossClusterSearchConnectionRequest.destination_domain_info required"
        )
    if "ConnectionAlias" in data:
        out["connection_alias"] = data["ConnectionAlias"]
    else:
        raise DeserializationError(
            "CreateOutboundCrossClusterSearchConnectionRequest.connection_alias required"
        )
    return out
