"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkRouteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.network_route

NetworkRouteList: TypeAlias = list[
    "aws_sdk_networkmanager.types.network_route.NetworkRoute"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkRouteList) -> list:
    import aws_sdk_networkmanager.types.network_route

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.network_route.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkRouteList:
    import aws_sdk_networkmanager.types.network_route

    out: NetworkRouteList = []
    for item in data:
        out.append(aws_sdk_networkmanager.types.network_route.deserialize_json(item))
    return out
