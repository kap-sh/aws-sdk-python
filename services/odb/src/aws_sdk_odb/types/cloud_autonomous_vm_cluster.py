"""Generated from Smithy shape ``com.amazonaws.odb#CloudAutonomousVmCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_odb.types.compute_model
    import aws_sdk_odb.types.iam_role_list
    import aws_sdk_odb.types.license_model
    import aws_sdk_odb.types.maintenance_window
    import aws_sdk_odb.types.resource_arn
    import aws_sdk_odb.types.resource_display_name
    import aws_sdk_odb.types.resource_id
    import aws_sdk_odb.types.resource_id_or_arn
    import aws_sdk_odb.types.resource_status
    import aws_sdk_odb.types.string_list


class CloudAutonomousVmCluster(TypedDict, closed=True):
    cloud_autonomous_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the Autonomous VM cluster.</p>"""
    cloud_autonomous_vm_cluster_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the Autonomous VM cluster.</p>"""
    odb_network_id: NotRequired["aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"]
    """<p>The unique identifier of the ODB network associated with this Autonomous VM cluster.</p>"""
    odb_network_arn: NotRequired["aws_sdk_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the ODB network associated with this Autonomous VM cluster.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the OCI resource anchor associated with this Autonomous VM cluster.</p>"""
    percent_progress: NotRequired["float"]
    """<p>The progress of the current operation on the Autonomous VM cluster, as a percentage.</p>"""
    display_name: NotRequired[
        "aws_sdk_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>The display name of the Autonomous VM cluster.</p>"""
    status: NotRequired["aws_sdk_odb.types.resource_status.ResourceStatus"]
    """<p>The current state of the Autonomous VM cluster. Possible values include <code>CREATING</code>, <code>AVAILABLE</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>DELETED</code>, <code>FAILED</code>.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the Autonomous VM cluster.</p>"""
    cloud_exadata_infrastructure_id: NotRequired[
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    ]
    """<p>The unique identifier of the Cloud Exadata Infrastructure containing this Autonomous VM cluster.</p>"""
    cloud_exadata_infrastructure_arn: NotRequired[
        "aws_sdk_odb.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Cloud Exadata Infrastructure containing this Autonomous VM cluster.</p>"""
    autonomous_data_storage_percentage: NotRequired["float"]
    """<p>The percentage of data storage currently in use for Autonomous Databases in the Autonomous VM cluster.</p>"""
    autonomous_data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The data storage size allocated for Autonomous Databases in the Autonomous VM cluster, in TB.</p>"""
    available_autonomous_data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The available data storage space for Autonomous Databases in the Autonomous VM cluster, in TB.</p>"""
    available_container_databases: NotRequired["int"]
    """<p>The number of Autonomous CDBs that you can create with the currently available storage.</p>"""
    available_cpus: NotRequired["float"]
    """<p>The number of CPU cores available for allocation to Autonomous Databases.</p>"""
    compute_model: NotRequired["aws_sdk_odb.types.compute_model.ComputeModel"]
    """<p>The compute model of the Autonomous VM cluster: ECPU or OCPU.</p>"""
    cpu_core_count: NotRequired["int"]
    """<p>The total number of CPU cores in the Autonomous VM cluster.</p>"""
    cpu_core_count_per_node: NotRequired["int"]
    """<p>The number of CPU cores enabled per node in the Autonomous VM cluster.</p>"""
    cpu_percentage: NotRequired["float"]
    """<p>The percentage of total CPU cores currently in use in the Autonomous VM cluster.</p>"""
    data_storage_size_in_g_bs: NotRequired["float"]
    """<p>The total data storage allocated to the Autonomous VM cluster, in GB.</p>"""
    data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The total data storage allocated to the Autonomous VM cluster, in TB.</p>"""
    db_node_storage_size_in_g_bs: NotRequired["int"]
    """<p>The local node storage allocated to the Autonomous VM cluster, in gigabytes (GB).</p>"""
    db_servers: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The list of database servers associated with the Autonomous VM cluster.</p>"""
    description: NotRequired["str"]
    """<p>The user-provided description of the Autonomous VM cluster.</p>"""
    domain: NotRequired["str"]
    """<p>The domain name for the Autonomous VM cluster.</p>"""
    exadata_storage_in_t_bs_lowest_scaled_value: NotRequired["float"]
    """<p>The minimum value to which you can scale down the Exadata storage, in TB.</p>"""
    hostname: NotRequired["str"]
    """<p>The hostname for the Autonomous VM cluster.</p>"""
    ocid: NotRequired["str"]
    """<p>The Oracle Cloud Identifier (OCID) of the Autonomous VM cluster.</p>"""
    oci_url: NotRequired["str"]
    """<p>The URL for accessing the OCI console page for this Autonomous VM cluster.</p>"""
    is_mtls_enabled_vm_cluster: NotRequired["bool"]
    """<p>Indicates whether mutual TLS (mTLS) authentication is enabled for the Autonomous VM cluster.</p>"""
    license_model: NotRequired["aws_sdk_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model that applies to the Autonomous VM cluster.</p>"""
    maintenance_window: NotRequired[
        "aws_sdk_odb.types.maintenance_window.MaintenanceWindow"
    ]
    """<p>The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.</p>"""
    max_acds_lowest_scaled_value: NotRequired["int"]
    """<p>The minimum value to which you can scale down the maximum number of Autonomous CDBs.</p>"""
    memory_per_oracle_compute_unit_in_g_bs: NotRequired["int"]
    """<p>The amount of memory allocated per Oracle Compute Unit, in GB.</p>"""
    memory_size_in_g_bs: NotRequired["int"]
    """<p>The total amount of memory allocated to the Autonomous VM cluster, in gigabytes (GB).</p>"""
    node_count: NotRequired["int"]
    """<p>The number of database server nodes in the Autonomous VM cluster.</p>"""
    non_provisionable_autonomous_container_databases: NotRequired["int"]
    """<p>The number of Autonomous CDBs that can't be provisioned because of resource constraints.</p>"""
    provisionable_autonomous_container_databases: NotRequired["int"]
    """<p>The number of Autonomous CDBs that can be provisioned in the Autonomous VM cluster.</p>"""
    provisioned_autonomous_container_databases: NotRequired["int"]
    """<p>The number of Autonomous CDBs currently provisioned in the Autonomous VM cluster.</p>"""
    provisioned_cpus: NotRequired["float"]
    """<p>The number of CPU cores currently provisioned in the Autonomous VM cluster.</p>"""
    reclaimable_cpus: NotRequired["float"]
    """<p>The number of CPU cores that can be reclaimed from terminated or scaled-down Autonomous Databases.</p>"""
    reserved_cpus: NotRequired["float"]
    """<p>The number of CPU cores reserved for system operations and redundancy.</p>"""
    scan_listener_port_non_tls: NotRequired["int"]
    """<p>The SCAN listener port for non-TLS (TCP) protocol. The default is 1521.</p>"""
    scan_listener_port_tls: NotRequired["int"]
    """<p>The SCAN listener port for TLS (TCP) protocol. The default is 2484.</p>"""
    shape: NotRequired["str"]
    """<p>The shape of the Exadata infrastructure for the Autonomous VM cluster.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the Autonomous VM cluster was created.</p>"""
    time_database_ssl_certificate_expires: NotRequired["datetime.datetime"]
    """<p>The expiration date and time of the database SSL certificate.</p>"""
    time_ords_certificate_expires: NotRequired["datetime.datetime"]
    """<p>The expiration date and time of the Oracle REST Data Services (ORDS) certificate.</p>"""
    time_zone: NotRequired["str"]
    """<p>The time zone of the Autonomous VM cluster.</p>"""
    total_container_databases: NotRequired["int"]
    """<p>The total number of Autonomous Container Databases that can be created with the allocated local storage.</p>"""
    iam_roles: NotRequired["aws_sdk_odb.types.iam_role_list.IamRoleList"]
    """<p>The Amazon Web Services Identity and Access Management (IAM) service roles associated with the Autonomous VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudAutonomousVmCluster) -> dict:
    out: dict = {}
    out["cloudAutonomousVmClusterId"] = value["cloud_autonomous_vm_cluster_id"]
    if "cloud_autonomous_vm_cluster_arn" in value:
        out["cloudAutonomousVmClusterArn"] = value["cloud_autonomous_vm_cluster_arn"]
    if "odb_network_id" in value:
        out["odbNetworkId"] = value["odb_network_id"]
    if "odb_network_arn" in value:
        out["odbNetworkArn"] = value["odb_network_arn"]
    if "oci_resource_anchor_name" in value:
        out["ociResourceAnchorName"] = value["oci_resource_anchor_name"]
    if "percent_progress" in value:
        out["percentProgress"] = value["percent_progress"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "cloud_exadata_infrastructure_id" in value:
        out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    if "cloud_exadata_infrastructure_arn" in value:
        out["cloudExadataInfrastructureArn"] = value["cloud_exadata_infrastructure_arn"]
    if "autonomous_data_storage_percentage" in value:
        out["autonomousDataStoragePercentage"] = value[
            "autonomous_data_storage_percentage"
        ]
    if "autonomous_data_storage_size_in_t_bs" in value:
        out["autonomousDataStorageSizeInTBs"] = value[
            "autonomous_data_storage_size_in_t_bs"
        ]
    if "available_autonomous_data_storage_size_in_t_bs" in value:
        out["availableAutonomousDataStorageSizeInTBs"] = value[
            "available_autonomous_data_storage_size_in_t_bs"
        ]
    if "available_container_databases" in value:
        out["availableContainerDatabases"] = value["available_container_databases"]
    if "available_cpus" in value:
        out["availableCpus"] = value["available_cpus"]
    if "compute_model" in value:
        import aws_sdk_odb.types.compute_model

        out["computeModel"] = aws_sdk_odb.types.compute_model.serialize_aws_json_1_0(
            value["compute_model"]
        )
    if "cpu_core_count" in value:
        out["cpuCoreCount"] = value["cpu_core_count"]
    if "cpu_core_count_per_node" in value:
        out["cpuCoreCountPerNode"] = value["cpu_core_count_per_node"]
    if "cpu_percentage" in value:
        out["cpuPercentage"] = value["cpu_percentage"]
    if "data_storage_size_in_g_bs" in value:
        out["dataStorageSizeInGBs"] = value["data_storage_size_in_g_bs"]
    if "data_storage_size_in_t_bs" in value:
        out["dataStorageSizeInTBs"] = value["data_storage_size_in_t_bs"]
    if "db_node_storage_size_in_g_bs" in value:
        out["dbNodeStorageSizeInGBs"] = value["db_node_storage_size_in_g_bs"]
    if "db_servers" in value:
        import aws_sdk_odb.types.string_list

        out["dbServers"] = aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
            value["db_servers"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "domain" in value:
        out["domain"] = value["domain"]
    if "exadata_storage_in_t_bs_lowest_scaled_value" in value:
        out["exadataStorageInTBsLowestScaledValue"] = value[
            "exadata_storage_in_t_bs_lowest_scaled_value"
        ]
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "oci_url" in value:
        out["ociUrl"] = value["oci_url"]
    if "is_mtls_enabled_vm_cluster" in value:
        out["isMtlsEnabledVmCluster"] = value["is_mtls_enabled_vm_cluster"]
    if "license_model" in value:
        import aws_sdk_odb.types.license_model

        out["licenseModel"] = aws_sdk_odb.types.license_model.serialize_aws_json_1_0(
            value["license_model"]
        )
    if "maintenance_window" in value:
        import aws_sdk_odb.types.maintenance_window

        out["maintenanceWindow"] = (
            aws_sdk_odb.types.maintenance_window.serialize_aws_json_1_0(
                value["maintenance_window"]
            )
        )
    if "max_acds_lowest_scaled_value" in value:
        out["maxAcdsLowestScaledValue"] = value["max_acds_lowest_scaled_value"]
    if "memory_per_oracle_compute_unit_in_g_bs" in value:
        out["memoryPerOracleComputeUnitInGBs"] = value[
            "memory_per_oracle_compute_unit_in_g_bs"
        ]
    if "memory_size_in_g_bs" in value:
        out["memorySizeInGBs"] = value["memory_size_in_g_bs"]
    if "node_count" in value:
        out["nodeCount"] = value["node_count"]
    if "non_provisionable_autonomous_container_databases" in value:
        out["nonProvisionableAutonomousContainerDatabases"] = value[
            "non_provisionable_autonomous_container_databases"
        ]
    if "provisionable_autonomous_container_databases" in value:
        out["provisionableAutonomousContainerDatabases"] = value[
            "provisionable_autonomous_container_databases"
        ]
    if "provisioned_autonomous_container_databases" in value:
        out["provisionedAutonomousContainerDatabases"] = value[
            "provisioned_autonomous_container_databases"
        ]
    if "provisioned_cpus" in value:
        out["provisionedCpus"] = value["provisioned_cpus"]
    if "reclaimable_cpus" in value:
        out["reclaimableCpus"] = value["reclaimable_cpus"]
    if "reserved_cpus" in value:
        out["reservedCpus"] = value["reserved_cpus"]
    if "scan_listener_port_non_tls" in value:
        out["scanListenerPortNonTls"] = value["scan_listener_port_non_tls"]
    if "scan_listener_port_tls" in value:
        out["scanListenerPortTls"] = value["scan_listener_port_tls"]
    if "shape" in value:
        out["shape"] = value["shape"]
    if "created_at" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["createdAt"] = aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "time_database_ssl_certificate_expires" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeDatabaseSslCertificateExpires"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_database_ssl_certificate_expires"]
            )
        )
    if "time_ords_certificate_expires" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeOrdsCertificateExpires"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_ords_certificate_expires"]
            )
        )
    if "time_zone" in value:
        out["timeZone"] = value["time_zone"]
    if "total_container_databases" in value:
        out["totalContainerDatabases"] = value["total_container_databases"]
    if "iam_roles" in value:
        import aws_sdk_odb.types.iam_role_list

        out["iamRoles"] = aws_sdk_odb.types.iam_role_list.serialize_aws_json_1_0(
            value["iam_roles"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CloudAutonomousVmCluster:
    out: CloudAutonomousVmCluster = {}  # type: ignore[typeddict-item]
    if "cloudAutonomousVmClusterId" in data:
        out["cloud_autonomous_vm_cluster_id"] = data["cloudAutonomousVmClusterId"]
    else:
        raise DeserializationError(
            "CloudAutonomousVmCluster.cloud_autonomous_vm_cluster_id required"
        )
    if "cloudAutonomousVmClusterArn" in data:
        out["cloud_autonomous_vm_cluster_arn"] = data["cloudAutonomousVmClusterArn"]
    if "odbNetworkId" in data:
        out["odb_network_id"] = data["odbNetworkId"]
    if "odbNetworkArn" in data:
        out["odb_network_arn"] = data["odbNetworkArn"]
    if "ociResourceAnchorName" in data:
        out["oci_resource_anchor_name"] = data["ociResourceAnchorName"]
    if "percentProgress" in data:
        out["percent_progress"] = data["percentProgress"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "status" in data:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "cloudExadataInfrastructureId" in data:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    if "cloudExadataInfrastructureArn" in data:
        out["cloud_exadata_infrastructure_arn"] = data["cloudExadataInfrastructureArn"]
    if "autonomousDataStoragePercentage" in data:
        out["autonomous_data_storage_percentage"] = data[
            "autonomousDataStoragePercentage"
        ]
    if "autonomousDataStorageSizeInTBs" in data:
        out["autonomous_data_storage_size_in_t_bs"] = data[
            "autonomousDataStorageSizeInTBs"
        ]
    if "availableAutonomousDataStorageSizeInTBs" in data:
        out["available_autonomous_data_storage_size_in_t_bs"] = data[
            "availableAutonomousDataStorageSizeInTBs"
        ]
    if "availableContainerDatabases" in data:
        out["available_container_databases"] = data["availableContainerDatabases"]
    if "availableCpus" in data:
        out["available_cpus"] = data["availableCpus"]
    if "computeModel" in data:
        import aws_sdk_odb.types.compute_model

        out["compute_model"] = aws_sdk_odb.types.compute_model.deserialize_aws_json_1_0(
            data["computeModel"]
        )
    if "cpuCoreCount" in data:
        out["cpu_core_count"] = data["cpuCoreCount"]
    if "cpuCoreCountPerNode" in data:
        out["cpu_core_count_per_node"] = data["cpuCoreCountPerNode"]
    if "cpuPercentage" in data:
        out["cpu_percentage"] = data["cpuPercentage"]
    if "dataStorageSizeInGBs" in data:
        out["data_storage_size_in_g_bs"] = data["dataStorageSizeInGBs"]
    if "dataStorageSizeInTBs" in data:
        out["data_storage_size_in_t_bs"] = data["dataStorageSizeInTBs"]
    if "dbNodeStorageSizeInGBs" in data:
        out["db_node_storage_size_in_g_bs"] = data["dbNodeStorageSizeInGBs"]
    if "dbServers" in data:
        import aws_sdk_odb.types.string_list

        out["db_servers"] = aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
            data["dbServers"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "domain" in data:
        out["domain"] = data["domain"]
    if "exadataStorageInTBsLowestScaledValue" in data:
        out["exadata_storage_in_t_bs_lowest_scaled_value"] = data[
            "exadataStorageInTBsLowestScaledValue"
        ]
    if "hostname" in data:
        out["hostname"] = data["hostname"]
    if "ocid" in data:
        out["ocid"] = data["ocid"]
    if "ociUrl" in data:
        out["oci_url"] = data["ociUrl"]
    if "isMtlsEnabledVmCluster" in data:
        out["is_mtls_enabled_vm_cluster"] = data["isMtlsEnabledVmCluster"]
    if "licenseModel" in data:
        import aws_sdk_odb.types.license_model

        out["license_model"] = aws_sdk_odb.types.license_model.deserialize_aws_json_1_0(
            data["licenseModel"]
        )
    if "maintenanceWindow" in data:
        import aws_sdk_odb.types.maintenance_window

        out["maintenance_window"] = (
            aws_sdk_odb.types.maintenance_window.deserialize_aws_json_1_0(
                data["maintenanceWindow"]
            )
        )
    if "maxAcdsLowestScaledValue" in data:
        out["max_acds_lowest_scaled_value"] = data["maxAcdsLowestScaledValue"]
    if "memoryPerOracleComputeUnitInGBs" in data:
        out["memory_per_oracle_compute_unit_in_g_bs"] = data[
            "memoryPerOracleComputeUnitInGBs"
        ]
    if "memorySizeInGBs" in data:
        out["memory_size_in_g_bs"] = data["memorySizeInGBs"]
    if "nodeCount" in data:
        out["node_count"] = data["nodeCount"]
    if "nonProvisionableAutonomousContainerDatabases" in data:
        out["non_provisionable_autonomous_container_databases"] = data[
            "nonProvisionableAutonomousContainerDatabases"
        ]
    if "provisionableAutonomousContainerDatabases" in data:
        out["provisionable_autonomous_container_databases"] = data[
            "provisionableAutonomousContainerDatabases"
        ]
    if "provisionedAutonomousContainerDatabases" in data:
        out["provisioned_autonomous_container_databases"] = data[
            "provisionedAutonomousContainerDatabases"
        ]
    if "provisionedCpus" in data:
        out["provisioned_cpus"] = data["provisionedCpus"]
    if "reclaimableCpus" in data:
        out["reclaimable_cpus"] = data["reclaimableCpus"]
    if "reservedCpus" in data:
        out["reserved_cpus"] = data["reservedCpus"]
    if "scanListenerPortNonTls" in data:
        out["scan_listener_port_non_tls"] = data["scanListenerPortNonTls"]
    if "scanListenerPortTls" in data:
        out["scan_listener_port_tls"] = data["scanListenerPortTls"]
    if "shape" in data:
        out["shape"] = data["shape"]
    if "createdAt" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "timeDatabaseSslCertificateExpires" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_database_ssl_certificate_expires"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeDatabaseSslCertificateExpires"]
            )
        )
    if "timeOrdsCertificateExpires" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_ords_certificate_expires"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeOrdsCertificateExpires"]
            )
        )
    if "timeZone" in data:
        out["time_zone"] = data["timeZone"]
    if "totalContainerDatabases" in data:
        out["total_container_databases"] = data["totalContainerDatabases"]
    if "iamRoles" in data:
        import aws_sdk_odb.types.iam_role_list

        out["iam_roles"] = aws_sdk_odb.types.iam_role_list.deserialize_aws_json_1_0(
            data["iamRoles"]
        )
    return out
