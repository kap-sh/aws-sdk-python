"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkResourceCountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.network_resource_count

NetworkResourceCountList: TypeAlias = list[
    "capo_networkmanager.types.network_resource_count.NetworkResourceCount"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkResourceCountList) -> list:
    import capo_networkmanager.types.network_resource_count

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.network_resource_count.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkResourceCountList:
    import capo_networkmanager.types.network_resource_count

    out: NetworkResourceCountList = []
    for item in data:
        out.append(
            capo_networkmanager.types.network_resource_count.deserialize_json(item)
        )
    return out
