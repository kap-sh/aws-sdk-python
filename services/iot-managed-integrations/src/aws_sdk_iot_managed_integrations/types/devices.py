"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#Devices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.device

Devices: TypeAlias = list["aws_sdk_iot_managed_integrations.types.device.Device"]


# --- restJson1 ser/de ---
def serialize_json(value: Devices) -> list:
    import aws_sdk_iot_managed_integrations.types.device

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_managed_integrations.types.device.serialize_json(item))
    return out


def deserialize_json(data: list) -> Devices:
    import aws_sdk_iot_managed_integrations.types.device

    out: Devices = []
    for item in data:
        out.append(aws_sdk_iot_managed_integrations.types.device.deserialize_json(item))
    return out
