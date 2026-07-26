"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#NeighborConnectionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_discovery_service.types.boxed_integer
    import capo_application_discovery_service.types.configuration_id
    import capo_application_discovery_service.types.long
    import capo_application_discovery_service.types.string


class NeighborConnectionDetail(TypedDict, closed=True):
    source_server_id: (
        "capo_application_discovery_service.types.configuration_id.ConfigurationId"
    )
    """<p>The ID of the server that opened the network connection.</p>"""
    destination_server_id: (
        "capo_application_discovery_service.types.configuration_id.ConfigurationId"
    )
    """<p>The ID of the server that accepted the network connection.</p>"""
    destination_port: NotRequired[
        "capo_application_discovery_service.types.boxed_integer.BoxedInteger"
    ]
    """<p>The destination network port for the connection.</p>"""
    transport_protocol: NotRequired[
        "capo_application_discovery_service.types.string.String"
    ]
    """<p>The network protocol used for the connection.</p>"""
    connections_count: "capo_application_discovery_service.types.long.Long"
    """<p>The number of open network connections with the neighboring server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NeighborConnectionDetail) -> dict:
    out: dict = {}
    out["sourceServerId"] = value["source_server_id"]
    out["destinationServerId"] = value["destination_server_id"]
    if "destination_port" in value:
        out["destinationPort"] = value["destination_port"]
    if "transport_protocol" in value:
        out["transportProtocol"] = value["transport_protocol"]
    out["connectionsCount"] = value.get("connections_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> NeighborConnectionDetail:
    out: NeighborConnectionDetail = {}  # type: ignore[typeddict-item]
    if "sourceServerId" in data:
        out["source_server_id"] = data["sourceServerId"]
    else:
        raise DeserializationError("NeighborConnectionDetail.source_server_id required")
    if "destinationServerId" in data:
        out["destination_server_id"] = data["destinationServerId"]
    else:
        raise DeserializationError(
            "NeighborConnectionDetail.destination_server_id required"
        )
    if "destinationPort" in data:
        out["destination_port"] = data["destinationPort"]
    if "transportProtocol" in data:
        out["transport_protocol"] = data["transportProtocol"]
    if "connectionsCount" in data:
        out["connections_count"] = data["connectionsCount"]
    else:
        out["connections_count"] = 0
    return out
