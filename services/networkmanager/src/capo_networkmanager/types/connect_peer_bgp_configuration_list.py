"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerBgpConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.connect_peer_bgp_configuration

ConnectPeerBgpConfigurationList: TypeAlias = list[
    "capo_networkmanager.types.connect_peer_bgp_configuration.ConnectPeerBgpConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerBgpConfigurationList) -> list:
    import capo_networkmanager.types.connect_peer_bgp_configuration

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.connect_peer_bgp_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConnectPeerBgpConfigurationList:
    import capo_networkmanager.types.connect_peer_bgp_configuration

    out: ConnectPeerBgpConfigurationList = []
    for item in data:
        out.append(
            capo_networkmanager.types.connect_peer_bgp_configuration.deserialize_json(
                item
            )
        )
    return out
