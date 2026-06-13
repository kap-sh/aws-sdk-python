"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_network_interface_filter

RouterNetworkInterfaceFilterList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.router_network_interface_filter.RouterNetworkInterfaceFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterfaceFilterList) -> list:
    import aws_sdk_mediaconnect.types.router_network_interface_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.router_network_interface_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouterNetworkInterfaceFilterList:
    import aws_sdk_mediaconnect.types.router_network_interface_filter

    out: RouterNetworkInterfaceFilterList = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.router_network_interface_filter.deserialize_json(
                item
            )
        )
    return out
