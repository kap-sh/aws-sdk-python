"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudVmClusterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.cloud_vm_cluster


class GetCloudVmClusterOutput(TypedDict, closed=True):
    cloud_vm_cluster: NotRequired["aws_sdk_odb.types.cloud_vm_cluster.CloudVmCluster"]
    """<p>The VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCloudVmClusterOutput) -> dict:
    out: dict = {}
    if "cloud_vm_cluster" in value:
        import aws_sdk_odb.types.cloud_vm_cluster

        out["cloudVmCluster"] = (
            aws_sdk_odb.types.cloud_vm_cluster.serialize_aws_json_1_0(
                value["cloud_vm_cluster"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCloudVmClusterOutput:
    out: GetCloudVmClusterOutput = {}  # type: ignore[typeddict-item]
    if "cloudVmCluster" in data:
        import aws_sdk_odb.types.cloud_vm_cluster

        out["cloud_vm_cluster"] = (
            aws_sdk_odb.types.cloud_vm_cluster.deserialize_aws_json_1_0(
                data["cloudVmCluster"]
            )
        )
    return out
