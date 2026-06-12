"""Generated from Smithy shape ``com.amazonaws.opensearch#CreateOutboundConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.connection_alias
    import aws_sdk_opensearch.types.connection_mode
    import aws_sdk_opensearch.types.connection_properties
    import aws_sdk_opensearch.types.domain_information_container


class CreateOutboundConnectionRequest(TypedDict):
    local_domain_info: "aws_sdk_opensearch.types.domain_information_container.DomainInformationContainer"
    """<p>Name and Region of the source (local) domain.</p>"""
    remote_domain_info: "aws_sdk_opensearch.types.domain_information_container.DomainInformationContainer"
    """<p>Name and Region of the destination (remote) domain.</p>"""
    connection_alias: "aws_sdk_opensearch.types.connection_alias.ConnectionAlias"
    """<p>Name of the connection.</p>"""
    connection_mode: NotRequired[
        "aws_sdk_opensearch.types.connection_mode.ConnectionMode"
    ]
    """<p>The connection mode.</p>"""
    connection_properties: NotRequired[
        "aws_sdk_opensearch.types.connection_properties.ConnectionProperties"
    ]
    """<p>The <code>ConnectionProperties</code> for the outbound connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOutboundConnectionRequest) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.domain_information_container

    out["LocalDomainInfo"] = (
        aws_sdk_opensearch.types.domain_information_container.serialize_json(
            value["local_domain_info"]
        )
    )
    import aws_sdk_opensearch.types.domain_information_container

    out["RemoteDomainInfo"] = (
        aws_sdk_opensearch.types.domain_information_container.serialize_json(
            value["remote_domain_info"]
        )
    )
    out["ConnectionAlias"] = value["connection_alias"]
    if "connection_mode" in value:
        import aws_sdk_opensearch.types.connection_mode

        out["ConnectionMode"] = aws_sdk_opensearch.types.connection_mode.serialize_json(
            value["connection_mode"]
        )
    if "connection_properties" in value:
        import aws_sdk_opensearch.types.connection_properties

        out["ConnectionProperties"] = (
            aws_sdk_opensearch.types.connection_properties.serialize_json(
                value["connection_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateOutboundConnectionRequest:
    out: CreateOutboundConnectionRequest = {}  # type: ignore[typeddict-item]
    if "LocalDomainInfo" in data:
        import aws_sdk_opensearch.types.domain_information_container

        out["local_domain_info"] = (
            aws_sdk_opensearch.types.domain_information_container.deserialize_json(
                data["LocalDomainInfo"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOutboundConnectionRequest.local_domain_info required"
        )
    if "RemoteDomainInfo" in data:
        import aws_sdk_opensearch.types.domain_information_container

        out["remote_domain_info"] = (
            aws_sdk_opensearch.types.domain_information_container.deserialize_json(
                data["RemoteDomainInfo"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOutboundConnectionRequest.remote_domain_info required"
        )
    if "ConnectionAlias" in data:
        out["connection_alias"] = data["ConnectionAlias"]
    else:
        raise DeserializationError(
            "CreateOutboundConnectionRequest.connection_alias required"
        )
    if "ConnectionMode" in data:
        import aws_sdk_opensearch.types.connection_mode

        out["connection_mode"] = (
            aws_sdk_opensearch.types.connection_mode.deserialize_json(
                data["ConnectionMode"]
            )
        )
    if "ConnectionProperties" in data:
        import aws_sdk_opensearch.types.connection_properties

        out["connection_properties"] = (
            aws_sdk_opensearch.types.connection_properties.deserialize_json(
                data["ConnectionProperties"]
            )
        )
    return out
