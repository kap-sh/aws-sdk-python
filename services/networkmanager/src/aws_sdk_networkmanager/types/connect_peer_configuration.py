"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_peer_bgp_configuration_list
    import aws_sdk_networkmanager.types.constrained_string_list
    import aws_sdk_networkmanager.types.ip_address
    import aws_sdk_networkmanager.types.tunnel_protocol


class ConnectPeerConfiguration(TypedDict, closed=True):
    core_network_address: NotRequired[
        "aws_sdk_networkmanager.types.ip_address.IPAddress"
    ]
    """<p>The IP address of a core network.</p>"""
    peer_address: NotRequired["aws_sdk_networkmanager.types.ip_address.IPAddress"]
    """<p>The IP address of the Connect peer.</p>"""
    inside_cidr_blocks: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The inside IP addresses used for a Connect peer configuration.</p>"""
    protocol: NotRequired["aws_sdk_networkmanager.types.tunnel_protocol.TunnelProtocol"]
    """<p>The protocol used for a Connect peer configuration.</p>"""
    bgp_configurations: NotRequired[
        "aws_sdk_networkmanager.types.connect_peer_bgp_configuration_list.ConnectPeerBgpConfigurationList"
    ]
    """<p>The Connect peer BGP configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerConfiguration) -> dict:
    out: dict = {}
    if "core_network_address" in value:
        out["CoreNetworkAddress"] = value["core_network_address"]
    if "peer_address" in value:
        out["PeerAddress"] = value["peer_address"]
    if "inside_cidr_blocks" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["InsideCidrBlocks"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["inside_cidr_blocks"]
            )
        )
    if "protocol" in value:
        import aws_sdk_networkmanager.types.tunnel_protocol

        out["Protocol"] = aws_sdk_networkmanager.types.tunnel_protocol.serialize_json(
            value["protocol"]
        )
    if "bgp_configurations" in value:
        import aws_sdk_networkmanager.types.connect_peer_bgp_configuration_list

        out["BgpConfigurations"] = (
            aws_sdk_networkmanager.types.connect_peer_bgp_configuration_list.serialize_json(
                value["bgp_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectPeerConfiguration:
    out: ConnectPeerConfiguration = {}  # type: ignore[typeddict-item]
    if "CoreNetworkAddress" in data:
        out["core_network_address"] = data["CoreNetworkAddress"]
    if "PeerAddress" in data:
        out["peer_address"] = data["PeerAddress"]
    if "InsideCidrBlocks" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["inside_cidr_blocks"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["InsideCidrBlocks"]
            )
        )
    if "Protocol" in data:
        import aws_sdk_networkmanager.types.tunnel_protocol

        out["protocol"] = aws_sdk_networkmanager.types.tunnel_protocol.deserialize_json(
            data["Protocol"]
        )
    if "BgpConfigurations" in data:
        import aws_sdk_networkmanager.types.connect_peer_bgp_configuration_list

        out["bgp_configurations"] = (
            aws_sdk_networkmanager.types.connect_peer_bgp_configuration_list.deserialize_json(
                data["BgpConfigurations"]
            )
        )
    return out
