"""Generated from Smithy shape ``com.amazonaws.workmail#DeviceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.device_type

DeviceTypeList: TypeAlias = list["aws_sdk_workmail.types.device_type.DeviceType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceTypeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeviceTypeList:
    return list(data)
