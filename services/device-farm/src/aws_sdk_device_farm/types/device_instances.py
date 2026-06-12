"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_instance

DeviceInstances: TypeAlias = list[
    "aws_sdk_device_farm.types.device_instance.DeviceInstance"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceInstances) -> list:
    import aws_sdk_device_farm.types.device_instance

    out: list = []
    for item in value:
        out.append(
            aws_sdk_device_farm.types.device_instance.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeviceInstances:
    import aws_sdk_device_farm.types.device_instance

    out: DeviceInstances = []
    for item in data:
        out.append(
            aws_sdk_device_farm.types.device_instance.deserialize_aws_json_1_1(item)
        )
    return out
