"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkNetworkFunctionGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_network_function_group

CoreNetworkNetworkFunctionGroupList: TypeAlias = list[
    "aws_sdk_networkmanager.types.core_network_network_function_group.CoreNetworkNetworkFunctionGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkNetworkFunctionGroupList) -> list:
    import aws_sdk_networkmanager.types.core_network_network_function_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.core_network_network_function_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CoreNetworkNetworkFunctionGroupList:
    import aws_sdk_networkmanager.types.core_network_network_function_group

    out: CoreNetworkNetworkFunctionGroupList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.core_network_network_function_group.deserialize_json(
                item
            )
        )
    return out
