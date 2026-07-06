"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_odb.types.autonomous_database_apex
    import aws_sdk_odb.types.autonomous_database_connection_strings
    import aws_sdk_odb.types.autonomous_database_connection_urls
    import aws_sdk_odb.types.autonomous_database_resource_status
    import aws_sdk_odb.types.autonomous_maintenance_schedule_type
    import aws_sdk_odb.types.compute_model
    import aws_sdk_odb.types.customer_contacts
    import aws_sdk_odb.types.data_guard_role
    import aws_sdk_odb.types.data_safe_status
    import aws_sdk_odb.types.database_edition
    import aws_sdk_odb.types.database_management_status
    import aws_sdk_odb.types.database_standby_summary
    import aws_sdk_odb.types.database_tool_list
    import aws_sdk_odb.types.database_type
    import aws_sdk_odb.types.db_workload
    import aws_sdk_odb.types.disaster_recovery_configuration
    import aws_sdk_odb.types.disaster_recovery_type
    import aws_sdk_odb.types.encryption_summary
    import aws_sdk_odb.types.integer_list
    import aws_sdk_odb.types.license_model
    import aws_sdk_odb.types.long_term_backup_schedule
    import aws_sdk_odb.types.net_services_architecture
    import aws_sdk_odb.types.open_mode
    import aws_sdk_odb.types.operations_insights_status
    import aws_sdk_odb.types.permission_level
    import aws_sdk_odb.types.refreshable_mode
    import aws_sdk_odb.types.refreshable_status
    import aws_sdk_odb.types.resource_arn
    import aws_sdk_odb.types.resource_id
    import aws_sdk_odb.types.resource_id_or_arn
    import aws_sdk_odb.types.resource_pool_summary
    import aws_sdk_odb.types.scheduled_operation_details_list
    import aws_sdk_odb.types.standby_allowlisted_ips_source
    import aws_sdk_odb.types.string_list


