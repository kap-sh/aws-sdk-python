"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReportClusters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_cluster

MatterCapabilityReportClusters: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.matter_capability_report_cluster.MatterCapabilityReportCluster"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReportClusters) -> list:
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_cluster

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.matter_capability_report_cluster.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MatterCapabilityReportClusters:
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_cluster

    out: MatterCapabilityReportClusters = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.matter_capability_report_cluster.deserialize_json(
                item
            )
        )
    return out
