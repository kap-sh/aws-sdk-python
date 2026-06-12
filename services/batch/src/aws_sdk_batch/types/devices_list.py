"""Generated from Smithy shape ``com.amazonaws.batch#DevicesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.device

DevicesList: TypeAlias = list["aws_sdk_batch.types.device.Device"]


# --- restJson1 ser/de ---
def serialize_json(value: DevicesList) -> list:
    import aws_sdk_batch.types.device

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.device.serialize_json(item))
    return out


def deserialize_json(data: list) -> DevicesList:
    import aws_sdk_batch.types.device

    out: DevicesList = []
    for item in data:
        out.append(aws_sdk_batch.types.device.deserialize_json(item))
    return out
