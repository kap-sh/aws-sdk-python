"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbInstanceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_rds_db_domain_memberships
    import aws_sdk_securityhub.types.aws_rds_db_instance_associated_roles
    import aws_sdk_securityhub.types.aws_rds_db_instance_endpoint
    import aws_sdk_securityhub.types.aws_rds_db_instance_vpc_security_groups
    import aws_sdk_securityhub.types.aws_rds_db_option_group_memberships
    import aws_sdk_securityhub.types.aws_rds_db_parameter_groups
    import aws_sdk_securityhub.types.aws_rds_db_pending_modified_values
    import aws_sdk_securityhub.types.aws_rds_db_processor_features
    import aws_sdk_securityhub.types.aws_rds_db_status_infos
    import aws_sdk_securityhub.types.aws_rds_db_subnet_group
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class AwsRdsDbInstanceDetails(TypedDict):
    associated_roles: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_instance_associated_roles.AwsRdsDbInstanceAssociatedRoles"
    ]
    """<p>The IAM roles associated with the DB instance.</p>"""
    ca_certificate_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the CA certificate for this DB instance.</p>"""
    db_cluster_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.</p>"""
    db_instance_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.</p>"""
    db_instance_class: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Contains the name of the compute and memory capacity class of the DB instance.</p>"""
    db_instance_port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>Specifies the port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.</p>"""
    dbi_resource_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Web Services Region-unique, immutable identifier for the DB instance. This identifier is found in CloudTrail log entries whenever the KMS key for the DB instance is accessed. </p>"""
    db_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The meaning of this parameter differs according to the database engine you use.</p> <p> <b>MySQL, MariaDB, SQL Server, PostgreSQL</b> </p> <p>Contains the name of the initial database of this instance that was provided at create time, if one was specified when the DB instance was created. This same name is returned for the life of the DB instance.</p> <p> <b>Oracle</b> </p> <p>Contains the Oracle System ID (SID) of the created DB instance. Not shown when the returned parameters don't apply to an Oracle DB instance. </p>"""
    deletion_protection: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the DB instance has deletion protection enabled.</p> <p>When deletion protection is enabled, the database cannot be deleted.</p>"""
    endpoint: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_instance_endpoint.AwsRdsDbInstanceEndpoint"
    ]
    """<p>Specifies the connection endpoint.</p>"""
    engine: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Provides the name of the database engine to use for this DB instance.</p>"""
    engine_version: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates the database engine version.</p>"""
    iam_database_authentication_enabled: NotRequired[
        "aws_sdk_securityhub.types.boolean.Boolean"
    ]
    """<p>True if mapping of IAM accounts to database accounts is enabled, and otherwise false.</p> <p>IAM database authentication can be enabled for the following database engines.</p> <ul> <li> <p>For MySQL 5.6, minor version 5.6.34 or higher</p> </li> <li> <p>For MySQL 5.7, minor version 5.7.16 or higher</p> </li> <li> <p>Aurora 5.6 or higher</p> </li> </ul>"""
    instance_create_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates when the DB instance was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    kms_key_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>If <code>StorageEncrypted</code> is true, the KMS key identifier for the encrypted DB instance.</p>"""
    publicly_accessible: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Specifies the accessibility options for the DB instance.</p> <p>A value of true specifies an Internet-facing instance with a publicly resolvable DNS name, which resolves to a public IP address.</p> <p>A value of false specifies an internal instance with a DNS name that resolves to a private IP address. </p>"""
    storage_encrypted: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Specifies whether the DB instance is encrypted.</p>"""
    tde_credential_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN from the key store with which the instance is associated for TDE encryption.</p>"""
    vpc_security_groups: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_instance_vpc_security_groups.AwsRdsDbInstanceVpcSecurityGroups"
    ]
    """<p>A list of VPC security groups that the DB instance belongs to.</p>"""
    multi_az: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the DB instance is a multiple Availability Zone deployment.</p>"""
    enhanced_monitoring_resource_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the CloudWatch Logs log stream that receives the enhanced monitoring metrics data for the DB instance.</p>"""
    db_instance_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The current status of the DB instance.</p>"""
    master_username: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The master user name of the DB instance.</p>"""
    allocated_storage: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The amount of storage (in gigabytes) to initially allocate for the DB instance.</p>"""
    preferred_backup_window: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The range of time each day when automated backups are created, if automated backups are enabled.</p> <p>Uses the format <code>HH:MM-HH:MM</code>. For example, <code>04:52-05:22</code>.</p>"""
    backup_retention_period: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of days for which to retain automated backups.</p>"""
    db_security_groups: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>A list of the DB security groups to assign to the DB instance.</p>"""
    db_parameter_groups: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_parameter_groups.AwsRdsDbParameterGroups"
    ]
    """<p>A list of the DB parameter groups to assign to the DB instance.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Availability Zone where the DB instance will be created.</p>"""
    db_subnet_group: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_subnet_group.AwsRdsDbSubnetGroup"
    ]
    """<p>Information about the subnet group that is associated with the DB instance.</p>"""
    preferred_maintenance_window: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p>Uses the format <code><day>:HH:MM-<day>:HH:MM</code>.</p> <p>For the day values, use <code>mon</code>|<code>tue</code>|<code>wed</code>|<code>thu</code>|<code>fri</code>|<code>sat</code>|<code>sun</code>.</p> <p>For example, <code>sun:09:32-sun:10:02</code>.</p>"""
    pending_modified_values: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_pending_modified_values.AwsRdsDbPendingModifiedValues"
    ]
    """<p>Changes to the DB instance that are currently pending.</p>"""
    latest_restorable_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies the latest time to which a database can be restored with point-in-time restore.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    auto_minor_version_upgrade: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether minor version patches are applied automatically.</p>"""
    read_replica_source_db_instance_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>If this DB instance is a read replica, contains the identifier of the source DB instance.</p>"""
    read_replica_db_instance_identifiers: NotRequired[
        "aws_sdk_securityhub.types.string_list.StringList"
    ]
    """<p>List of identifiers of the read replicas associated with this DB instance.</p>"""
    read_replica_db_cluster_identifiers: NotRequired[
        "aws_sdk_securityhub.types.string_list.StringList"
    ]
    """<p>List of identifiers of Aurora DB clusters to which the RDS DB instance is replicated as a read replica.</p>"""
    license_model: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>License model information for this DB instance.</p>"""
    iops: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>Specifies the provisioned IOPS (I/O operations per second) for this DB instance.</p>"""
    option_group_memberships: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_option_group_memberships.AwsRdsDbOptionGroupMemberships"
    ]
    """<p>The list of option group memberships for this DB instance.</p>"""
    character_set_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the character set that this DB instance is associated with.</p>"""
    secondary_availability_zone: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>For a DB instance with multi-Availability Zone support, the name of the secondary Availability Zone.</p>"""
    status_infos: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_status_infos.AwsRdsDbStatusInfos"
    ]
    """<p>The status of a read replica. If the instance isn't a read replica, this is empty.</p>"""
    storage_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The storage type for the DB instance.</p>"""
    domain_memberships: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_domain_memberships.AwsRdsDbDomainMemberships"
    ]
    """<p>The Active Directory domain membership records associated with the DB instance.</p>"""
    copy_tags_to_snapshot: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to copy resource tags to snapshots of the DB instance.</p>"""
    monitoring_interval: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The interval, in seconds, between points when enhanced monitoring metrics are collected for the DB instance.</p>"""
    monitoring_role_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN for the IAM role that permits Amazon RDS to send enhanced monitoring metrics to CloudWatch Logs.</p>"""
    promotion_tier: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The order in which to promote an Aurora replica to the primary instance after a failure of the existing primary instance.</p>"""
    timezone: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The time zone of the DB instance.</p>"""
    performance_insights_enabled: NotRequired[
        "aws_sdk_securityhub.types.boolean.Boolean"
    ]
    """<p>Indicates whether Performance Insights is enabled for the DB instance.</p>"""
    performance_insights_kms_key_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the KMS key used to encrypt the Performance Insights data.</p>"""
    performance_insights_retention_period: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>The number of days to retain Performance Insights data.</p>"""
    enabled_cloud_watch_logs_exports: NotRequired[
        "aws_sdk_securityhub.types.string_list.StringList"
    ]
    """<p>A list of log types that this DB instance is configured to export to CloudWatch Logs.</p>"""
    processor_features: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_processor_features.AwsRdsDbProcessorFeatures"
    ]
    """<p>The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.</p>"""
    listener_endpoint: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_instance_endpoint.AwsRdsDbInstanceEndpoint"
    ]
    max_allocated_storage: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The upper limit to which Amazon RDS can automatically scale the storage of the DB instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbInstanceDetails) -> dict:
    out: dict = {}
    if "associated_roles" in value:
        import aws_sdk_securityhub.types.aws_rds_db_instance_associated_roles

        out["AssociatedRoles"] = (
            aws_sdk_securityhub.types.aws_rds_db_instance_associated_roles.serialize_json(
                value["associated_roles"]
            )
        )
    if "ca_certificate_identifier" in value:
        out["CACertificateIdentifier"] = value["ca_certificate_identifier"]
    if "db_cluster_identifier" in value:
        out["DBClusterIdentifier"] = value["db_cluster_identifier"]
    if "db_instance_identifier" in value:
        out["DBInstanceIdentifier"] = value["db_instance_identifier"]
    if "db_instance_class" in value:
        out["DBInstanceClass"] = value["db_instance_class"]
    if "db_instance_port" in value:
        out["DbInstancePort"] = value["db_instance_port"]
    if "dbi_resource_id" in value:
        out["DbiResourceId"] = value["dbi_resource_id"]
    if "db_name" in value:
        out["DBName"] = value["db_name"]
    if "deletion_protection" in value:
        out["DeletionProtection"] = value["deletion_protection"]
    if "endpoint" in value:
        import aws_sdk_securityhub.types.aws_rds_db_instance_endpoint

        out["Endpoint"] = (
            aws_sdk_securityhub.types.aws_rds_db_instance_endpoint.serialize_json(
                value["endpoint"]
            )
        )
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "iam_database_authentication_enabled" in value:
        out["IAMDatabaseAuthenticationEnabled"] = value[
            "iam_database_authentication_enabled"
        ]
    if "instance_create_time" in value:
        out["InstanceCreateTime"] = value["instance_create_time"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "publicly_accessible" in value:
        out["PubliclyAccessible"] = value["publicly_accessible"]
    if "storage_encrypted" in value:
        out["StorageEncrypted"] = value["storage_encrypted"]
    if "tde_credential_arn" in value:
        out["TdeCredentialArn"] = value["tde_credential_arn"]
    if "vpc_security_groups" in value:
        import aws_sdk_securityhub.types.aws_rds_db_instance_vpc_security_groups

        out["VpcSecurityGroups"] = (
            aws_sdk_securityhub.types.aws_rds_db_instance_vpc_security_groups.serialize_json(
                value["vpc_security_groups"]
            )
        )
    if "multi_az" in value:
        out["MultiAz"] = value["multi_az"]
    if "enhanced_monitoring_resource_arn" in value:
        out["EnhancedMonitoringResourceArn"] = value["enhanced_monitoring_resource_arn"]
    if "db_instance_status" in value:
        out["DbInstanceStatus"] = value["db_instance_status"]
    if "master_username" in value:
        out["MasterUsername"] = value["master_username"]
    if "allocated_storage" in value:
        out["AllocatedStorage"] = value["allocated_storage"]
    if "preferred_backup_window" in value:
        out["PreferredBackupWindow"] = value["preferred_backup_window"]
    if "backup_retention_period" in value:
        out["BackupRetentionPeriod"] = value["backup_retention_period"]
    if "db_security_groups" in value:
        import aws_sdk_securityhub.types.string_list

        out["DbSecurityGroups"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["db_security_groups"]
        )
    if "db_parameter_groups" in value:
        import aws_sdk_securityhub.types.aws_rds_db_parameter_groups

        out["DbParameterGroups"] = (
            aws_sdk_securityhub.types.aws_rds_db_parameter_groups.serialize_json(
                value["db_parameter_groups"]
            )
        )
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "db_subnet_group" in value:
        import aws_sdk_securityhub.types.aws_rds_db_subnet_group

        out["DbSubnetGroup"] = (
            aws_sdk_securityhub.types.aws_rds_db_subnet_group.serialize_json(
                value["db_subnet_group"]
            )
        )
    if "preferred_maintenance_window" in value:
        out["PreferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "pending_modified_values" in value:
        import aws_sdk_securityhub.types.aws_rds_db_pending_modified_values

        out["PendingModifiedValues"] = (
            aws_sdk_securityhub.types.aws_rds_db_pending_modified_values.serialize_json(
                value["pending_modified_values"]
            )
        )
    if "latest_restorable_time" in value:
        out["LatestRestorableTime"] = value["latest_restorable_time"]
    if "auto_minor_version_upgrade" in value:
        out["AutoMinorVersionUpgrade"] = value["auto_minor_version_upgrade"]
    if "read_replica_source_db_instance_identifier" in value:
        out["ReadReplicaSourceDBInstanceIdentifier"] = value[
            "read_replica_source_db_instance_identifier"
        ]
    if "read_replica_db_instance_identifiers" in value:
        import aws_sdk_securityhub.types.string_list

        out["ReadReplicaDBInstanceIdentifiers"] = (
            aws_sdk_securityhub.types.string_list.serialize_json(
                value["read_replica_db_instance_identifiers"]
            )
        )
    if "read_replica_db_cluster_identifiers" in value:
        import aws_sdk_securityhub.types.string_list

        out["ReadReplicaDBClusterIdentifiers"] = (
            aws_sdk_securityhub.types.string_list.serialize_json(
                value["read_replica_db_cluster_identifiers"]
            )
        )
    if "license_model" in value:
        out["LicenseModel"] = value["license_model"]
    if "iops" in value:
        out["Iops"] = value["iops"]
    if "option_group_memberships" in value:
        import aws_sdk_securityhub.types.aws_rds_db_option_group_memberships

        out["OptionGroupMemberships"] = (
            aws_sdk_securityhub.types.aws_rds_db_option_group_memberships.serialize_json(
                value["option_group_memberships"]
            )
        )
    if "character_set_name" in value:
        out["CharacterSetName"] = value["character_set_name"]
    if "secondary_availability_zone" in value:
        out["SecondaryAvailabilityZone"] = value["secondary_availability_zone"]
    if "status_infos" in value:
        import aws_sdk_securityhub.types.aws_rds_db_status_infos

        out["StatusInfos"] = (
            aws_sdk_securityhub.types.aws_rds_db_status_infos.serialize_json(
                value["status_infos"]
            )
        )
    if "storage_type" in value:
        out["StorageType"] = value["storage_type"]
    if "domain_memberships" in value:
        import aws_sdk_securityhub.types.aws_rds_db_domain_memberships

        out["DomainMemberships"] = (
            aws_sdk_securityhub.types.aws_rds_db_domain_memberships.serialize_json(
                value["domain_memberships"]
            )
        )
    if "copy_tags_to_snapshot" in value:
        out["CopyTagsToSnapshot"] = value["copy_tags_to_snapshot"]
    if "monitoring_interval" in value:
        out["MonitoringInterval"] = value["monitoring_interval"]
    if "monitoring_role_arn" in value:
        out["MonitoringRoleArn"] = value["monitoring_role_arn"]
    if "promotion_tier" in value:
        out["PromotionTier"] = value["promotion_tier"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    if "performance_insights_enabled" in value:
        out["PerformanceInsightsEnabled"] = value["performance_insights_enabled"]
    if "performance_insights_kms_key_id" in value:
        out["PerformanceInsightsKmsKeyId"] = value["performance_insights_kms_key_id"]
    if "performance_insights_retention_period" in value:
        out["PerformanceInsightsRetentionPeriod"] = value[
            "performance_insights_retention_period"
        ]
    if "enabled_cloud_watch_logs_exports" in value:
        import aws_sdk_securityhub.types.string_list

        out["EnabledCloudWatchLogsExports"] = (
            aws_sdk_securityhub.types.string_list.serialize_json(
                value["enabled_cloud_watch_logs_exports"]
            )
        )
    if "processor_features" in value:
        import aws_sdk_securityhub.types.aws_rds_db_processor_features

        out["ProcessorFeatures"] = (
            aws_sdk_securityhub.types.aws_rds_db_processor_features.serialize_json(
                value["processor_features"]
            )
        )
    if "listener_endpoint" in value:
        import aws_sdk_securityhub.types.aws_rds_db_instance_endpoint

        out["ListenerEndpoint"] = (
            aws_sdk_securityhub.types.aws_rds_db_instance_endpoint.serialize_json(
                value["listener_endpoint"]
            )
        )
    if "max_allocated_storage" in value:
        out["MaxAllocatedStorage"] = value["max_allocated_storage"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbInstanceDetails:
    out: AwsRdsDbInstanceDetails = {}  # type: ignore[typeddict-item]
    if "AssociatedRoles" in data:
        import aws_sdk_securityhub.types.aws_rds_db_instance_associated_roles

        out["associated_roles"] = (
            aws_sdk_securityhub.types.aws_rds_db_instance_associated_roles.deserialize_json(
                data["AssociatedRoles"]
            )
        )
    if "CACertificateIdentifier" in data:
        out["ca_certificate_identifier"] = data["CACertificateIdentifier"]
    if "DBClusterIdentifier" in data:
        out["db_cluster_identifier"] = data["DBClusterIdentifier"]
    if "DBInstanceIdentifier" in data:
        out["db_instance_identifier"] = data["DBInstanceIdentifier"]
    if "DBInstanceClass" in data:
        out["db_instance_class"] = data["DBInstanceClass"]
    if "DbInstancePort" in data:
        out["db_instance_port"] = data["DbInstancePort"]
    if "DbiResourceId" in data:
        out["dbi_resource_id"] = data["DbiResourceId"]
    if "DBName" in data:
        out["db_name"] = data["DBName"]
    if "DeletionProtection" in data:
        out["deletion_protection"] = data["DeletionProtection"]
    if "Endpoint" in data:
        import aws_sdk_securityhub.types.aws_rds_db_instance_endpoint

        out["endpoint"] = (
            aws_sdk_securityhub.types.aws_rds_db_instance_endpoint.deserialize_json(
                data["Endpoint"]
            )
        )
    if "Engine" in data:
        out["engine"] = data["Engine"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "IAMDatabaseAuthenticationEnabled" in data:
        out["iam_database_authentication_enabled"] = data[
            "IAMDatabaseAuthenticationEnabled"
        ]
    if "InstanceCreateTime" in data:
        out["instance_create_time"] = data["InstanceCreateTime"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "PubliclyAccessible" in data:
        out["publicly_accessible"] = data["PubliclyAccessible"]
    if "StorageEncrypted" in data:
        out["storage_encrypted"] = data["StorageEncrypted"]
    if "TdeCredentialArn" in data:
        out["tde_credential_arn"] = data["TdeCredentialArn"]
    if "VpcSecurityGroups" in data:
        import aws_sdk_securityhub.types.aws_rds_db_instance_vpc_security_groups

        out["vpc_security_groups"] = (
            aws_sdk_securityhub.types.aws_rds_db_instance_vpc_security_groups.deserialize_json(
                data["VpcSecurityGroups"]
            )
        )
    if "MultiAz" in data:
        out["multi_az"] = data["MultiAz"]
    if "EnhancedMonitoringResourceArn" in data:
        out["enhanced_monitoring_resource_arn"] = data["EnhancedMonitoringResourceArn"]
    if "DbInstanceStatus" in data:
        out["db_instance_status"] = data["DbInstanceStatus"]
    if "MasterUsername" in data:
        out["master_username"] = data["MasterUsername"]
    if "AllocatedStorage" in data:
        out["allocated_storage"] = data["AllocatedStorage"]
    if "PreferredBackupWindow" in data:
        out["preferred_backup_window"] = data["PreferredBackupWindow"]
    if "BackupRetentionPeriod" in data:
        out["backup_retention_period"] = data["BackupRetentionPeriod"]
    if "DbSecurityGroups" in data:
        import aws_sdk_securityhub.types.string_list

        out["db_security_groups"] = (
            aws_sdk_securityhub.types.string_list.deserialize_json(
                data["DbSecurityGroups"]
            )
        )
    if "DbParameterGroups" in data:
        import aws_sdk_securityhub.types.aws_rds_db_parameter_groups

        out["db_parameter_groups"] = (
            aws_sdk_securityhub.types.aws_rds_db_parameter_groups.deserialize_json(
                data["DbParameterGroups"]
            )
        )
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "DbSubnetGroup" in data:
        import aws_sdk_securityhub.types.aws_rds_db_subnet_group

        out["db_subnet_group"] = (
            aws_sdk_securityhub.types.aws_rds_db_subnet_group.deserialize_json(
                data["DbSubnetGroup"]
            )
        )
    if "PreferredMaintenanceWindow" in data:
        out["preferred_maintenance_window"] = data["PreferredMaintenanceWindow"]
    if "PendingModifiedValues" in data:
        import aws_sdk_securityhub.types.aws_rds_db_pending_modified_values

        out["pending_modified_values"] = (
            aws_sdk_securityhub.types.aws_rds_db_pending_modified_values.deserialize_json(
                data["PendingModifiedValues"]
            )
        )
    if "LatestRestorableTime" in data:
        out["latest_restorable_time"] = data["LatestRestorableTime"]
    if "AutoMinorVersionUpgrade" in data:
        out["auto_minor_version_upgrade"] = data["AutoMinorVersionUpgrade"]
    if "ReadReplicaSourceDBInstanceIdentifier" in data:
        out["read_replica_source_db_instance_identifier"] = data[
            "ReadReplicaSourceDBInstanceIdentifier"
        ]
    if "ReadReplicaDBInstanceIdentifiers" in data:
        import aws_sdk_securityhub.types.string_list

        out["read_replica_db_instance_identifiers"] = (
            aws_sdk_securityhub.types.string_list.deserialize_json(
                data["ReadReplicaDBInstanceIdentifiers"]
            )
        )
    if "ReadReplicaDBClusterIdentifiers" in data:
        import aws_sdk_securityhub.types.string_list

        out["read_replica_db_cluster_identifiers"] = (
            aws_sdk_securityhub.types.string_list.deserialize_json(
                data["ReadReplicaDBClusterIdentifiers"]
            )
        )
    if "LicenseModel" in data:
        out["license_model"] = data["LicenseModel"]
    if "Iops" in data:
        out["iops"] = data["Iops"]
    if "OptionGroupMemberships" in data:
        import aws_sdk_securityhub.types.aws_rds_db_option_group_memberships

        out["option_group_memberships"] = (
            aws_sdk_securityhub.types.aws_rds_db_option_group_memberships.deserialize_json(
                data["OptionGroupMemberships"]
            )
        )
    if "CharacterSetName" in data:
        out["character_set_name"] = data["CharacterSetName"]
    if "SecondaryAvailabilityZone" in data:
        out["secondary_availability_zone"] = data["SecondaryAvailabilityZone"]
    if "StatusInfos" in data:
        import aws_sdk_securityhub.types.aws_rds_db_status_infos

        out["status_infos"] = (
            aws_sdk_securityhub.types.aws_rds_db_status_infos.deserialize_json(
                data["StatusInfos"]
            )
        )
    if "StorageType" in data:
        out["storage_type"] = data["StorageType"]
    if "DomainMemberships" in data:
        import aws_sdk_securityhub.types.aws_rds_db_domain_memberships

        out["domain_memberships"] = (
            aws_sdk_securityhub.types.aws_rds_db_domain_memberships.deserialize_json(
                data["DomainMemberships"]
            )
        )
    if "CopyTagsToSnapshot" in data:
        out["copy_tags_to_snapshot"] = data["CopyTagsToSnapshot"]
    if "MonitoringInterval" in data:
        out["monitoring_interval"] = data["MonitoringInterval"]
    if "MonitoringRoleArn" in data:
        out["monitoring_role_arn"] = data["MonitoringRoleArn"]
    if "PromotionTier" in data:
        out["promotion_tier"] = data["PromotionTier"]
    if "Timezone" in data:
        out["timezone"] = data["Timezone"]
    if "PerformanceInsightsEnabled" in data:
        out["performance_insights_enabled"] = data["PerformanceInsightsEnabled"]
    if "PerformanceInsightsKmsKeyId" in data:
        out["performance_insights_kms_key_id"] = data["PerformanceInsightsKmsKeyId"]
    if "PerformanceInsightsRetentionPeriod" in data:
        out["performance_insights_retention_period"] = data[
            "PerformanceInsightsRetentionPeriod"
        ]
    if "EnabledCloudWatchLogsExports" in data:
        import aws_sdk_securityhub.types.string_list

        out["enabled_cloud_watch_logs_exports"] = (
            aws_sdk_securityhub.types.string_list.deserialize_json(
                data["EnabledCloudWatchLogsExports"]
            )
        )
    if "ProcessorFeatures" in data:
        import aws_sdk_securityhub.types.aws_rds_db_processor_features

        out["processor_features"] = (
            aws_sdk_securityhub.types.aws_rds_db_processor_features.deserialize_json(
                data["ProcessorFeatures"]
            )
        )
    if "ListenerEndpoint" in data:
        import aws_sdk_securityhub.types.aws_rds_db_instance_endpoint

        out["listener_endpoint"] = (
            aws_sdk_securityhub.types.aws_rds_db_instance_endpoint.deserialize_json(
                data["ListenerEndpoint"]
            )
        )
    if "MaxAllocatedStorage" in data:
        out["max_allocated_storage"] = data["MaxAllocatedStorage"]
    return out
