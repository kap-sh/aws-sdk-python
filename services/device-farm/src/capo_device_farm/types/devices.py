"""Generated from Smithy shape ``com.amazonaws.devicefarm#Devices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.device

Devices: TypeAlias = list["capo_device_farm.types.device.Device"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Devices) -> list:
    import capo_device_farm.types.device

    out: list = []
    for item in value:
        out.append(capo_device_farm.types.device.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Devices:
    import capo_device_farm.types.device

    out: Devices = []
    for item in data:
        out.append(capo_device_farm.types.device.deserialize_aws_json_1_1(item))
    return out
