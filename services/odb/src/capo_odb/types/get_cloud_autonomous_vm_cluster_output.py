"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudAutonomousVmClusterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.cloud_autonomous_vm_cluster


class GetCloudAutonomousVmClusterOutput(TypedDict, closed=True):
    cloud_autonomous_vm_cluster: NotRequired[
        "capo_odb.types.cloud_autonomous_vm_cluster.CloudAutonomousVmCluster"
    ]
    """<p>The details of the requested Autonomous VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCloudAutonomousVmClusterOutput) -> dict:
    out: dict = {}
    if "cloud_autonomous_vm_cluster" in value:
        import capo_odb.types.cloud_autonomous_vm_cluster

        out["cloudAutonomousVmCluster"] = (
            capo_odb.types.cloud_autonomous_vm_cluster.serialize_aws_json_1_0(
                value["cloud_autonomous_vm_cluster"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCloudAutonomousVmClusterOutput:
    out: GetCloudAutonomousVmClusterOutput = {}  # type: ignore[typeddict-item]
    if "cloudAutonomousVmCluster" in data:
        import capo_odb.types.cloud_autonomous_vm_cluster

        out["cloud_autonomous_vm_cluster"] = (
            capo_odb.types.cloud_autonomous_vm_cluster.deserialize_aws_json_1_0(
                data["cloudAutonomousVmCluster"]
            )
        )
    return out
