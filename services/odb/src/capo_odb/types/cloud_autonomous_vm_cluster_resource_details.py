"""Generated from Smithy shape ``com.amazonaws.odb#CloudAutonomousVmClusterResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id


class CloudAutonomousVmClusterResourceDetails(TypedDict, closed=True):
    cloud_autonomous_vm_cluster_id: NotRequired["capo_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the Autonomous VM cluster.</p>"""
    unallocated_adb_storage_in_t_bs: NotRequired["float"]
    """<p>The amount of unallocated Autonomous Database storage in the Autonomous VM cluster, in terabytes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudAutonomousVmClusterResourceDetails) -> dict:
    out: dict = {}
    if "cloud_autonomous_vm_cluster_id" in value:
        out["cloudAutonomousVmClusterId"] = value["cloud_autonomous_vm_cluster_id"]
    if "unallocated_adb_storage_in_t_bs" in value:
        out["unallocatedAdbStorageInTBs"] = value["unallocated_adb_storage_in_t_bs"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CloudAutonomousVmClusterResourceDetails:
    out: CloudAutonomousVmClusterResourceDetails = {}  # type: ignore[typeddict-item]
    if "cloudAutonomousVmClusterId" in data:
        out["cloud_autonomous_vm_cluster_id"] = data["cloudAutonomousVmClusterId"]
    if "unallocatedAdbStorageInTBs" in data:
        out["unallocated_adb_storage_in_t_bs"] = data["unallocatedAdbStorageInTBs"]
    return out
