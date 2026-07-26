"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkNetworkFunctionGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_network_function_group

CoreNetworkNetworkFunctionGroupList: TypeAlias = list[
    "capo_networkmanager.types.core_network_network_function_group.CoreNetworkNetworkFunctionGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkNetworkFunctionGroupList) -> list:
    import capo_networkmanager.types.core_network_network_function_group

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.core_network_network_function_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CoreNetworkNetworkFunctionGroupList:
    import capo_networkmanager.types.core_network_network_function_group

    out: CoreNetworkNetworkFunctionGroupList = []
    for item in data:
        out.append(
            capo_networkmanager.types.core_network_network_function_group.deserialize_json(
                item
            )
        )
    return out
