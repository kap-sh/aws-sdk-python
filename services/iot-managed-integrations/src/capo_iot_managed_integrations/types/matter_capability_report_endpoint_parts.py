"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReportEndpointParts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.endpoint_id

MatterCapabilityReportEndpointParts: TypeAlias = list[
    "capo_iot_managed_integrations.types.endpoint_id.EndpointId"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReportEndpointParts) -> list:
    return list(value)


def deserialize_json(data: list) -> MatterCapabilityReportEndpointParts:
    return list(data)
