"""Generated from Smithy shape ``com.amazonaws.devicefarm#DevicePools``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_pool

DevicePools: TypeAlias = list["aws_sdk_device_farm.types.device_pool.DevicePool"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DevicePools) -> list:
    import aws_sdk_device_farm.types.device_pool

    out: list = []
    for item in value:
        out.append(aws_sdk_device_farm.types.device_pool.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DevicePools:
    import aws_sdk_device_farm.types.device_pool

    out: DevicePools = []
    for item in data:
        out.append(aws_sdk_device_farm.types.device_pool.deserialize_aws_json_1_1(item))
    return out
