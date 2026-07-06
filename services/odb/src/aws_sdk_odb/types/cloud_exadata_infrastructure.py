"""Generated from Smithy shape ``com.amazonaws.odb#CloudExadataInfrastructure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_odb.types.compute_model
    import aws_sdk_odb.types.customer_contacts
    import aws_sdk_odb.types.maintenance_window
    import aws_sdk_odb.types.resource_id_or_arn
    import aws_sdk_odb.types.resource_status


class CloudExadataInfrastructure(TypedDict, closed=True):
    cloud_exadata_infrastructure_id: (
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    )
    """<p>The unique identifier for the Exadata infrastructure.</p>"""
    display_name: NotRequired["str"]
    """<p>The user-friendly name for the Exadata infrastructure.</p>"""
    status: NotRequired["aws_sdk_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the Exadata infrastructure.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the Exadata infrastructure.</p>"""
    cloud_exadata_infrastructure_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the Exadata infrastructure.</p>"""
    activated_storage_count: NotRequired["int"]
    """<p>The number of storage servers requested for the Exadata infrastructure.</p>"""
    additional_storage_count: NotRequired["int"]
    """<p>The number of storage servers requested for the Exadata infrastructure.</p>"""
    available_storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of available storage, in gigabytes (GB), for the Exadata infrastructure.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The name of the Availability Zone (AZ) where the Exadata infrastructure is located.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The AZ ID of the AZ where the Exadata infrastructure is located.</p>"""
    compute_count: NotRequired["int"]
    """<p>The number of database servers for the Exadata infrastructure.</p>"""
    cpu_count: NotRequired["int"]
    """<p>The total number of CPU cores that are allocated to the Exadata infrastructure.</p>"""
    customer_contacts_to_send_to_oci: NotRequired[
        "aws_sdk_odb.types.customer_contacts.CustomerContacts"
    ]
    """<p>The email addresses of contacts to receive notification from Oracle about maintenance updates for the Exadata infrastructure.</p>"""
    data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The size of the Exadata infrastructure's data disk group, in terabytes (TB).</p>"""
    db_node_storage_size_in_g_bs: NotRequired["int"]
    """<p>The size of the Exadata infrastructure's local node storage, in gigabytes (GB).</p>"""
    db_server_version: NotRequired["str"]
    """<p>The software version of the database servers (dom0) in the Exadata infrastructure.</p>"""
    last_maintenance_run_id: NotRequired["str"]
    """<p>The Oracle Cloud Identifier (OCID) of the last maintenance run for the Exadata infrastructure.</p>"""
    maintenance_window: NotRequired[
        "aws_sdk_odb.types.maintenance_window.MaintenanceWindow"
    ]
    """<p>The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.</p>"""
    max_cpu_count: NotRequired["int"]
    """<p>The total number of CPU cores available on the Exadata infrastructure.</p>"""
    max_data_storage_in_t_bs: NotRequired["float"]
    """<p>The total amount of data disk group storage, in terabytes (TB), that's available on the Exadata infrastructure.</p>"""
    max_db_node_storage_size_in_g_bs: NotRequired["int"]
    """<p>The total amount of local node storage, in gigabytes (GB), that's available on the Exadata infrastructure.</p>"""
    max_memory_in_g_bs: NotRequired["int"]
    """<p>The total amount of memory, in gigabytes (GB), that's available on the Exadata infrastructure.</p>"""
    memory_size_in_g_bs: NotRequired["int"]
    """<p>The amount of memory, in gigabytes (GB), that's allocated on the Exadata infrastructure.</p>"""
    monthly_db_server_version: NotRequired["str"]
    """<p>The monthly software version of the database servers installed on the Exadata infrastructure.</p>"""
    monthly_storage_server_version: NotRequired["str"]
    """<p>The monthly software version of the storage servers installed on the Exadata infrastructure.</p>"""
    next_maintenance_run_id: NotRequired["str"]
    """<p>The OCID of the next maintenance run for the Exadata infrastructure.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the OCI resource anchor for the Exadata infrastructure.</p>"""
    oci_url: NotRequired["str"]
    """<p>The HTTPS link to the Exadata infrastructure in OCI.</p>"""
    ocid: NotRequired["str"]
    """<p>The OCID of the Exadata infrastructure.</p>"""
    shape: NotRequired["str"]
    """<p>The model name of the Exadata infrastructure.</p>"""
    storage_count: NotRequired["int"]
    """<p>The number of storage servers that are activated for the Exadata infrastructure.</p>"""
    storage_server_version: NotRequired["str"]
    """<p>The software version of the storage servers on the Exadata infrastructure.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the Exadata infrastructure was created.</p>"""
    total_storage_size_in_g_bs: NotRequired["int"]
    """<p>The total amount of storage, in gigabytes (GB), on the the Exadata infrastructure.</p>"""
    percent_progress: NotRequired["float"]
    """<p>The amount of progress made on the current operation on the Exadata infrastructure, expressed as a percentage.</p>"""
    database_server_type: NotRequired["str"]
    """<p>The database server model type of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>"""
    storage_server_type: NotRequired["str"]
    """<p>The storage server model type of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>"""
    compute_model: NotRequired["aws_sdk_odb.types.compute_model.ComputeModel"]
    """<p>The OCI model compute model used when you create or clone an instance: ECPU or OCPU. An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudExadataInfrastructure) -> dict:
    out: dict = {}
    out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "cloud_exadata_infrastructure_arn" in value:
        out["cloudExadataInfrastructureArn"] = value["cloud_exadata_infrastructure_arn"]
    if "activated_storage_count" in value:
        out["activatedStorageCount"] = value["activated_storage_count"]
    if "additional_storage_count" in value:
        out["additionalStorageCount"] = value["additional_storage_count"]
    if "available_storage_size_in_g_bs" in value:
        out["availableStorageSizeInGBs"] = value["available_storage_size_in_g_bs"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "compute_count" in value:
        out["computeCount"] = value["compute_count"]
    if "cpu_count" in value:
        out["cpuCount"] = value["cpu_count"]
    if "customer_contacts_to_send_to_oci" in value:
        import aws_sdk_odb.types.customer_contacts

        out["customerContactsToSendToOCI"] = (
            aws_sdk_odb.types.customer_contacts.serialize_aws_json_1_0(
                value["customer_contacts_to_send_to_oci"]
            )
        )
    if "data_storage_size_in_t_bs" in value:
        out["dataStorageSizeInTBs"] = value["data_storage_size_in_t_bs"]
    if "db_node_storage_size_in_g_bs" in value:
        out["dbNodeStorageSizeInGBs"] = value["db_node_storage_size_in_g_bs"]
    if "db_server_version" in value:
        out["dbServerVersion"] = value["db_server_version"]
    if "last_maintenance_run_id" in value:
        out["lastMaintenanceRunId"] = value["last_maintenance_run_id"]
    if "maintenance_window" in value:
        import aws_sdk_odb.types.maintenance_window

        out["maintenanceWindow"] = (
            aws_sdk_odb.types.maintenance_window.serialize_aws_json_1_0(
                value["maintenance_window"]
            )
        )
    if "max_cpu_count" in value:
        out["maxCpuCount"] = value["max_cpu_count"]
    if "max_data_storage_in_t_bs" in value:
        out["maxDataStorageInTBs"] = value["max_data_storage_in_t_bs"]
    if "max_db_node_storage_size_in_g_bs" in value:
        out["maxDbNodeStorageSizeInGBs"] = value["max_db_node_storage_size_in_g_bs"]
    if "max_memory_in_g_bs" in value:
        out["maxMemoryInGBs"] = value["max_memory_in_g_bs"]
    if "memory_size_in_g_bs" in value:
        out["memorySizeInGBs"] = value["memory_size_in_g_bs"]
    if "monthly_db_server_version" in value:
        out["monthlyDbServerVersion"] = value["monthly_db_server_version"]
    if "monthly_storage_server_version" in value:
        out["monthlyStorageServerVersion"] = value["monthly_storage_server_version"]
    if "next_maintenance_run_id" in value:
        out["nextMaintenanceRunId"] = value["next_maintenance_run_id"]
    if "oci_resource_anchor_name" in value:
        out["ociResourceAnchorName"] = value["oci_resource_anchor_name"]
    if "oci_url" in value:
        out["ociUrl"] = value["oci_url"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "shape" in value:
        out["shape"] = value["shape"]
    if "storage_count" in value:
        out["storageCount"] = value["storage_count"]
    if "storage_server_version" in value:
        out["storageServerVersion"] = value["storage_server_version"]
    if "created_at" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["createdAt"] = aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "total_storage_size_in_g_bs" in value:
        out["totalStorageSizeInGBs"] = value["total_storage_size_in_g_bs"]
    if "percent_progress" in value:
        out["percentProgress"] = value["percent_progress"]
    if "database_server_type" in value:
        out["databaseServerType"] = value["database_server_type"]
    if "storage_server_type" in value:
        out["storageServerType"] = value["storage_server_type"]
    if "compute_model" in value:
        import aws_sdk_odb.types.compute_model

        out["computeModel"] = aws_sdk_odb.types.compute_model.serialize_aws_json_1_0(
            value["compute_model"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CloudExadataInfrastructure:
    out: CloudExadataInfrastructure = {}  # type: ignore[typeddict-item]
    if "cloudExadataInfrastructureId" in data:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    else:
        raise DeserializationError(
            "CloudExadataInfrastructure.cloud_exadata_infrastructure_id required"
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "status" in data:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "cloudExadataInfrastructureArn" in data:
        out["cloud_exadata_infrastructure_arn"] = data["cloudExadataInfrastructureArn"]
    if "activatedStorageCount" in data:
        out["activated_storage_count"] = data["activatedStorageCount"]
    if "additionalStorageCount" in data:
        out["additional_storage_count"] = data["additionalStorageCount"]
    if "availableStorageSizeInGBs" in data:
        out["available_storage_size_in_g_bs"] = data["availableStorageSizeInGBs"]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if "computeCount" in data:
        out["compute_count"] = data["computeCount"]
    if "cpuCount" in data:
        out["cpu_count"] = data["cpuCount"]
    if "customerContactsToSendToOCI" in data:
        import aws_sdk_odb.types.customer_contacts

        out["customer_contacts_to_send_to_oci"] = (
            aws_sdk_odb.types.customer_contacts.deserialize_aws_json_1_0(
                data["customerContactsToSendToOCI"]
            )
        )
    if "dataStorageSizeInTBs" in data:
        out["data_storage_size_in_t_bs"] = data["dataStorageSizeInTBs"]
    if "dbNodeStorageSizeInGBs" in data:
        out["db_node_storage_size_in_g_bs"] = data["dbNodeStorageSizeInGBs"]
    if "dbServerVersion" in data:
        out["db_server_version"] = data["dbServerVersion"]
    if "lastMaintenanceRunId" in data:
        out["last_maintenance_run_id"] = data["lastMaintenanceRunId"]
    if "maintenanceWindow" in data:
        import aws_sdk_odb.types.maintenance_window

        out["maintenance_window"] = (
            aws_sdk_odb.types.maintenance_window.deserialize_aws_json_1_0(
                data["maintenanceWindow"]
            )
        )
    if "maxCpuCount" in data:
        out["max_cpu_count"] = data["maxCpuCount"]
    if "maxDataStorageInTBs" in data:
        out["max_data_storage_in_t_bs"] = data["maxDataStorageInTBs"]
    if "maxDbNodeStorageSizeInGBs" in data:
        out["max_db_node_storage_size_in_g_bs"] = data["maxDbNodeStorageSizeInGBs"]
    if "maxMemoryInGBs" in data:
        out["max_memory_in_g_bs"] = data["maxMemoryInGBs"]
    if "memorySizeInGBs" in data:
        out["memory_size_in_g_bs"] = data["memorySizeInGBs"]
    if "monthlyDbServerVersion" in data:
        out["monthly_db_server_version"] = data["monthlyDbServerVersion"]
    if "monthlyStorageServerVersion" in data:
        out["monthly_storage_server_version"] = data["monthlyStorageServerVersion"]
    if "nextMaintenanceRunId" in data:
        out["next_maintenance_run_id"] = data["nextMaintenanceRunId"]
    if "ociResourceAnchorName" in data:
        out["oci_resource_anchor_name"] = data["ociResourceAnchorName"]
    if "ociUrl" in data:
        out["oci_url"] = data["ociUrl"]
    if "ocid" in data:
        out["ocid"] = data["ocid"]
    if "shape" in data:
        out["shape"] = data["shape"]
    if "storageCount" in data:
        out["storage_count"] = data["storageCount"]
    if "storageServerVersion" in data:
        out["storage_server_version"] = data["storageServerVersion"]
    if "createdAt" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "totalStorageSizeInGBs" in data:
        out["total_storage_size_in_g_bs"] = data["totalStorageSizeInGBs"]
    if "percentProgress" in data:
        out["percent_progress"] = data["percentProgress"]
    if "databaseServerType" in data:
        out["database_server_type"] = data["databaseServerType"]
    if "storageServerType" in data:
        out["storage_server_type"] = data["storageServerType"]
    if "computeModel" in data:
        import aws_sdk_odb.types.compute_model

        out["compute_model"] = aws_sdk_odb.types.compute_model.deserialize_aws_json_1_0(
            data["computeModel"]
        )
    return out
