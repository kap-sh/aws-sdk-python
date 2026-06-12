"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.network_resource

NetworkResourceList: TypeAlias = list[
    "aws_sdk_networkmanager.types.network_resource.NetworkResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkResourceList) -> list:
    import aws_sdk_networkmanager.types.network_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.network_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkResourceList:
    import aws_sdk_networkmanager.types.network_resource

    out: NetworkResourceList = []
    for item in data:
        out.append(aws_sdk_networkmanager.types.network_resource.deserialize_json(item))
    return out
