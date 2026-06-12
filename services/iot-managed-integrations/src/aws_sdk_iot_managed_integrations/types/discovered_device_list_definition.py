"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveredDeviceListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.discovered_device_summary

DiscoveredDeviceListDefinition: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.discovered_device_summary.DiscoveredDeviceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveredDeviceListDefinition) -> list:
    import aws_sdk_iot_managed_integrations.types.discovered_device_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.discovered_device_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DiscoveredDeviceListDefinition:
    import aws_sdk_iot_managed_integrations.types.discovered_device_summary

    out: DiscoveredDeviceListDefinition = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.discovered_device_summary.deserialize_json(
                item
            )
        )
    return out
