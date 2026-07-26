"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkRoutingInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_routing_information

CoreNetworkRoutingInformationList: TypeAlias = list[
    "capo_networkmanager.types.core_network_routing_information.CoreNetworkRoutingInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkRoutingInformationList) -> list:
    import capo_networkmanager.types.core_network_routing_information

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.core_network_routing_information.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CoreNetworkRoutingInformationList:
    import capo_networkmanager.types.core_network_routing_information

    out: CoreNetworkRoutingInformationList = []
    for item in data:
        out.append(
            capo_networkmanager.types.core_network_routing_information.deserialize_json(
                item
            )
        )
    return out
