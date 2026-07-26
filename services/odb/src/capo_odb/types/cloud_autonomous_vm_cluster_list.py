"""Generated from Smithy shape ``com.amazonaws.odb#CloudAutonomousVmClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.cloud_autonomous_vm_cluster_summary

CloudAutonomousVmClusterList: TypeAlias = list[
    "capo_odb.types.cloud_autonomous_vm_cluster_summary.CloudAutonomousVmClusterSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudAutonomousVmClusterList) -> list:
    import capo_odb.types.cloud_autonomous_vm_cluster_summary

    out: list = []
    for item in value:
        out.append(
            capo_odb.types.cloud_autonomous_vm_cluster_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CloudAutonomousVmClusterList:
    import capo_odb.types.cloud_autonomous_vm_cluster_summary

    out: CloudAutonomousVmClusterList = []
    for item in data:
        out.append(
            capo_odb.types.cloud_autonomous_vm_cluster_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
