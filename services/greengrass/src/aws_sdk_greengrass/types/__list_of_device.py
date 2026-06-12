"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfDevice``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.device

__listOfDevice: TypeAlias = list["aws_sdk_greengrass.types.device.Device"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDevice) -> list:
    import aws_sdk_greengrass.types.device

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrass.types.device.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDevice:
    import aws_sdk_greengrass.types.device

    out: __listOfDevice = []
    for item in data:
        out.append(aws_sdk_greengrass.types.device.deserialize_json(item))
    return out
