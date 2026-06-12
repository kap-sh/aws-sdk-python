"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CoreDevicesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.core_device

CoreDevicesList: TypeAlias = list["aws_sdk_greengrassv2.types.core_device.CoreDevice"]


# --- restJson1 ser/de ---
def serialize_json(value: CoreDevicesList) -> list:
    import aws_sdk_greengrassv2.types.core_device

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrassv2.types.core_device.serialize_json(item))
    return out


def deserialize_json(data: list) -> CoreDevicesList:
    import aws_sdk_greengrassv2.types.core_device

    out: CoreDevicesList = []
    for item in data:
        out.append(aws_sdk_greengrassv2.types.core_device.deserialize_json(item))
    return out
