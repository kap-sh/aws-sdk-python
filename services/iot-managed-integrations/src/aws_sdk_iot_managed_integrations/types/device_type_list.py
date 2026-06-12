"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeviceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.device_type

DeviceTypeList: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.device_type.DeviceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> DeviceTypeList:
    return list(data)