class AutonomousDatabaseSummary(TypedDict, closed=True):
    autonomous_database_id: NotRequired[
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    ]
    """<p>The unique identifier of the Autonomous Database.</p>"""
    autonomous_database_arn: NotRequired["aws_sdk_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the Autonomous Database.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the Oracle Cloud Infrastructure (OCI) resource anchor associated with the Autonomous Database.</p>"""
    percent_progress: NotRequired["float"]
    """<p>The progress of the current operation on the Autonomous Database, as a percentage.</p>"""
    ocid: NotRequired["str"]
    """<p>The Oracle Cloud Identifier (OCID) of the Autonomous Database.</p>"""
    oci_url: NotRequired["str"]
    """<p>The URL for accessing the OCI console page for the Autonomous Database.</p>"""
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the Autonomous Database.</p>"""
    db_name: NotRequired["str"]
    """<p>The name of the Autonomous Database.</p>"""
    source_id: NotRequired["str"]
    """<p>The unique identifier of the source from which the Autonomous Database was created.</p>"""
    status: NotRequired[
        "aws_sdk_odb.types.autonomous_database_resource_status.AutonomousDatabaseResourceStatus"
    ]
    """<p>The current status of the Autonomous Database.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the Autonomous Database, if applicable.</p>"""
    database_type: NotRequired["aws_sdk_odb.types.database_type.DatabaseType"]
    """<p>The type of the Autonomous Database, either a regular database or a clone.</p>"""
    db_version: NotRequired["str"]
    """<p>The Oracle Database software version of the Autonomous Database.</p>"""
    db_workload: NotRequired["aws_sdk_odb.types.db_workload.DbWorkload"]
    """<p>The intended use of the Autonomous Database, such as transaction processing, data warehouse, JSON database, or APEX.</p>"""
    character_set: NotRequired["str"]
    """<p>The character set of the Autonomous Database.</p>"""
    ncharacter_set: NotRequired["str"]
    """<p>The national character set of the Autonomous Database.</p>"""
    database_edition: NotRequired["aws_sdk_odb.types.database_edition.DatabaseEdition"]
    """<p>The Oracle Database edition of the Autonomous Database.</p>"""
    license_model: NotRequired["aws_sdk_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model that applies to the Autonomous Database.</p>"""
    open_mode: NotRequired["aws_sdk_odb.types.open_mode.OpenMode"]
    """<p>The mode in which the Autonomous Database is open, either read-only or read/write.</p>"""
    permission_level: NotRequired["aws_sdk_odb.types.permission_level.PermissionLevel"]
    """<p>The permission level of the Autonomous Database.</p>"""
    is_mtls_connection_required: NotRequired["bool"]
    """<p>Indicates whether mutual TLS (mTLS) authentication is required to connect to the Autonomous Database.</p>"""
    autonomous_maintenance_schedule_type: NotRequired[
        "aws_sdk_odb.types.autonomous_maintenance_schedule_type.AutonomousMaintenanceScheduleType"
    ]
    """<p>The maintenance schedule type for the Autonomous Database.</p>"""
    net_services_architecture: NotRequired[
        "aws_sdk_odb.types.net_services_architecture.NetServicesArchitecture"
    ]
    """<p>The Oracle Net Services architecture of the Autonomous Database, either dedicated or shared.</p>"""
    available_upgrade_versions: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The list of Oracle Database software versions to which the Autonomous Database can be upgraded.</p>"""
    byol_compute_count_limit: NotRequired["int"]
    """<p>The maximum number of compute resources that you can allocate to the Autonomous Database under the bring-your-own-license (BYOL) model.</p>"""
    connection_string_details: NotRequired[
        "aws_sdk_odb.types.autonomous_database_connection_strings.AutonomousDatabaseConnectionStrings"
    ]
    """<p>The connection string details for the Autonomous Database.</p>"""
    service_console_url: NotRequired["str"]
    """<p>The URL for accessing the Oracle service console for the Autonomous Database.</p>"""
    sql_web_developer_url: NotRequired["str"]
    """<p>The URL for accessing Oracle SQL Developer Web for the Autonomous Database.</p>"""
    customer_contacts: NotRequired[
        "aws_sdk_odb.types.customer_contacts.CustomerContacts"
    ]
    """<p>The list of customer contacts that receive operational notifications from Oracle for the Autonomous Database.</p>"""
    apex_details: NotRequired[
        "aws_sdk_odb.types.autonomous_database_apex.AutonomousDatabaseApex"
    ]
    """<p>The Oracle Application Express (APEX) details for the Autonomous Database.</p>"""
    standby_db: NotRequired[
        "aws_sdk_odb.types.database_standby_summary.DatabaseStandbySummary"
    ]
    """<p>The details of the standby Autonomous Database in a cross-Region Oracle Data Guard configuration.</p>"""
    local_standby_db: NotRequired[
        "aws_sdk_odb.types.database_standby_summary.DatabaseStandbySummary"
    ]
    """<p>The details of the local standby Autonomous Database in an Oracle Data Guard configuration.</p>"""
    data_safe_status: NotRequired["aws_sdk_odb.types.data_safe_status.DataSafeStatus"]
    """<p>The status of the Oracle Data Safe registration for the Autonomous Database.</p>"""
    database_management_status: NotRequired[
        "aws_sdk_odb.types.database_management_status.DatabaseManagementStatus"
    ]
    """<p>The status of Oracle Database Management for the Autonomous Database.</p>"""
    operations_insights_status: NotRequired[
        "aws_sdk_odb.types.operations_insights_status.OperationsInsightsStatus"
    ]
    """<p>The status of Oracle Operations Insights for the Autonomous Database.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Availability Zone where the Autonomous Database is located.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The unique identifier of the Availability Zone where the Autonomous Database is located.</p>"""
    maintenance_target_component: NotRequired["str"]
    """<p>The component on the Autonomous Database that the current maintenance is being applied to.</p>"""
    connection_urls: NotRequired[
        "aws_sdk_odb.types.autonomous_database_connection_urls.AutonomousDatabaseConnectionUrls"
    ]
    """<p>The connection URLs for accessing tools and services for the Autonomous Database.</p>"""
    db_tools_details: NotRequired[
        "aws_sdk_odb.types.database_tool_list.DatabaseToolList"
    ]
    """<p>The list of database management tools enabled for the Autonomous Database.</p>"""
    scheduled_operations: NotRequired[
        "aws_sdk_odb.types.scheduled_operation_details_list.ScheduledOperationDetailsList"
    ]
    """<p>The list of scheduled start and stop times for the Autonomous Database.</p>"""
    resource_pool_leader_id: NotRequired["str"]
    """<p>The unique identifier of the resource pool leader Autonomous Database.</p>"""
    compute_count: NotRequired["float"]
    """<p>The compute capacity, in number of Elastic CPUs (ECPUs) or Oracle CPUs (OCPUs), assigned to the Autonomous Database.</p>"""
    compute_model: NotRequired["aws_sdk_odb.types.compute_model.ComputeModel"]
    """<p>The compute model of the Autonomous Database, either ECPU or OCPU.</p>"""
    cpu_core_count: NotRequired["int"]
    """<p>The number of CPU cores allocated to the Autonomous Database.</p>"""
    memory_per_oracle_compute_unit_in_g_bs: NotRequired["int"]
    """<p>The amount of memory allocated per Oracle Compute Unit, in GB.</p>"""
    provisionable_cpus: NotRequired["aws_sdk_odb.types.integer_list.IntegerList"]
    """<p>The list of CPU core counts that you can provision for the Autonomous Database.</p>"""
    is_auto_scaling_enabled: NotRequired["bool"]
    """<p>Indicates whether automatic scaling of the compute resources is enabled for the Autonomous Database.</p>"""
    data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The size, in terabytes (TB), of the data volume allocated for the Autonomous Database.</p>"""
    data_storage_size_in_g_bs: NotRequired["int"]
    """<p>The size, in gigabytes (GB), of the data volume allocated for the Autonomous Database.</p>"""
    used_data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The amount of data storage currently in use by the Autonomous Database, in TB.</p>"""
    used_data_storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of data storage currently in use by the Autonomous Database, in GB.</p>"""
    actual_used_data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The actual amount of data storage currently in use by the Autonomous Database, in TB.</p>"""
    allocated_storage_size_in_t_bs: NotRequired["float"]
    """<p>The amount of storage currently allocated to the Autonomous Database, in TB.</p>"""
    in_memory_area_in_g_bs: NotRequired["int"]
    """<p>The size of the in-memory area of the Autonomous Database, in GB.</p>"""
    is_auto_scaling_for_storage_enabled: NotRequired["bool"]
    """<p>Indicates whether automatic scaling of the storage is enabled for the Autonomous Database.</p>"""
    odb_network_id: NotRequired["aws_sdk_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the ODB network associated with the Autonomous Database.</p>"""
    odb_network_arn: NotRequired["aws_sdk_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the ODB network associated with the Autonomous Database.</p>"""
    private_endpoint: NotRequired["str"]
    """<p>The private endpoint for the Autonomous Database.</p>"""
    private_endpoint_ip: NotRequired["str"]
    """<p>The private endpoint IP address for the Autonomous Database.</p>"""
    private_endpoint_label: NotRequired["str"]
    """<p>The private endpoint label for the Autonomous Database.</p>"""
    allowlisted_ips: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The list of IP addresses that are allowed to access the Autonomous Database.</p>"""
    standby_allowlisted_ips: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The list of IP addresses that are allowed to access the standby Autonomous Database.</p>"""
    standby_allowlisted_ips_source: NotRequired[
        "aws_sdk_odb.types.standby_allowlisted_ips_source.StandbyAllowlistedIpsSource"
    ]
    """<p>The source of the allowlisted IP addresses for the standby Autonomous Database.</p>"""
    is_local_data_guard_enabled: NotRequired["bool"]
    """<p>Indicates whether local Oracle Data Guard is enabled for the Autonomous Database.</p>"""
    is_remote_data_guard_enabled: NotRequired["bool"]
    """<p>Indicates whether remote Oracle Data Guard is enabled for the Autonomous Database.</p>"""
    local_disaster_recovery_type: NotRequired[
        "aws_sdk_odb.types.disaster_recovery_type.DisasterRecoveryType"
    ]
    """<p>The type of local disaster recovery configured for the Autonomous Database.</p>"""
    role: NotRequired["aws_sdk_odb.types.data_guard_role.DataGuardRole"]
    """<p>The Oracle Data Guard role of the Autonomous Database.</p>"""
    peer_db_ids: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The list of unique identifiers of the peer Autonomous Databases.</p>"""
    failed_data_recovery_in_seconds: NotRequired["int"]
    """<p>The amount of time, in seconds, that the data in the Autonomous Database is behind the data in the primary database.</p>"""
    local_adg_auto_failover_max_data_loss_limit: NotRequired["int"]
    """<p>The maximum data loss limit, in seconds, for automatic failover to the local Oracle Data Guard standby database.</p>"""
    remote_disaster_recovery_configuration: NotRequired[
        "aws_sdk_odb.types.disaster_recovery_configuration.DisasterRecoveryConfiguration"
    ]
    """<p>The configuration of the remote disaster recovery for the Autonomous Database.</p>"""
    is_refreshable_clone: NotRequired["bool"]
    """<p>Indicates whether the Autonomous Database is a refreshable clone.</p>"""
    refreshable_mode: NotRequired["aws_sdk_odb.types.refreshable_mode.RefreshableMode"]
    """<p>The refresh mode of the refreshable clone Autonomous Database.</p>"""
    refreshable_status: NotRequired[
        "aws_sdk_odb.types.refreshable_status.RefreshableStatus"
    ]
    """<p>The refresh status of the refreshable clone Autonomous Database.</p>"""
    auto_refresh_frequency_in_seconds: NotRequired["int"]
    """<p>The frequency, in seconds, at which the refreshable clone Autonomous Database is automatically refreshed.</p>"""
    auto_refresh_point_lag_in_seconds: NotRequired["int"]
    """<p>The time lag, in seconds, between the refreshable clone and its source Autonomous Database.</p>"""
    is_reconnect_clone_enabled: NotRequired["bool"]
    """<p>Indicates whether reconnecting the refreshable clone to its source Autonomous Database is enabled.</p>"""
    clone_table_space_list: NotRequired["aws_sdk_odb.types.integer_list.IntegerList"]
    """<p>The list of tablespace identifiers to clone for the Autonomous Database.</p>"""
    backup_retention_period_in_days: NotRequired["int"]
    """<p>The retention period, in days, for automatic backups of the Autonomous Database.</p>"""
    long_term_backup_schedule: NotRequired[
        "aws_sdk_odb.types.long_term_backup_schedule.LongTermBackupSchedule"
    ]
    """<p>The long-term backup schedule for the Autonomous Database.</p>"""
    is_backup_retention_locked: NotRequired["bool"]
    """<p>Indicates whether the backup retention period of the Autonomous Database is locked.</p>"""
    total_backup_storage_size_in_g_bs: NotRequired["float"]
    """<p>The total amount of backup storage used by the Autonomous Database, in GB.</p>"""
    resource_pool_summary: NotRequired[
        "aws_sdk_odb.types.resource_pool_summary.ResourcePoolSummary"
    ]
    """<p>The configuration of the resource pool for the Autonomous Database.</p>"""
    encryption_summary: NotRequired[
        "aws_sdk_odb.types.encryption_summary.EncryptionSummary"
    ]
    """<p>The encryption configuration for the Autonomous Database.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the Autonomous Database was created.</p>"""
    time_of_last_backup: NotRequired["datetime.datetime"]
    """<p>The date and time of the last backup of the Autonomous Database.</p>"""
    time_maintenance_begin: NotRequired["datetime.datetime"]
    """<p>The date and time when the next maintenance of the Autonomous Database begins.</p>"""
    time_maintenance_end: NotRequired["datetime.datetime"]
    """<p>The date and time when the next maintenance of the Autonomous Database ends.</p>"""
    time_local_data_guard_enabled: NotRequired["datetime.datetime"]
    """<p>The date and time when local Oracle Data Guard was enabled for the Autonomous Database.</p>"""
    time_data_guard_role_changed: NotRequired["datetime.datetime"]
    """<p>The date and time when the Oracle Data Guard role of the Autonomous Database last changed.</p>"""
    time_of_last_switchover: NotRequired["datetime.datetime"]
    """<p>The date and time of the last switchover operation for the Autonomous Database.</p>"""
    time_of_last_failover: NotRequired["datetime.datetime"]
    """<p>The date and time of the last failover operation for the Autonomous Database.</p>"""
    time_of_last_refresh: NotRequired["datetime.datetime"]
    """<p>The date and time of the last refresh of the refreshable clone Autonomous Database.</p>"""
    time_of_last_refresh_point: NotRequired["datetime.datetime"]
    """<p>The date and time as of which the data in the refreshable clone Autonomous Database is current.</p>"""
    time_of_next_refresh: NotRequired["datetime.datetime"]
    """<p>The date and time of the next scheduled refresh of the refreshable clone Autonomous Database.</p>"""
    time_of_auto_refresh_start: NotRequired["datetime.datetime"]
    """<p>The date and time at which the automatic refresh of the refreshable clone Autonomous Database starts.</p>"""
    time_deletion_of_free_autonomous_database: NotRequired["datetime.datetime"]
    """<p>The date and time when the inactive Always Free Autonomous Database is scheduled to be automatically deleted.</p>"""
    time_reclamation_of_free_autonomous_database: NotRequired["datetime.datetime"]
    """<p>The date and time when the Always Free Autonomous Database is scheduled to be stopped because of inactivity.</p>"""
    time_disaster_recovery_role_changed: NotRequired["datetime.datetime"]
    """<p>The date and time when the disaster recovery role of the Autonomous Database last changed.</p>"""
    time_until_reconnect_clone_enabled: NotRequired["datetime.datetime"]
    """<p>The date and time until which reconnecting the refreshable clone to its source Autonomous Database is allowed.</p>"""
    next_long_term_backup_time_stamp: NotRequired["datetime.datetime"]
    """<p>The date and time of the next scheduled long-term backup of the Autonomous Database.</p>"""
    time_undeleted: NotRequired["datetime.datetime"]
    """<p>The date and time when the Autonomous Database was restored after deletion.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseSummary) -> dict:
    out: dict = {}
    if "autonomous_database_id" in value:
        out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "autonomous_database_arn" in value:
        out["autonomousDatabaseArn"] = value["autonomous_database_arn"]
    if "oci_resource_anchor_name" in value:
        out["ociResourceAnchorName"] = value["oci_resource_anchor_name"]
    if "percent_progress" in value:
        out["percentProgress"] = value["percent_progress"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "oci_url" in value:
        out["ociUrl"] = value["oci_url"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "db_name" in value:
        out["dbName"] = value["db_name"]
    if "source_id" in value:
        out["sourceId"] = value["source_id"]
    if "status" in value:
        import aws_sdk_odb.types.autonomous_database_resource_status

        out["status"] = (
            aws_sdk_odb.types.autonomous_database_resource_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "database_type" in value:
        import aws_sdk_odb.types.database_type

        out["databaseType"] = aws_sdk_odb.types.database_type.serialize_aws_json_1_0(
            value["database_type"]
        )
    if "db_version" in value:
        out["dbVersion"] = value["db_version"]
    if "db_workload" in value:
        import aws_sdk_odb.types.db_workload

        out["dbWorkload"] = aws_sdk_odb.types.db_workload.serialize_aws_json_1_0(
            value["db_workload"]
        )
    if "character_set" in value:
        out["characterSet"] = value["character_set"]
    if "ncharacter_set" in value:
        out["ncharacterSet"] = value["ncharacter_set"]
    if "database_edition" in value:
        import aws_sdk_odb.types.database_edition

        out["databaseEdition"] = (
            aws_sdk_odb.types.database_edition.serialize_aws_json_1_0(
                value["database_edition"]
            )
        )
    if "license_model" in value:
        import aws_sdk_odb.types.license_model

        out["licenseModel"] = aws_sdk_odb.types.license_model.serialize_aws_json_1_0(
            value["license_model"]
        )
    if "open_mode" in value:
        import aws_sdk_odb.types.open_mode

        out["openMode"] = aws_sdk_odb.types.open_mode.serialize_aws_json_1_0(
            value["open_mode"]
        )
    if "permission_level" in value:
        import aws_sdk_odb.types.permission_level

        out["permissionLevel"] = (
            aws_sdk_odb.types.permission_level.serialize_aws_json_1_0(
                value["permission_level"]
            )
        )
    if "is_mtls_connection_required" in value:
        out["isMtlsConnectionRequired"] = value["is_mtls_connection_required"]
    if "autonomous_maintenance_schedule_type" in value:
        import aws_sdk_odb.types.autonomous_maintenance_schedule_type

        out["autonomousMaintenanceScheduleType"] = (
            aws_sdk_odb.types.autonomous_maintenance_schedule_type.serialize_aws_json_1_0(
                value["autonomous_maintenance_schedule_type"]
            )
        )
    if "net_services_architecture" in value:
        import aws_sdk_odb.types.net_services_architecture

        out["netServicesArchitecture"] = (
            aws_sdk_odb.types.net_services_architecture.serialize_aws_json_1_0(
                value["net_services_architecture"]
            )
        )
    if "available_upgrade_versions" in value:
        import aws_sdk_odb.types.string_list

        out["availableUpgradeVersions"] = (
            aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
                value["available_upgrade_versions"]
            )
        )
    if "byol_compute_count_limit" in value:
        out["byolComputeCountLimit"] = value["byol_compute_count_limit"]
    if "connection_string_details" in value:
        import aws_sdk_odb.types.autonomous_database_connection_strings

        out["connectionStringDetails"] = (
            aws_sdk_odb.types.autonomous_database_connection_strings.serialize_aws_json_1_0(
                value["connection_string_details"]
            )
        )
    if "service_console_url" in value:
        out["serviceConsoleUrl"] = value["service_console_url"]
    if "sql_web_developer_url" in value:
        out["sqlWebDeveloperUrl"] = value["sql_web_developer_url"]
    if "customer_contacts" in value:
        import aws_sdk_odb.types.customer_contacts

        out["customerContacts"] = (
            aws_sdk_odb.types.customer_contacts.serialize_aws_json_1_0(
                value["customer_contacts"]
            )
        )
    if "apex_details" in value:
        import aws_sdk_odb.types.autonomous_database_apex

        out["apexDetails"] = (
            aws_sdk_odb.types.autonomous_database_apex.serialize_aws_json_1_0(
                value["apex_details"]
            )
        )
    if "standby_db" in value:
        import aws_sdk_odb.types.database_standby_summary

        out["standbyDb"] = (
            aws_sdk_odb.types.database_standby_summary.serialize_aws_json_1_0(
                value["standby_db"]
            )
        )
    if "local_standby_db" in value:
        import aws_sdk_odb.types.database_standby_summary

        out["localStandbyDb"] = (
            aws_sdk_odb.types.database_standby_summary.serialize_aws_json_1_0(
                value["local_standby_db"]
            )
        )
    if "data_safe_status" in value:
        import aws_sdk_odb.types.data_safe_status

        out["dataSafeStatus"] = (
            aws_sdk_odb.types.data_safe_status.serialize_aws_json_1_0(
                value["data_safe_status"]
            )
        )
    if "database_management_status" in value:
        import aws_sdk_odb.types.database_management_status

        out["databaseManagementStatus"] = (
            aws_sdk_odb.types.database_management_status.serialize_aws_json_1_0(
                value["database_management_status"]
            )
        )
    if "operations_insights_status" in value:
        import aws_sdk_odb.types.operations_insights_status

        out["operationsInsightsStatus"] = (
            aws_sdk_odb.types.operations_insights_status.serialize_aws_json_1_0(
                value["operations_insights_status"]
            )
        )
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "maintenance_target_component" in value:
        out["maintenanceTargetComponent"] = value["maintenance_target_component"]
    if "connection_urls" in value:
        import aws_sdk_odb.types.autonomous_database_connection_urls

        out["connectionUrls"] = (
            aws_sdk_odb.types.autonomous_database_connection_urls.serialize_aws_json_1_0(
                value["connection_urls"]
            )
        )
    if "db_tools_details" in value:
        import aws_sdk_odb.types.database_tool_list

        out["dbToolsDetails"] = (
            aws_sdk_odb.types.database_tool_list.serialize_aws_json_1_0(
                value["db_tools_details"]
            )
        )
    if "scheduled_operations" in value:
        import aws_sdk_odb.types.scheduled_operation_details_list

        out["scheduledOperations"] = (
            aws_sdk_odb.types.scheduled_operation_details_list.serialize_aws_json_1_0(
                value["scheduled_operations"]
            )
        )
    if "resource_pool_leader_id" in value:
        out["resourcePoolLeaderId"] = value["resource_pool_leader_id"]
    if "compute_count" in value:
        out["computeCount"] = value["compute_count"]
    if "compute_model" in value:
        import aws_sdk_odb.types.compute_model

        out["computeModel"] = aws_sdk_odb.types.compute_model.serialize_aws_json_1_0(
            value["compute_model"]
        )
    if "cpu_core_count" in value:
        out["cpuCoreCount"] = value["cpu_core_count"]
    if "memory_per_oracle_compute_unit_in_g_bs" in value:
        out["memoryPerOracleComputeUnitInGBs"] = value[
            "memory_per_oracle_compute_unit_in_g_bs"
        ]
    if "provisionable_cpus" in value:
        import aws_sdk_odb.types.integer_list

        out["provisionableCpus"] = (
            aws_sdk_odb.types.integer_list.serialize_aws_json_1_0(
                value["provisionable_cpus"]
            )
        )
    if "is_auto_scaling_enabled" in value:
        out["isAutoScalingEnabled"] = value["is_auto_scaling_enabled"]
    if "data_storage_size_in_t_bs" in value:
        out["dataStorageSizeInTBs"] = value["data_storage_size_in_t_bs"]
    if "data_storage_size_in_g_bs" in value:
        out["dataStorageSizeInGBs"] = value["data_storage_size_in_g_bs"]
    if "used_data_storage_size_in_t_bs" in value:
        out["usedDataStorageSizeInTBs"] = value["used_data_storage_size_in_t_bs"]
    if "used_data_storage_size_in_g_bs" in value:
        out["usedDataStorageSizeInGBs"] = value["used_data_storage_size_in_g_bs"]
    if "actual_used_data_storage_size_in_t_bs" in value:
        out["actualUsedDataStorageSizeInTBs"] = value[
            "actual_used_data_storage_size_in_t_bs"
        ]
    if "allocated_storage_size_in_t_bs" in value:
        out["allocatedStorageSizeInTBs"] = value["allocated_storage_size_in_t_bs"]
    if "in_memory_area_in_g_bs" in value:
        out["inMemoryAreaInGBs"] = value["in_memory_area_in_g_bs"]
    if "is_auto_scaling_for_storage_enabled" in value:
        out["isAutoScalingForStorageEnabled"] = value[
            "is_auto_scaling_for_storage_enabled"
        ]
    if "odb_network_id" in value:
        out["odbNetworkId"] = value["odb_network_id"]
    if "odb_network_arn" in value:
        out["odbNetworkArn"] = value["odb_network_arn"]
    if "private_endpoint" in value:
        out["privateEndpoint"] = value["private_endpoint"]
    if "private_endpoint_ip" in value:
        out["privateEndpointIp"] = value["private_endpoint_ip"]
    if "private_endpoint_label" in value:
        out["privateEndpointLabel"] = value["private_endpoint_label"]
    if "allowlisted_ips" in value:
        import aws_sdk_odb.types.string_list

        out["allowlistedIps"] = aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
            value["allowlisted_ips"]
        )
    if "standby_allowlisted_ips" in value:
        import aws_sdk_odb.types.string_list

        out["standbyAllowlistedIps"] = (
            aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
                value["standby_allowlisted_ips"]
            )
        )
    if "standby_allowlisted_ips_source" in value:
        import aws_sdk_odb.types.standby_allowlisted_ips_source

        out["standbyAllowlistedIpsSource"] = (
            aws_sdk_odb.types.standby_allowlisted_ips_source.serialize_aws_json_1_0(
                value["standby_allowlisted_ips_source"]
            )
        )
    if "is_local_data_guard_enabled" in value:
        out["isLocalDataGuardEnabled"] = value["is_local_data_guard_enabled"]
    if "is_remote_data_guard_enabled" in value:
        out["isRemoteDataGuardEnabled"] = value["is_remote_data_guard_enabled"]
    if "local_disaster_recovery_type" in value:
        import aws_sdk_odb.types.disaster_recovery_type

        out["localDisasterRecoveryType"] = (
            aws_sdk_odb.types.disaster_recovery_type.serialize_aws_json_1_0(
                value["local_disaster_recovery_type"]
            )
        )
    if "role" in value:
        import aws_sdk_odb.types.data_guard_role

        out["role"] = aws_sdk_odb.types.data_guard_role.serialize_aws_json_1_0(
            value["role"]
        )
    if "peer_db_ids" in value:
        import aws_sdk_odb.types.string_list

        out["peerDbIds"] = aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
            value["peer_db_ids"]
        )
    if "failed_data_recovery_in_seconds" in value:
        out["failedDataRecoveryInSeconds"] = value["failed_data_recovery_in_seconds"]
    if "local_adg_auto_failover_max_data_loss_limit" in value:
        out["localAdgAutoFailoverMaxDataLossLimit"] = value[
            "local_adg_auto_failover_max_data_loss_limit"
        ]
    if "remote_disaster_recovery_configuration" in value:
        import aws_sdk_odb.types.disaster_recovery_configuration

        out["remoteDisasterRecoveryConfiguration"] = (
            aws_sdk_odb.types.disaster_recovery_configuration.serialize_aws_json_1_0(
                value["remote_disaster_recovery_configuration"]
            )
        )
    if "is_refreshable_clone" in value:
        out["isRefreshableClone"] = value["is_refreshable_clone"]
    if "refreshable_mode" in value:
        import aws_sdk_odb.types.refreshable_mode

        out["refreshableMode"] = (
            aws_sdk_odb.types.refreshable_mode.serialize_aws_json_1_0(
                value["refreshable_mode"]
            )
        )
    if "refreshable_status" in value:
        import aws_sdk_odb.types.refreshable_status

        out["refreshableStatus"] = (
            aws_sdk_odb.types.refreshable_status.serialize_aws_json_1_0(
                value["refreshable_status"]
            )
        )
    if "auto_refresh_frequency_in_seconds" in value:
        out["autoRefreshFrequencyInSeconds"] = value[
            "auto_refresh_frequency_in_seconds"
        ]
    if "auto_refresh_point_lag_in_seconds" in value:
        out["autoRefreshPointLagInSeconds"] = value["auto_refresh_point_lag_in_seconds"]
    if "is_reconnect_clone_enabled" in value:
        out["isReconnectCloneEnabled"] = value["is_reconnect_clone_enabled"]
    if "clone_table_space_list" in value:
        import aws_sdk_odb.types.integer_list

        out["cloneTableSpaceList"] = (
            aws_sdk_odb.types.integer_list.serialize_aws_json_1_0(
                value["clone_table_space_list"]
            )
        )
    if "backup_retention_period_in_days" in value:
        out["backupRetentionPeriodInDays"] = value["backup_retention_period_in_days"]
    if "long_term_backup_schedule" in value:
        import aws_sdk_odb.types.long_term_backup_schedule

        out["longTermBackupSchedule"] = (
            aws_sdk_odb.types.long_term_backup_schedule.serialize_aws_json_1_0(
                value["long_term_backup_schedule"]
            )
        )
    if "is_backup_retention_locked" in value:
        out["isBackupRetentionLocked"] = value["is_backup_retention_locked"]
    if "total_backup_storage_size_in_g_bs" in value:
        out["totalBackupStorageSizeInGBs"] = value["total_backup_storage_size_in_g_bs"]
    if "resource_pool_summary" in value:
        import aws_sdk_odb.types.resource_pool_summary

        out["resourcePoolSummary"] = (
            aws_sdk_odb.types.resource_pool_summary.serialize_aws_json_1_0(
                value["resource_pool_summary"]
            )
        )
    if "encryption_summary" in value:
        import aws_sdk_odb.types.encryption_summary

        out["encryptionSummary"] = (
            aws_sdk_odb.types.encryption_summary.serialize_aws_json_1_0(
                value["encryption_summary"]
            )
        )
    if "created_at" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["createdAt"] = aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "time_of_last_backup" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeOfLastBackup"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_of_last_backup"]
            )
        )
    if "time_maintenance_begin" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeMaintenanceBegin"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_maintenance_begin"]
            )
        )
    if "time_maintenance_end" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeMaintenanceEnd"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_maintenance_end"]
            )
        )
    if "time_local_data_guard_enabled" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeLocalDataGuardEnabled"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_local_data_guard_enabled"]
            )
        )
    if "time_data_guard_role_changed" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeDataGuardRoleChanged"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_data_guard_role_changed"]
            )
        )
    if "time_of_last_switchover" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeOfLastSwitchover"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_of_last_switchover"]
            )
        )
    if "time_of_last_failover" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeOfLastFailover"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_of_last_failover"]
            )
        )
    if "time_of_last_refresh" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeOfLastRefresh"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_of_last_refresh"]
            )
        )
    if "time_of_last_refresh_point" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeOfLastRefreshPoint"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_of_last_refresh_point"]
            )
        )
    if "time_of_next_refresh" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeOfNextRefresh"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_of_next_refresh"]
            )
        )
    if "time_of_auto_refresh_start" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeOfAutoRefreshStart"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_of_auto_refresh_start"]
            )
        )
    if "time_deletion_of_free_autonomous_database" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeDeletionOfFreeAutonomousDatabase"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_deletion_of_free_autonomous_database"]
            )
        )
    if "time_reclamation_of_free_autonomous_database" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeReclamationOfFreeAutonomousDatabase"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_reclamation_of_free_autonomous_database"]
            )
        )
    if "time_disaster_recovery_role_changed" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeDisasterRecoveryRoleChanged"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_disaster_recovery_role_changed"]
            )
        )
    if "time_until_reconnect_clone_enabled" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeUntilReconnectCloneEnabled"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_until_reconnect_clone_enabled"]
            )
        )
    if "next_long_term_backup_time_stamp" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["nextLongTermBackupTimeStamp"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["next_long_term_backup_time_stamp"]
            )
        )
    if "time_undeleted" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeUndeleted"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_undeleted"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutonomousDatabaseSummary:
    out: AutonomousDatabaseSummary = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseId" in data:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    if "autonomousDatabaseArn" in data:
        out["autonomous_database_arn"] = data["autonomousDatabaseArn"]
    if "ociResourceAnchorName" in data:
        out["oci_resource_anchor_name"] = data["ociResourceAnchorName"]
    if "percentProgress" in data:
        out["percent_progress"] = data["percentProgress"]
    if "ocid" in data:
        out["ocid"] = data["ocid"]
    if "ociUrl" in data:
        out["oci_url"] = data["ociUrl"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "dbName" in data:
        out["db_name"] = data["dbName"]
    if "sourceId" in data:
        out["source_id"] = data["sourceId"]
    if "status" in data:
        import aws_sdk_odb.types.autonomous_database_resource_status

        out["status"] = (
            aws_sdk_odb.types.autonomous_database_resource_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "databaseType" in data:
        import aws_sdk_odb.types.database_type

        out["database_type"] = aws_sdk_odb.types.database_type.deserialize_aws_json_1_0(
            data["databaseType"]
        )
    if "dbVersion" in data:
        out["db_version"] = data["dbVersion"]
    if "dbWorkload" in data:
        import aws_sdk_odb.types.db_workload

        out["db_workload"] = aws_sdk_odb.types.db_workload.deserialize_aws_json_1_0(
            data["dbWorkload"]
        )
    if "characterSet" in data:
        out["character_set"] = data["characterSet"]
    if "ncharacterSet" in data:
        out["ncharacter_set"] = data["ncharacterSet"]
    if "databaseEdition" in data:
        import aws_sdk_odb.types.database_edition

        out["database_edition"] = (
            aws_sdk_odb.types.database_edition.deserialize_aws_json_1_0(
                data["databaseEdition"]
            )
        )
    if "licenseModel" in data:
        import aws_sdk_odb.types.license_model

        out["license_model"] = aws_sdk_odb.types.license_model.deserialize_aws_json_1_0(
            data["licenseModel"]
        )
    if "openMode" in data:
        import aws_sdk_odb.types.open_mode

        out["open_mode"] = aws_sdk_odb.types.open_mode.deserialize_aws_json_1_0(
            data["openMode"]
        )
    if "permissionLevel" in data:
        import aws_sdk_odb.types.permission_level

        out["permission_level"] = (
            aws_sdk_odb.types.permission_level.deserialize_aws_json_1_0(
                data["permissionLevel"]
            )
        )
    if "isMtlsConnectionRequired" in data:
        out["is_mtls_connection_required"] = data["isMtlsConnectionRequired"]
    if "autonomousMaintenanceScheduleType" in data:
        import aws_sdk_odb.types.autonomous_maintenance_schedule_type

        out["autonomous_maintenance_schedule_type"] = (
            aws_sdk_odb.types.autonomous_maintenance_schedule_type.deserialize_aws_json_1_0(
                data["autonomousMaintenanceScheduleType"]
            )
        )
    if "netServicesArchitecture" in data:
        import aws_sdk_odb.types.net_services_architecture

        out["net_services_architecture"] = (
            aws_sdk_odb.types.net_services_architecture.deserialize_aws_json_1_0(
                data["netServicesArchitecture"]
            )
        )
    if "availableUpgradeVersions" in data:
        import aws_sdk_odb.types.string_list

        out["available_upgrade_versions"] = (
            aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
                data["availableUpgradeVersions"]
            )
        )
    if "byolComputeCountLimit" in data:
        out["byol_compute_count_limit"] = data["byolComputeCountLimit"]
    if "connectionStringDetails" in data:
        import aws_sdk_odb.types.autonomous_database_connection_strings

        out["connection_string_details"] = (
            aws_sdk_odb.types.autonomous_database_connection_strings.deserialize_aws_json_1_0(
                data["connectionStringDetails"]
            )
        )
    if "serviceConsoleUrl" in data:
        out["service_console_url"] = data["serviceConsoleUrl"]
    if "sqlWebDeveloperUrl" in data:
        out["sql_web_developer_url"] = data["sqlWebDeveloperUrl"]
    if "customerContacts" in data:
        import aws_sdk_odb.types.customer_contacts

        out["customer_contacts"] = (
            aws_sdk_odb.types.customer_contacts.deserialize_aws_json_1_0(
                data["customerContacts"]
            )
        )
    if "apexDetails" in data:
        import aws_sdk_odb.types.autonomous_database_apex

        out["apex_details"] = (
            aws_sdk_odb.types.autonomous_database_apex.deserialize_aws_json_1_0(
                data["apexDetails"]
            )
        )
    if "standbyDb" in data:
        import aws_sdk_odb.types.database_standby_summary

        out["standby_db"] = (
            aws_sdk_odb.types.database_standby_summary.deserialize_aws_json_1_0(
                data["standbyDb"]
            )
        )
    if "localStandbyDb" in data:
        import aws_sdk_odb.types.database_standby_summary

        out["local_standby_db"] = (
            aws_sdk_odb.types.database_standby_summary.deserialize_aws_json_1_0(
                data["localStandbyDb"]
            )
        )
    if "dataSafeStatus" in data:
        import aws_sdk_odb.types.data_safe_status

        out["data_safe_status"] = (
            aws_sdk_odb.types.data_safe_status.deserialize_aws_json_1_0(
                data["dataSafeStatus"]
            )
        )
    if "databaseManagementStatus" in data:
        import aws_sdk_odb.types.database_management_status

        out["database_management_status"] = (
            aws_sdk_odb.types.database_management_status.deserialize_aws_json_1_0(
                data["databaseManagementStatus"]
            )
        )
    if "operationsInsightsStatus" in data:
        import aws_sdk_odb.types.operations_insights_status

        out["operations_insights_status"] = (
            aws_sdk_odb.types.operations_insights_status.deserialize_aws_json_1_0(
                data["operationsInsightsStatus"]
            )
        )
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if "maintenanceTargetComponent" in data:
        out["maintenance_target_component"] = data["maintenanceTargetComponent"]
    if "connectionUrls" in data:
        import aws_sdk_odb.types.autonomous_database_connection_urls

        out["connection_urls"] = (
            aws_sdk_odb.types.autonomous_database_connection_urls.deserialize_aws_json_1_0(
                data["connectionUrls"]
            )
        )
    if "dbToolsDetails" in data:
        import aws_sdk_odb.types.database_tool_list

        out["db_tools_details"] = (
            aws_sdk_odb.types.database_tool_list.deserialize_aws_json_1_0(
                data["dbToolsDetails"]
            )
        )
    if "scheduledOperations" in data:
        import aws_sdk_odb.types.scheduled_operation_details_list

        out["scheduled_operations"] = (
            aws_sdk_odb.types.scheduled_operation_details_list.deserialize_aws_json_1_0(
                data["scheduledOperations"]
            )
        )
    if "resourcePoolLeaderId" in data:
        out["resource_pool_leader_id"] = data["resourcePoolLeaderId"]
    if "computeCount" in data:
        out["compute_count"] = data["computeCount"]
    if "computeModel" in data:
        import aws_sdk_odb.types.compute_model

        out["compute_model"] = aws_sdk_odb.types.compute_model.deserialize_aws_json_1_0(
            data["computeModel"]
        )
    if "cpuCoreCount" in data:
        out["cpu_core_count"] = data["cpuCoreCount"]
    if "memoryPerOracleComputeUnitInGBs" in data:
        out["memory_per_oracle_compute_unit_in_g_bs"] = data[
            "memoryPerOracleComputeUnitInGBs"
        ]
    if "provisionableCpus" in data:
        import aws_sdk_odb.types.integer_list

        out["provisionable_cpus"] = (
            aws_sdk_odb.types.integer_list.deserialize_aws_json_1_0(
                data["provisionableCpus"]
            )
        )
    if "isAutoScalingEnabled" in data:
        out["is_auto_scaling_enabled"] = data["isAutoScalingEnabled"]
    if "dataStorageSizeInTBs" in data:
        out["data_storage_size_in_t_bs"] = data["dataStorageSizeInTBs"]
    if "dataStorageSizeInGBs" in data:
        out["data_storage_size_in_g_bs"] = data["dataStorageSizeInGBs"]
    if "usedDataStorageSizeInTBs" in data:
        out["used_data_storage_size_in_t_bs"] = data["usedDataStorageSizeInTBs"]
    if "usedDataStorageSizeInGBs" in data:
        out["used_data_storage_size_in_g_bs"] = data["usedDataStorageSizeInGBs"]
    if "actualUsedDataStorageSizeInTBs" in data:
        out["actual_used_data_storage_size_in_t_bs"] = data[
            "actualUsedDataStorageSizeInTBs"
        ]
    if "allocatedStorageSizeInTBs" in data:
        out["allocated_storage_size_in_t_bs"] = data["allocatedStorageSizeInTBs"]
    if "inMemoryAreaInGBs" in data:
        out["in_memory_area_in_g_bs"] = data["inMemoryAreaInGBs"]
    if "isAutoScalingForStorageEnabled" in data:
        out["is_auto_scaling_for_storage_enabled"] = data[
            "isAutoScalingForStorageEnabled"
        ]
    if "odbNetworkId" in data:
        out["odb_network_id"] = data["odbNetworkId"]
    if "odbNetworkArn" in data:
        out["odb_network_arn"] = data["odbNetworkArn"]
    if "privateEndpoint" in data:
        out["private_endpoint"] = data["privateEndpoint"]
    if "privateEndpointIp" in data:
        out["private_endpoint_ip"] = data["privateEndpointIp"]
    if "privateEndpointLabel" in data:
        out["private_endpoint_label"] = data["privateEndpointLabel"]
    if "allowlistedIps" in data:
        import aws_sdk_odb.types.string_list

        out["allowlisted_ips"] = aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
            data["allowlistedIps"]
        )
    if "standbyAllowlistedIps" in data:
        import aws_sdk_odb.types.string_list

        out["standby_allowlisted_ips"] = (
            aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
                data["standbyAllowlistedIps"]
            )
        )
    if "standbyAllowlistedIpsSource" in data:
        import aws_sdk_odb.types.standby_allowlisted_ips_source

        out["standby_allowlisted_ips_source"] = (
            aws_sdk_odb.types.standby_allowlisted_ips_source.deserialize_aws_json_1_0(
                data["standbyAllowlistedIpsSource"]
            )
        )
    if "isLocalDataGuardEnabled" in data:
        out["is_local_data_guard_enabled"] = data["isLocalDataGuardEnabled"]
    if "isRemoteDataGuardEnabled" in data:
        out["is_remote_data_guard_enabled"] = data["isRemoteDataGuardEnabled"]
    if "localDisasterRecoveryType" in data:
        import aws_sdk_odb.types.disaster_recovery_type

        out["local_disaster_recovery_type"] = (
            aws_sdk_odb.types.disaster_recovery_type.deserialize_aws_json_1_0(
                data["localDisasterRecoveryType"]
            )
        )
    if "role" in data:
        import aws_sdk_odb.types.data_guard_role

        out["role"] = aws_sdk_odb.types.data_guard_role.deserialize_aws_json_1_0(
            data["role"]
        )
    if "peerDbIds" in data:
        import aws_sdk_odb.types.string_list

        out["peer_db_ids"] = aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
            data["peerDbIds"]
        )
    if "failedDataRecoveryInSeconds" in data:
        out["failed_data_recovery_in_seconds"] = data["failedDataRecoveryInSeconds"]
    if "localAdgAutoFailoverMaxDataLossLimit" in data:
        out["local_adg_auto_failover_max_data_loss_limit"] = data[
            "localAdgAutoFailoverMaxDataLossLimit"
        ]
    if "remoteDisasterRecoveryConfiguration" in data:
        import aws_sdk_odb.types.disaster_recovery_configuration

        out["remote_disaster_recovery_configuration"] = (
            aws_sdk_odb.types.disaster_recovery_configuration.deserialize_aws_json_1_0(
                data["remoteDisasterRecoveryConfiguration"]
            )
        )
    if "isRefreshableClone" in data:
        out["is_refreshable_clone"] = data["isRefreshableClone"]
    if "refreshableMode" in data:
        import aws_sdk_odb.types.refreshable_mode

        out["refreshable_mode"] = (
            aws_sdk_odb.types.refreshable_mode.deserialize_aws_json_1_0(
                data["refreshableMode"]
            )
        )
    if "refreshableStatus" in data:
        import aws_sdk_odb.types.refreshable_status

        out["refreshable_status"] = (
            aws_sdk_odb.types.refreshable_status.deserialize_aws_json_1_0(
                data["refreshableStatus"]
            )
        )
    if "autoRefreshFrequencyInSeconds" in data:
        out["auto_refresh_frequency_in_seconds"] = data["autoRefreshFrequencyInSeconds"]
    if "autoRefreshPointLagInSeconds" in data:
        out["auto_refresh_point_lag_in_seconds"] = data["autoRefreshPointLagInSeconds"]
    if "isReconnectCloneEnabled" in data:
        out["is_reconnect_clone_enabled"] = data["isReconnectCloneEnabled"]
    if "cloneTableSpaceList" in data:
        import aws_sdk_odb.types.integer_list

        out["clone_table_space_list"] = (
            aws_sdk_odb.types.integer_list.deserialize_aws_json_1_0(
                data["cloneTableSpaceList"]
            )
        )
    if "backupRetentionPeriodInDays" in data:
        out["backup_retention_period_in_days"] = data["backupRetentionPeriodInDays"]
    if "longTermBackupSchedule" in data:
        import aws_sdk_odb.types.long_term_backup_schedule

        out["long_term_backup_schedule"] = (
            aws_sdk_odb.types.long_term_backup_schedule.deserialize_aws_json_1_0(
                data["longTermBackupSchedule"]
            )
        )
    if "isBackupRetentionLocked" in data:
        out["is_backup_retention_locked"] = data["isBackupRetentionLocked"]
    if "totalBackupStorageSizeInGBs" in data:
        out["total_backup_storage_size_in_g_bs"] = data["totalBackupStorageSizeInGBs"]
    if "resourcePoolSummary" in data:
        import aws_sdk_odb.types.resource_pool_summary

        out["resource_pool_summary"] = (
            aws_sdk_odb.types.resource_pool_summary.deserialize_aws_json_1_0(
                data["resourcePoolSummary"]
            )
        )
    if "encryptionSummary" in data:
        import aws_sdk_odb.types.encryption_summary

        out["encryption_summary"] = (
            aws_sdk_odb.types.encryption_summary.deserialize_aws_json_1_0(
                data["encryptionSummary"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "timeOfLastBackup" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_of_last_backup"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeOfLastBackup"]
            )
        )
    if "timeMaintenanceBegin" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_maintenance_begin"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeMaintenanceBegin"]
            )
        )
    if "timeMaintenanceEnd" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_maintenance_end"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeMaintenanceEnd"]
            )
        )
    if "timeLocalDataGuardEnabled" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_local_data_guard_enabled"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeLocalDataGuardEnabled"]
            )
        )
    if "timeDataGuardRoleChanged" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_data_guard_role_changed"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeDataGuardRoleChanged"]
            )
        )
    if "timeOfLastSwitchover" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_of_last_switchover"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeOfLastSwitchover"]
            )
        )
    if "timeOfLastFailover" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_of_last_failover"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeOfLastFailover"]
            )
        )
    if "timeOfLastRefresh" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_of_last_refresh"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeOfLastRefresh"]
            )
        )
    if "timeOfLastRefreshPoint" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_of_last_refresh_point"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeOfLastRefreshPoint"]
            )
        )
    if "timeOfNextRefresh" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_of_next_refresh"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeOfNextRefresh"]
            )
        )
    if "timeOfAutoRefreshStart" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_of_auto_refresh_start"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeOfAutoRefreshStart"]
            )
        )
    if "timeDeletionOfFreeAutonomousDatabase" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_deletion_of_free_autonomous_database"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeDeletionOfFreeAutonomousDatabase"]
            )
        )
    if "timeReclamationOfFreeAutonomousDatabase" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_reclamation_of_free_autonomous_database"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeReclamationOfFreeAutonomousDatabase"]
            )
        )
    if "timeDisasterRecoveryRoleChanged" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_disaster_recovery_role_changed"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeDisasterRecoveryRoleChanged"]
            )
        )
    if "timeUntilReconnectCloneEnabled" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_until_reconnect_clone_enabled"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeUntilReconnectCloneEnabled"]
            )
        )
    if "nextLongTermBackupTimeStamp" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["next_long_term_backup_time_stamp"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["nextLongTermBackupTimeStamp"]
            )
        )
    if "timeUndeleted" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_undeleted"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeUndeleted"]
            )
        )
    return out
