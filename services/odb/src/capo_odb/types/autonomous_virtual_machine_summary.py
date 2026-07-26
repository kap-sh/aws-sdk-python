"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousVirtualMachineSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id
    import capo_odb.types.resource_status


class AutonomousVirtualMachineSummary(TypedDict, closed=True):
    autonomous_virtual_machine_id: NotRequired["capo_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the Autonomous VM.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the Autonomous VM.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the Autonomous VM, if applicable.</p>"""
    vm_name: NotRequired["str"]
    """<p>The name of the Autonomous VM.</p>"""
    db_server_id: NotRequired["capo_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the database server hosting this Autonomous VM.</p>"""
    db_server_display_name: NotRequired["str"]
    """<p>The display name of the database server hosting this Autonomous VM.</p>"""
    cpu_core_count: NotRequired["int"]
    """<p>The number of CPU cores allocated to this Autonomous VM.</p>"""
    memory_size_in_g_bs: NotRequired["int"]
    """<p>The amount of memory allocated to this Autonomous VM, in gigabytes (GB).</p>"""
    db_node_storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of storage allocated to this Autonomous Virtual Machine, in gigabytes (GB).</p>"""
    client_ip_address: NotRequired["str"]
    """<p>The IP address used by clients to connect to this Autonomous VM.</p>"""
    cloud_autonomous_vm_cluster_id: NotRequired["str"]
    """<p>The unique identifier of the Autonomous VM cluster containing this Autonomous VM.</p>"""
    ocid: NotRequired["str"]
    """<p>The Oracle Cloud Identifier (OCID) of the Autonomous VM.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the Oracle Cloud Infrastructure (OCI) resource anchor associated with this Autonomous VM.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousVirtualMachineSummary) -> dict:
    out: dict = {}
    if "autonomous_virtual_machine_id" in value:
        out["autonomousVirtualMachineId"] = value["autonomous_virtual_machine_id"]
    if "status" in value:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "vm_name" in value:
        out["vmName"] = value["vm_name"]
    if "db_server_id" in value:
        out["dbServerId"] = value["db_server_id"]
    if "db_server_display_name" in value:
        out["dbServerDisplayName"] = value["db_server_display_name"]
    if "cpu_core_count" in value:
        out["cpuCoreCount"] = value["cpu_core_count"]
    if "memory_size_in_g_bs" in value:
        out["memorySizeInGBs"] = value["memory_size_in_g_bs"]
    if "db_node_storage_size_in_g_bs" in value:
        out["dbNodeStorageSizeInGBs"] = value["db_node_storage_size_in_g_bs"]
    if "client_ip_address" in value:
        out["clientIpAddress"] = value["client_ip_address"]
    if "cloud_autonomous_vm_cluster_id" in value:
        out["cloudAutonomousVmClusterId"] = value["cloud_autonomous_vm_cluster_id"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "oci_resource_anchor_name" in value:
        out["ociResourceAnchorName"] = value["oci_resource_anchor_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AutonomousVirtualMachineSummary:
    out: AutonomousVirtualMachineSummary = {}  # type: ignore[typeddict-item]
    if "autonomousVirtualMachineId" in data:
        out["autonomous_virtual_machine_id"] = data["autonomousVirtualMachineId"]
    if "status" in data:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "vmName" in data:
        out["vm_name"] = data["vmName"]
    if "dbServerId" in data:
        out["db_server_id"] = data["dbServerId"]
    if "dbServerDisplayName" in data:
        out["db_server_display_name"] = data["dbServerDisplayName"]
    if "cpuCoreCount" in data:
        out["cpu_core_count"] = data["cpuCoreCount"]
    if "memorySizeInGBs" in data:
        out["memory_size_in_g_bs"] = data["memorySizeInGBs"]
    if "dbNodeStorageSizeInGBs" in data:
        out["db_node_storage_size_in_g_bs"] = data["dbNodeStorageSizeInGBs"]
    if "clientIpAddress" in data:
        out["client_ip_address"] = data["clientIpAddress"]
    if "cloudAutonomousVmClusterId" in data:
        out["cloud_autonomous_vm_cluster_id"] = data["cloudAutonomousVmClusterId"]
    if "ocid" in data:
        out["ocid"] = data["ocid"]
    if "ociResourceAnchorName" in data:
        out["oci_resource_anchor_name"] = data["ociResourceAnchorName"]
    return out
