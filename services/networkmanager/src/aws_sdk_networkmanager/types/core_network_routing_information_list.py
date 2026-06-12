"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkRoutingInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_routing_information

CoreNetworkRoutingInformationList: TypeAlias = list[
    "aws_sdk_networkmanager.types.core_network_routing_information.CoreNetworkRoutingInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkRoutingInformationList) -> list:
    import aws_sdk_networkmanager.types.core_network_routing_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.core_network_routing_information.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CoreNetworkRoutingInformationList:
    import aws_sdk_networkmanager.types.core_network_routing_information

    out: CoreNetworkRoutingInformationList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.core_network_routing_information.deserialize_json(
                item
            )
        )
    return out
