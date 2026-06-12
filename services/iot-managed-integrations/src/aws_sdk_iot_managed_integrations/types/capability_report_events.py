"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CapabilityReportEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.event_name

CapabilityReportEvents: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.event_name.EventName"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityReportEvents) -> list:
    return list(value)


def deserialize_json(data: list) -> CapabilityReportEvents:
    return list(data)
