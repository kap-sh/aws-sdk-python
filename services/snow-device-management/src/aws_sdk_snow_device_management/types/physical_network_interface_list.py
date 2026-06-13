"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#PhysicalNetworkInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.physical_network_interface

PhysicalNetworkInterfaceList: TypeAlias = list[
    "aws_sdk_snow_device_management.types.physical_network_interface.PhysicalNetworkInterface"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalNetworkInterfaceList) -> list:
    import aws_sdk_snow_device_management.types.physical_network_interface

    out: list = []
    for item in value:
        out.append(
            aws_sdk_snow_device_management.types.physical_network_interface.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PhysicalNetworkInterfaceList:
    import aws_sdk_snow_device_management.types.physical_network_interface

    out: PhysicalNetworkInterfaceList = []
    for item in data:
        out.append(
            aws_sdk_snow_device_management.types.physical_network_interface.deserialize_json(
                item
            )
        )
    return out
