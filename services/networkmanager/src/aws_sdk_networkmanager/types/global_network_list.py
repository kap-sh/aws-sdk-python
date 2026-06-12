"""Generated from Smithy shape ``com.amazonaws.networkmanager#GlobalNetworkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.global_network

GlobalNetworkList: TypeAlias = list[
    "aws_sdk_networkmanager.types.global_network.GlobalNetwork"
]


# --- restJson1 ser/de ---
def serialize_json(value: GlobalNetworkList) -> list:
    import aws_sdk_networkmanager.types.global_network

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.global_network.serialize_json(item))
    return out


def deserialize_json(data: list) -> GlobalNetworkList:
    import aws_sdk_networkmanager.types.global_network

    out: GlobalNetworkList = []
    for item in data:
        out.append(aws_sdk_networkmanager.types.global_network.deserialize_json(item))
    return out
