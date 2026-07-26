"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CapabilityReportActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.action_name

CapabilityReportActions: TypeAlias = list[
    "capo_iot_managed_integrations.types.action_name.ActionName"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityReportActions) -> list:
    return list(value)


def deserialize_json(data: list) -> CapabilityReportActions:
    return list(data)
