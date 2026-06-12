"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeviceProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.device_profile

DeviceProfileList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.device_profile.DeviceProfile"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceProfileList) -> list:
    import aws_sdk_iot_wireless.types.device_profile

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_wireless.types.device_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeviceProfileList:
    import aws_sdk_iot_wireless.types.device_profile

    out: DeviceProfileList = []
    for item in data:
        out.append(aws_sdk_iot_wireless.types.device_profile.deserialize_json(item))
    return out
