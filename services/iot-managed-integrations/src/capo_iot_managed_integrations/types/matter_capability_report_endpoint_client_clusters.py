"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReportEndpointClientClusters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.cluster_id

MatterCapabilityReportEndpointClientClusters: TypeAlias = list[
    "capo_iot_managed_integrations.types.cluster_id.ClusterId"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReportEndpointClientClusters) -> list:
    return list(value)


def deserialize_json(data: list) -> MatterCapabilityReportEndpointClientClusters:
    return list(data)
