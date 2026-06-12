"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CapabilityReportProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.property_name

CapabilityReportProperties: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.property_name.PropertyName"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityReportProperties) -> list:
    return list(value)


def deserialize_json(data: list) -> CapabilityReportProperties:
    return list(data)
