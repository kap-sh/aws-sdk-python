"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#PhysicalNetworkInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snow_device_management.types.physical_network_interface

PhysicalNetworkInterfaceList: TypeAlias = list[
    "capo_snow_device_management.types.physical_network_interface.PhysicalNetworkInterface"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalNetworkInterfaceList) -> list:
    import capo_snow_device_management.types.physical_network_interface

    out: list = []
    for item in value:
        out.append(
            capo_snow_device_management.types.physical_network_interface.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PhysicalNetworkInterfaceList:
    import capo_snow_device_management.types.physical_network_interface

    out: PhysicalNetworkInterfaceList = []
    for item in data:
        out.append(
            capo_snow_device_management.types.physical_network_interface.deserialize_json(
                item
            )
        )
    return out
