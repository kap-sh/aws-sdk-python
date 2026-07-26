"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.network_resource

NetworkResourceList: TypeAlias = list[
    "capo_networkmanager.types.network_resource.NetworkResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkResourceList) -> list:
    import capo_networkmanager.types.network_resource

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.network_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkResourceList:
    import capo_networkmanager.types.network_resource

    out: NetworkResourceList = []
    for item in data:
        out.append(capo_networkmanager.types.network_resource.deserialize_json(item))
    return out
