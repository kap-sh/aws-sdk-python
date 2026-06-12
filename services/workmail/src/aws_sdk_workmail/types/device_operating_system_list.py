"""Generated from Smithy shape ``com.amazonaws.workmail#DeviceOperatingSystemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.device_operating_system

DeviceOperatingSystemList: TypeAlias = list[
    "aws_sdk_workmail.types.device_operating_system.DeviceOperatingSystem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceOperatingSystemList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeviceOperatingSystemList:
    return list(data)
