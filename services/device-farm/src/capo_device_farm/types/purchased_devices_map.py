"""Generated from Smithy shape ``com.amazonaws.devicefarm#PurchasedDevicesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.device_platform
    import capo_device_farm.types.integer

PurchasedDevicesMap: TypeAlias = dict[
    "capo_device_farm.types.device_platform.DevicePlatform",
    "capo_device_farm.types.integer.Integer",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PurchasedDevicesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_device_farm.types.device_platform

        out[capo_device_farm.types.device_platform.serialize_aws_json_1_1(key)] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> PurchasedDevicesMap:
    out: PurchasedDevicesMap = {}
    for key, value in data.items():
        import capo_device_farm.types.device_platform

        out[capo_device_farm.types.device_platform.deserialize_aws_json_1_1(key)] = (
            value
        )
    return out
