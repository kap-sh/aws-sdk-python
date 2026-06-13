"""Generated from Smithy shape ``com.amazonaws.odb#CloudVmClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.cloud_vm_cluster_summary

CloudVmClusterList: TypeAlias = list[
    "aws_sdk_odb.types.cloud_vm_cluster_summary.CloudVmClusterSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudVmClusterList) -> list:
    import aws_sdk_odb.types.cloud_vm_cluster_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_odb.types.cloud_vm_cluster_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CloudVmClusterList:
    import aws_sdk_odb.types.cloud_vm_cluster_summary

    out: CloudVmClusterList = []
    for item in data:
        out.append(
            aws_sdk_odb.types.cloud_vm_cluster_summary.deserialize_aws_json_1_0(item)
        )
    return out
