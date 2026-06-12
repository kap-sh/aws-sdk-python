"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkRouteDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.network_route_destination

NetworkRouteDestinationList: TypeAlias = list[
    "aws_sdk_networkmanager.types.network_route_destination.NetworkRouteDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkRouteDestinationList) -> list:
    import aws_sdk_networkmanager.types.network_route_destination

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.network_route_destination.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkRouteDestinationList:
    import aws_sdk_networkmanager.types.network_route_destination

    out: NetworkRouteDestinationList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.network_route_destination.deserialize_json(
                item
            )
        )
    return out
