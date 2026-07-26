"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_network_interface_type

RouterNetworkInterfaceTypeList: TypeAlias = list[
    "capo_mediaconnect.types.router_network_interface_type.RouterNetworkInterfaceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterfaceTypeList) -> list:
    import capo_mediaconnect.types.router_network_interface_type

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.router_network_interface_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouterNetworkInterfaceTypeList:
    import capo_mediaconnect.types.router_network_interface_type

    out: RouterNetworkInterfaceTypeList = []
    for item in data:
        out.append(
            capo_mediaconnect.types.router_network_interface_type.deserialize_json(item)
        )
    return out
