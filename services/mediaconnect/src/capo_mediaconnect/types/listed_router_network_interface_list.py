"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedRouterNetworkInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.listed_router_network_interface

ListedRouterNetworkInterfaceList: TypeAlias = list[
    "capo_mediaconnect.types.listed_router_network_interface.ListedRouterNetworkInterface"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListedRouterNetworkInterfaceList) -> list:
    import capo_mediaconnect.types.listed_router_network_interface

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.listed_router_network_interface.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListedRouterNetworkInterfaceList:
    import capo_mediaconnect.types.listed_router_network_interface

    out: ListedRouterNetworkInterfaceList = []
    for item in data:
        out.append(
            capo_mediaconnect.types.listed_router_network_interface.deserialize_json(
                item
            )
        )
    return out
