"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkFunctionGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.network_function_group

NetworkFunctionGroupList: TypeAlias = list[
    "aws_sdk_networkmanager.types.network_function_group.NetworkFunctionGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkFunctionGroupList) -> list:
    import aws_sdk_networkmanager.types.network_function_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.network_function_group.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkFunctionGroupList:
    import aws_sdk_networkmanager.types.network_function_group

    out: NetworkFunctionGroupList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.network_function_group.deserialize_json(item)
        )
    return out
