"""Generated from Smithy shape ``com.amazonaws.opensearch#InboundConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.connection_id
    import capo_opensearch.types.connection_mode
    import capo_opensearch.types.domain_information_container
    import capo_opensearch.types.inbound_connection_status


class InboundConnection(TypedDict, closed=True):
    local_domain_info: NotRequired[
        "capo_opensearch.types.domain_information_container.DomainInformationContainer"
    ]
    """<p>Information about the source (local) domain.</p>"""
    remote_domain_info: NotRequired[
        "capo_opensearch.types.domain_information_container.DomainInformationContainer"
    ]
    """<p>Information about the destination (remote) domain.</p>"""
    connection_id: NotRequired["capo_opensearch.types.connection_id.ConnectionId"]
    """<p>The unique identifier of the connection.</p>"""
    connection_status: NotRequired[
        "capo_opensearch.types.inbound_connection_status.InboundConnectionStatus"
    ]
    """<p>The current status of the connection.</p>"""
    connection_mode: NotRequired["capo_opensearch.types.connection_mode.ConnectionMode"]
    """<p>The connection mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InboundConnection) -> dict:
    out: dict = {}
    if "local_domain_info" in value:
        import capo_opensearch.types.domain_information_container

        out["LocalDomainInfo"] = (
            capo_opensearch.types.domain_information_container.serialize_json(
                value["local_domain_info"]
            )
        )
    if "remote_domain_info" in value:
        import capo_opensearch.types.domain_information_container

        out["RemoteDomainInfo"] = (
            capo_opensearch.types.domain_information_container.serialize_json(
                value["remote_domain_info"]
            )
        )
    if "connection_id" in value:
        out["ConnectionId"] = value["connection_id"]
    if "connection_status" in value:
        import capo_opensearch.types.inbound_connection_status

        out["ConnectionStatus"] = (
            capo_opensearch.types.inbound_connection_status.serialize_json(
                value["connection_status"]
            )
        )
    if "connection_mode" in value:
        import capo_opensearch.types.connection_mode

        out["ConnectionMode"] = capo_opensearch.types.connection_mode.serialize_json(
            value["connection_mode"]
        )
    return out


def deserialize_json(data: dict) -> InboundConnection:
    out: InboundConnection = {}  # type: ignore[typeddict-item]
    if "LocalDomainInfo" in data:
        import capo_opensearch.types.domain_information_container

        out["local_domain_info"] = (
            capo_opensearch.types.domain_information_container.deserialize_json(
                data["LocalDomainInfo"]
            )
        )
    if "RemoteDomainInfo" in data:
        import capo_opensearch.types.domain_information_container

        out["remote_domain_info"] = (
            capo_opensearch.types.domain_information_container.deserialize_json(
                data["RemoteDomainInfo"]
            )
        )
    if "ConnectionId" in data:
        out["connection_id"] = data["ConnectionId"]
    if "ConnectionStatus" in data:
        import capo_opensearch.types.inbound_connection_status

        out["connection_status"] = (
            capo_opensearch.types.inbound_connection_status.deserialize_json(
                data["ConnectionStatus"]
            )
        )
    if "ConnectionMode" in data:
        import capo_opensearch.types.connection_mode

        out["connection_mode"] = capo_opensearch.types.connection_mode.deserialize_json(
            data["ConnectionMode"]
        )
    return out
