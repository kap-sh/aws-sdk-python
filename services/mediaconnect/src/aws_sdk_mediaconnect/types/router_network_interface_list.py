"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_network_interface

RouterNetworkInterfaceList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.router_network_interface.RouterNetworkInterface"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterfaceList) -> list:
    import aws_sdk_mediaconnect.types.router_network_interface

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.router_network_interface.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouterNetworkInterfaceList:
    import aws_sdk_mediaconnect.types.router_network_interface

    out: RouterNetworkInterfaceList = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.router_network_interface.deserialize_json(item)
        )
    return out
