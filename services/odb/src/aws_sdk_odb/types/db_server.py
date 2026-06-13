"""Generated from Smithy shape ``com.amazonaws.odb#DbServer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_odb.types.compute_model
    import aws_sdk_odb.types.db_server_patching_details
    import aws_sdk_odb.types.resource_id
    import aws_sdk_odb.types.resource_status
    import aws_sdk_odb.types.string_list


class DbServer(TypedDict):
    db_server_id: NotRequired["aws_sdk_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier for the database server.</p>"""
    status: NotRequired["aws_sdk_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the database server.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the database server.</p>"""
    cpu_core_count: NotRequired["int"]
    """<p>The number of CPU cores enabled on the database server.</p>"""
    db_node_storage_size_in_g_bs: NotRequired["int"]
    """<p>The allocated local node storage in GBs on the database server.</p>"""
    db_server_patching_details: NotRequired[
        "aws_sdk_odb.types.db_server_patching_details.DbServerPatchingDetails"
    ]
    """<p>The scheduling details for the quarterly maintenance window. Patching and system updates take place during the maintenance window.</p>"""
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the database server.</p>"""
    exadata_infrastructure_id: NotRequired["str"]
    """<p>The ID of the Exadata infrastructure the database server belongs to.</p>"""
    ocid: NotRequired["str"]
    """<p>The OCID of the database server.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the OCI resource anchor for the database server.</p>"""
    max_cpu_count: NotRequired["int"]
    """<p>The total number of CPU cores available.</p>"""
    max_db_node_storage_in_g_bs: NotRequired["int"]
    """<p>The total local node storage available in GBs.</p>"""
    max_memory_in_g_bs: NotRequired["int"]
    """<p>The total memory available in GBs.</p>"""
    memory_size_in_g_bs: NotRequired["int"]
    """<p>The allocated memory in GBs on the database server.</p>"""
    shape: NotRequired["str"]
    """<p>The shape of the database server. The shape determines the amount of CPU, storage, and memory resources available.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the database server was created.</p>"""
    vm_cluster_ids: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The OCID of the VM clusters that are associated with the database server.</p>"""
    compute_model: NotRequired["aws_sdk_odb.types.compute_model.ComputeModel"]
    """<p>The compute model of the database server (ECPU or OCPU).</p>"""
    autonomous_vm_cluster_ids: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The list of identifiers for the Autonomous VM clusters associated with this database server.</p>"""
    autonomous_virtual_machine_ids: NotRequired[
        "aws_sdk_odb.types.string_list.StringList"
    ]
    """<p>The list of unique identifiers for the Autonomous VMs associated with this database server.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbServer) -> dict:
    out: dict = {}
    if "db_server_id" in value:
        out["dbServerId"] = value["db_server_id"]
    if "status" in value:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "cpu_core_count" in value:
        out["cpuCoreCount"] = value["cpu_core_count"]
    if "db_node_storage_size_in_g_bs" in value:
        out["dbNodeStorageSizeInGBs"] = value["db_node_storage_size_in_g_bs"]
    if "db_server_patching_details" in value:
        import aws_sdk_odb.types.db_server_patching_details

        out["dbServerPatchingDetails"] = (
            aws_sdk_odb.types.db_server_patching_details.serialize_aws_json_1_0(
                value["db_server_patching_details"]
            )
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "exadata_infrastructure_id" in value:
        out["exadataInfrastructureId"] = value["exadata_infrastructure_id"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "oci_resource_anchor_name" in value:
        out["ociResourceAnchorName"] = value["oci_resource_anchor_name"]
    if "max_cpu_count" in value:
        out["maxCpuCount"] = value["max_cpu_count"]
    if "max_db_node_storage_in_g_bs" in value:
        out["maxDbNodeStorageInGBs"] = value["max_db_node_storage_in_g_bs"]
    if "max_memory_in_g_bs" in value:
        out["maxMemoryInGBs"] = value["max_memory_in_g_bs"]
    if "memory_size_in_g_bs" in value:
        out["memorySizeInGBs"] = value["memory_size_in_g_bs"]
    if "shape" in value:
        out["shape"] = value["shape"]
    if "created_at" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["createdAt"] = aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "vm_cluster_ids" in value:
        import aws_sdk_odb.types.string_list

        out["vmClusterIds"] = aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
            value["vm_cluster_ids"]
        )
    if "compute_model" in value:
        import aws_sdk_odb.types.compute_model

        out["computeModel"] = aws_sdk_odb.types.compute_model.serialize_aws_json_1_0(
            value["compute_model"]
        )
    if "autonomous_vm_cluster_ids" in value:
        import aws_sdk_odb.types.string_list

        out["autonomousVmClusterIds"] = (
            aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
                value["autonomous_vm_cluster_ids"]
            )
        )
    if "autonomous_virtual_machine_ids" in value:
        import aws_sdk_odb.types.string_list

        out["autonomousVirtualMachineIds"] = (
            aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
                value["autonomous_virtual_machine_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DbServer:
    out: DbServer = {}  # type: ignore[typeddict-item]
    if "dbServerId" in data:
        out["db_server_id"] = data["dbServerId"]
    if "status" in data:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "cpuCoreCount" in data:
        out["cpu_core_count"] = data["cpuCoreCount"]
    if "dbNodeStorageSizeInGBs" in data:
        out["db_node_storage_size_in_g_bs"] = data["dbNodeStorageSizeInGBs"]
    if "dbServerPatchingDetails" in data:
        import aws_sdk_odb.types.db_server_patching_details

        out["db_server_patching_details"] = (
            aws_sdk_odb.types.db_server_patching_details.deserialize_aws_json_1_0(
                data["dbServerPatchingDetails"]
            )
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "exadataInfrastructureId" in data:
        out["exadata_infrastructure_id"] = data["exadataInfrastructureId"]
    if "ocid" in data:
        out["ocid"] = data["ocid"]
    if "ociResourceAnchorName" in data:
        out["oci_resource_anchor_name"] = data["ociResourceAnchorName"]
    if "maxCpuCount" in data:
        out["max_cpu_count"] = data["maxCpuCount"]
    if "maxDbNodeStorageInGBs" in data:
        out["max_db_node_storage_in_g_bs"] = data["maxDbNodeStorageInGBs"]
    if "maxMemoryInGBs" in data:
        out["max_memory_in_g_bs"] = data["maxMemoryInGBs"]
    if "memorySizeInGBs" in data:
        out["memory_size_in_g_bs"] = data["memorySizeInGBs"]
    if "shape" in data:
        out["shape"] = data["shape"]
    if "createdAt" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "vmClusterIds" in data:
        import aws_sdk_odb.types.string_list

        out["vm_cluster_ids"] = aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
            data["vmClusterIds"]
        )
    if "computeModel" in data:
        import aws_sdk_odb.types.compute_model

        out["compute_model"] = aws_sdk_odb.types.compute_model.deserialize_aws_json_1_0(
            data["computeModel"]
        )
    if "autonomousVmClusterIds" in data:
        import aws_sdk_odb.types.string_list

        out["autonomous_vm_cluster_ids"] = (
            aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
                data["autonomousVmClusterIds"]
            )
        )
    if "autonomousVirtualMachineIds" in data:
        import aws_sdk_odb.types.string_list

        out["autonomous_virtual_machine_ids"] = (
            aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
                data["autonomousVirtualMachineIds"]
            )
        )
    return out
