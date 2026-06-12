"""Generated from Smithy shape ``com.amazonaws.opensearch#InboundConnection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.connection_id
    import aws_sdk_opensearch.types.connection_mode
    import aws_sdk_opensearch.types.domain_information_container
    import aws_sdk_opensearch.types.inbound_connection_status


class InboundConnection(TypedDict):
    local_domain_info: NotRequired[
        "aws_sdk_opensearch.types.domain_information_container.DomainInformationContainer"
    ]
    """<p>Information about the source (local) domain.</p>"""
    remote_domain_info: NotRequired[
        "aws_sdk_opensearch.types.domain_information_container.DomainInformationContainer"
    ]
    """<p>Information about the destination (remote) domain.</p>"""
    connection_id: NotRequired["aws_sdk_opensearch.types.connection_id.ConnectionId"]
    """<p>The unique identifier of the connection.</p>"""
    connection_status: NotRequired[
        "aws_sdk_opensearch.types.inbound_connection_status.InboundConnectionStatus"
    ]
    """<p>The current status of the connection.</p>"""
    connection_mode: NotRequired[
        "aws_sdk_opensearch.types.connection_mode.ConnectionMode"
    ]
    """<p>The connection mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InboundConnection) -> dict:
    out: dict = {}
    if "local_domain_info" in value:
        import aws_sdk_opensearch.types.domain_information_container

        out["LocalDomainInfo"] = (
            aws_sdk_opensearch.types.domain_information_container.serialize_json(
                value["local_domain_info"]
            )
        )
    if "remote_domain_info" in value:
        import aws_sdk_opensearch.types.domain_information_container

        out["RemoteDomainInfo"] = (
            aws_sdk_opensearch.types.domain_information_container.serialize_json(
                value["remote_domain_info"]
            )
        )
    if "connection_id" in value:
        out["ConnectionId"] = value["connection_id"]
    if "connection_status" in value:
        import aws_sdk_opensearch.types.inbound_connection_status

        out["ConnectionStatus"] = (
            aws_sdk_opensearch.types.inbound_connection_status.serialize_json(
                value["connection_status"]
            )
        )
    if "connection_mode" in value:
        import aws_sdk_opensearch.types.connection_mode

        out["ConnectionMode"] = aws_sdk_opensearch.types.connection_mode.serialize_json(
            value["connection_mode"]
        )
    return out


def deserialize_json(data: dict) -> InboundConnection:
    out: InboundConnection = {}  # type: ignore[typeddict-item]
    if "LocalDomainInfo" in data:
        import aws_sdk_opensearch.types.domain_information_container

        out["local_domain_info"] = (
            aws_sdk_opensearch.types.domain_information_container.deserialize_json(
                data["LocalDomainInfo"]
            )
        )
    if "RemoteDomainInfo" in data:
        import aws_sdk_opensearch.types.domain_information_container

        out["remote_domain_info"] = (
            aws_sdk_opensearch.types.domain_information_container.deserialize_json(
                data["RemoteDomainInfo"]
            )
        )
    if "ConnectionId" in data:
        out["connection_id"] = data["ConnectionId"]
    if "ConnectionStatus" in data:
        import aws_sdk_opensearch.types.inbound_connection_status

        out["connection_status"] = (
            aws_sdk_opensearch.types.inbound_connection_status.deserialize_json(
                data["ConnectionStatus"]
            )
        )
    if "ConnectionMode" in data:
        import aws_sdk_opensearch.types.connection_mode

        out["connection_mode"] = (
            aws_sdk_opensearch.types.connection_mode.deserialize_json(
                data["ConnectionMode"]
            )
        )
    return out
