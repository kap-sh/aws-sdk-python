"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeviceDiscoveryListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.device_discovery_summary

DeviceDiscoveryListDefinition: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.device_discovery_summary.DeviceDiscoverySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceDiscoveryListDefinition) -> list:
    import aws_sdk_iot_managed_integrations.types.device_discovery_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.device_discovery_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DeviceDiscoveryListDefinition:
    import aws_sdk_iot_managed_integrations.types.device_discovery_summary

    out: DeviceDiscoveryListDefinition = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.device_discovery_summary.deserialize_json(
                item
            )
        )
    return out
