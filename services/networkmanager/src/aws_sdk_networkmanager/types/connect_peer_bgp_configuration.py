"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerBgpConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.ip_address
    import aws_sdk_networkmanager.types.long


class ConnectPeerBgpConfiguration(TypedDict, closed=True):
    core_network_asn: NotRequired["aws_sdk_networkmanager.types.long.Long"]
    """<p>The ASN of the Coret Network.</p>"""
    peer_asn: NotRequired["aws_sdk_networkmanager.types.long.Long"]
    """<p>The ASN of the Connect peer.</p>"""
    core_network_address: NotRequired[
        "aws_sdk_networkmanager.types.ip_address.IPAddress"
    ]
    """<p>The address of a core network.</p>"""
    peer_address: NotRequired["aws_sdk_networkmanager.types.ip_address.IPAddress"]
    """<p>The address of a core network Connect peer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerBgpConfiguration) -> dict:
    out: dict = {}
    if "core_network_asn" in value:
        out["CoreNetworkAsn"] = value["core_network_asn"]
    if "peer_asn" in value:
        out["PeerAsn"] = value["peer_asn"]
    if "core_network_address" in value:
        out["CoreNetworkAddress"] = value["core_network_address"]
    if "peer_address" in value:
        out["PeerAddress"] = value["peer_address"]
    return out


def deserialize_json(data: dict) -> ConnectPeerBgpConfiguration:
    out: ConnectPeerBgpConfiguration = {}  # type: ignore[typeddict-item]
    if "CoreNetworkAsn" in data:
        out["core_network_asn"] = data["CoreNetworkAsn"]
    if "PeerAsn" in data:
        out["peer_asn"] = data["PeerAsn"]
    if "CoreNetworkAddress" in data:
        out["core_network_address"] = data["CoreNetworkAddress"]
    if "PeerAddress" in data:
        out["peer_address"] = data["PeerAddress"]
    return out
