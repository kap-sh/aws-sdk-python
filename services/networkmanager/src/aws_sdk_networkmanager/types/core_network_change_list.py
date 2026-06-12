"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkChangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_change

CoreNetworkChangeList: TypeAlias = list[
    "aws_sdk_networkmanager.types.core_network_change.CoreNetworkChange"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkChangeList) -> list:
    import aws_sdk_networkmanager.types.core_network_change

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.core_network_change.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CoreNetworkChangeList:
    import aws_sdk_networkmanager.types.core_network_change

    out: CoreNetworkChangeList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.core_network_change.deserialize_json(item)
        )
    return out
