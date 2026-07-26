"""Generated from Smithy shape ``com.amazonaws.quicksight#NetworkInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.network_interface

NetworkInterfaceList: TypeAlias = list[
    "capo_quicksight.types.network_interface.NetworkInterface"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterfaceList) -> list:
    import capo_quicksight.types.network_interface

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.network_interface.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkInterfaceList:
    import capo_quicksight.types.network_interface

    out: NetworkInterfaceList = []
    for item in data:
        out.append(capo_quicksight.types.network_interface.deserialize_json(item))
    return out
