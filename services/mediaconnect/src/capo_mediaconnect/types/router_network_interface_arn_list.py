"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_network_interface_arn

RouterNetworkInterfaceArnList: TypeAlias = list[
    "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterfaceArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> RouterNetworkInterfaceArnList:
    return list(data)
