"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerBgpConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_peer_bgp_configuration

ConnectPeerBgpConfigurationList: TypeAlias = list[
    "aws_sdk_networkmanager.types.connect_peer_bgp_configuration.ConnectPeerBgpConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerBgpConfigurationList) -> list:
    import aws_sdk_networkmanager.types.connect_peer_bgp_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.connect_peer_bgp_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConnectPeerBgpConfigurationList:
    import aws_sdk_networkmanager.types.connect_peer_bgp_configuration

    out: ConnectPeerBgpConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.connect_peer_bgp_configuration.deserialize_json(
                item
            )
        )
    return out
