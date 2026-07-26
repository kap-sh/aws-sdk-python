"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CoreDevicesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.core_device

CoreDevicesList: TypeAlias = list["capo_greengrassv2.types.core_device.CoreDevice"]


# --- restJson1 ser/de ---
def serialize_json(value: CoreDevicesList) -> list:
    import capo_greengrassv2.types.core_device

    out: list = []
    for item in value:
        out.append(capo_greengrassv2.types.core_device.serialize_json(item))
    return out


def deserialize_json(data: list) -> CoreDevicesList:
    import capo_greengrassv2.types.core_device

    out: CoreDevicesList = []
    for item in data:
        out.append(capo_greengrassv2.types.core_device.deserialize_json(item))
    return out
