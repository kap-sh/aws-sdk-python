"""Generated from Smithy shape ``com.amazonaws.odb#DbNodeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_odb.types.db_node_maintenance_type
    import aws_sdk_odb.types.db_node_resource_status
    import aws_sdk_odb.types.resource_arn
    import aws_sdk_odb.types.resource_id


class DbNodeSummary(TypedDict):
    db_node_id: NotRequired["aws_sdk_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the DB node.</p>"""
    db_node_arn: NotRequired["aws_sdk_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the DB node.</p>"""
    status: NotRequired[
        "aws_sdk_odb.types.db_node_resource_status.DbNodeResourceStatus"
    ]
    """<p>The current status of the DB node.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the DB node.</p>"""
    additional_details: NotRequired["str"]
    """<p>Additional information about the planned maintenance.</p>"""
    backup_ip_id: NotRequired["str"]
    """<p>The Oracle Cloud ID (OCID) of the backup IP address that's associated with the DB node.</p>"""
    backup_vnic2_id: NotRequired["str"]
    """<p>The OCID of the second backup virtual network interface card (VNIC) for the DB node.</p>"""
    backup_vnic_id: NotRequired["str"]
    """<p>The OCID of the backup VNIC for the DB node.</p>"""
    cpu_core_count: NotRequired["int"]
    """<p>The number of CPU cores enabled on the DB node.</p>"""
    db_node_storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of local node storage, in gigabytes (GB), that's allocated on the DB node.</p>"""
    db_server_id: NotRequired["aws_sdk_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the database server that's associated with the DB node.</p>"""
    db_system_id: NotRequired["str"]
    """<p>The OCID of the DB system.</p>"""
    fault_domain: NotRequired["str"]
    """<p>The name of the fault domain where the DB node is located.</p>"""
    host_ip_id: NotRequired["str"]
    """<p>The OCID of the host IP address that's associated with the DB node.</p>"""
    hostname: NotRequired["str"]
    """<p>The host name for the DB node.</p>"""
    ocid: NotRequired["str"]
    """<p>The OCID of the DB node.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the OCI resource anchor for the DB node.</p>"""
    maintenance_type: NotRequired[
        "aws_sdk_odb.types.db_node_maintenance_type.DbNodeMaintenanceType"
    ]
    """<p>The type of maintenance the DB node. </p>"""
    memory_size_in_g_bs: NotRequired["int"]
    """<p>The amount of memory, in gigabytes (GB), that allocated on the DB node.</p>"""
    software_storage_size_in_gb: NotRequired["int"]
    """<p>The size of the block storage volume, in gigabytes (GB), that's allocated for the DB system. This attribute applies only for virtual machine DB systems.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the DB node was created.</p>"""
    time_maintenance_window_end: NotRequired["str"]
    """<p>The end date and time of the maintenance window.</p>"""
    time_maintenance_window_start: NotRequired["str"]
    """<p>The start date and time of the maintenance window.</p>"""
    total_cpu_core_count: NotRequired["int"]
    """<p>The total number of CPU cores reserved on the DB node.</p>"""
    vnic2_id: NotRequired["str"]
    """<p>The OCID of the second VNIC.</p>"""
    vnic_id: NotRequired["str"]
    """<p>The OCID of the VNIC.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbNodeSummary) -> dict:
    out: dict = {}
    if "db_node_id" in value:
        out["dbNodeId"] = value["db_node_id"]
    if "db_node_arn" in value:
        out["dbNodeArn"] = value["db_node_arn"]
    if "status" in value:
        import aws_sdk_odb.types.db_node_resource_status

        out["status"] = (
            aws_sdk_odb.types.db_node_resource_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "additional_details" in value:
        out["additionalDetails"] = value["additional_details"]
    if "backup_ip_id" in value:
        out["backupIpId"] = value["backup_ip_id"]
    if "backup_vnic2_id" in value:
        out["backupVnic2Id"] = value["backup_vnic2_id"]
    if "backup_vnic_id" in value:
        out["backupVnicId"] = value["backup_vnic_id"]
    if "cpu_core_count" in value:
        out["cpuCoreCount"] = value["cpu_core_count"]
    if "db_node_storage_size_in_g_bs" in value:
        out["dbNodeStorageSizeInGBs"] = value["db_node_storage_size_in_g_bs"]
    if "db_server_id" in value:
        out["dbServerId"] = value["db_server_id"]
    if "db_system_id" in value:
        out["dbSystemId"] = value["db_system_id"]
    if "fault_domain" in value:
        out["faultDomain"] = value["fault_domain"]
    if "host_ip_id" in value:
        out["hostIpId"] = value["host_ip_id"]
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "oci_resource_anchor_name" in value:
        out["ociResourceAnchorName"] = value["oci_resource_anchor_name"]
    if "maintenance_type" in value:
        import aws_sdk_odb.types.db_node_maintenance_type

        out["maintenanceType"] = (
            aws_sdk_odb.types.db_node_maintenance_type.serialize_aws_json_1_0(
                value["maintenance_type"]
            )
        )
    if "memory_size_in_g_bs" in value:
        out["memorySizeInGBs"] = value["memory_size_in_g_bs"]
    if "software_storage_size_in_gb" in value:
        out["softwareStorageSizeInGB"] = value["software_storage_size_in_gb"]
    if "created_at" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["createdAt"] = aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "time_maintenance_window_end" in value:
        out["timeMaintenanceWindowEnd"] = value["time_maintenance_window_end"]
    if "time_maintenance_window_start" in value:
        out["timeMaintenanceWindowStart"] = value["time_maintenance_window_start"]
    if "total_cpu_core_count" in value:
        out["totalCpuCoreCount"] = value["total_cpu_core_count"]
    if "vnic2_id" in value:
        out["vnic2Id"] = value["vnic2_id"]
    if "vnic_id" in value:
        out["vnicId"] = value["vnic_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DbNodeSummary:
    out: DbNodeSummary = {}  # type: ignore[typeddict-item]
    if "dbNodeId" in data:
        out["db_node_id"] = data["dbNodeId"]
    if "dbNodeArn" in data:
        out["db_node_arn"] = data["dbNodeArn"]
    if "status" in data:
        import aws_sdk_odb.types.db_node_resource_status

        out["status"] = (
            aws_sdk_odb.types.db_node_resource_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "additionalDetails" in data:
        out["additional_details"] = data["additionalDetails"]
    if "backupIpId" in data:
        out["backup_ip_id"] = data["backupIpId"]
    if "backupVnic2Id" in data:
        out["backup_vnic2_id"] = data["backupVnic2Id"]
    if "backupVnicId" in data:
        out["backup_vnic_id"] = data["backupVnicId"]
    if "cpuCoreCount" in data:
        out["cpu_core_count"] = data["cpuCoreCount"]
    if "dbNodeStorageSizeInGBs" in data:
        out["db_node_storage_size_in_g_bs"] = data["dbNodeStorageSizeInGBs"]
    if "dbServerId" in data:
        out["db_server_id"] = data["dbServerId"]
    if "dbSystemId" in data:
        out["db_system_id"] = data["dbSystemId"]
    if "faultDomain" in data:
        out["fault_domain"] = data["faultDomain"]
    if "hostIpId" in data:
        out["host_ip_id"] = data["hostIpId"]
    if "hostname" in data:
        out["hostname"] = data["hostname"]
    if "ocid" in data:
        out["ocid"] = data["ocid"]
    if "ociResourceAnchorName" in data:
        out["oci_resource_anchor_name"] = data["ociResourceAnchorName"]
    if "maintenanceType" in data:
        import aws_sdk_odb.types.db_node_maintenance_type

        out["maintenance_type"] = (
            aws_sdk_odb.types.db_node_maintenance_type.deserialize_aws_json_1_0(
                data["maintenanceType"]
            )
        )
    if "memorySizeInGBs" in data:
        out["memory_size_in_g_bs"] = data["memorySizeInGBs"]
    if "softwareStorageSizeInGB" in data:
        out["software_storage_size_in_gb"] = data["softwareStorageSizeInGB"]
    if "createdAt" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "timeMaintenanceWindowEnd" in data:
        out["time_maintenance_window_end"] = data["timeMaintenanceWindowEnd"]
    if "timeMaintenanceWindowStart" in data:
        out["time_maintenance_window_start"] = data["timeMaintenanceWindowStart"]
    if "totalCpuCoreCount" in data:
        out["total_cpu_core_count"] = data["totalCpuCoreCount"]
    if "vnic2Id" in data:
        out["vnic2_id"] = data["vnic2Id"]
    if "vnicId" in data:
        out["vnic_id"] = data["vnicId"]
    return out
