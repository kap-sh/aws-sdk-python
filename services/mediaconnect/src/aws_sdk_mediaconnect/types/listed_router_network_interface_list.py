"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedRouterNetworkInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.listed_router_network_interface

ListedRouterNetworkInterfaceList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.listed_router_network_interface.ListedRouterNetworkInterface"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListedRouterNetworkInterfaceList) -> list:
    import aws_sdk_mediaconnect.types.listed_router_network_interface

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.listed_router_network_interface.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListedRouterNetworkInterfaceList:
    import aws_sdk_mediaconnect.types.listed_router_network_interface

    out: ListedRouterNetworkInterfaceList = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.listed_router_network_interface.deserialize_json(
                item
            )
        )
    return out
