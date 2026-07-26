"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReportEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.matter_event_id

MatterCapabilityReportEvents: TypeAlias = list[
    "capo_iot_managed_integrations.types.matter_event_id.MatterEventId"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReportEvents) -> list:
    return list(value)


def deserialize_json(data: list) -> MatterCapabilityReportEvents:
    return list(data)
