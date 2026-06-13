"""Generated from Smithy shape ``com.amazonaws.odb#CloudAutonomousVmClusterResourceDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.cloud_autonomous_vm_cluster_resource_details

CloudAutonomousVmClusterResourceDetailsList: TypeAlias = list[
    "aws_sdk_odb.types.cloud_autonomous_vm_cluster_resource_details.CloudAutonomousVmClusterResourceDetails"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudAutonomousVmClusterResourceDetailsList) -> list:
    import aws_sdk_odb.types.cloud_autonomous_vm_cluster_resource_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_odb.types.cloud_autonomous_vm_cluster_resource_details.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CloudAutonomousVmClusterResourceDetailsList:
    import aws_sdk_odb.types.cloud_autonomous_vm_cluster_resource_details

    out: CloudAutonomousVmClusterResourceDetailsList = []
    for item in data:
        out.append(
            aws_sdk_odb.types.cloud_autonomous_vm_cluster_resource_details.deserialize_aws_json_1_0(
                item
            )
        )
    return out
