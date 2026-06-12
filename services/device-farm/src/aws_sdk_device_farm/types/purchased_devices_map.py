"""Generated from Smithy shape ``com.amazonaws.devicefarm#PurchasedDevicesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_platform
    import aws_sdk_device_farm.types.integer

PurchasedDevicesMap: TypeAlias = dict[
    "aws_sdk_device_farm.types.device_platform.DevicePlatform",
    "aws_sdk_device_farm.types.integer.Integer",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PurchasedDevicesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_device_farm.types.device_platform

        out[aws_sdk_device_farm.types.device_platform.serialize_aws_json_1_1(key)] = (
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PurchasedDevicesMap:
    out: PurchasedDevicesMap = {}
    for key, value in data.items():
        import aws_sdk_device_farm.types.device_platform

        out[aws_sdk_device_farm.types.device_platform.deserialize_aws_json_1_1(key)] = (
            value
        )
    return out
