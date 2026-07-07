"""Generated from Smithy shape ``com.amazonaws.docdb#DBInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.boolean
    import aws_sdk_docdb.types.boolean_optional
    import aws_sdk_docdb.types.certificate_details
    import aws_sdk_docdb.types.db_instance_status_info_list
    import aws_sdk_docdb.types.db_subnet_group
    import aws_sdk_docdb.types.endpoint
    import aws_sdk_docdb.types.integer
    import aws_sdk_docdb.types.integer_optional
    import aws_sdk_docdb.types.log_type_list
    import aws_sdk_docdb.types.pending_modified_values
    import aws_sdk_docdb.types.string
    import aws_sdk_docdb.types.t_stamp
    import aws_sdk_docdb.types.vpc_security_group_membership_list


class DBInstance(TypedDict, closed=True):
    db_instance_identifier: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>Contains a user-provided database identifier. This identifier is the unique key that identifies an instance.</p>"""
    db_instance_class: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>Contains the name of the compute and memory capacity class of the instance.</p>"""
    engine: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>Provides the name of the database engine to be used for this instance.</p>"""
    db_instance_status: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>Specifies the current state of this database.</p>"""
    endpoint: NotRequired["aws_sdk_docdb.types.endpoint.Endpoint"]
    """<p>Specifies the connection endpoint.</p>"""
    instance_create_time: NotRequired["aws_sdk_docdb.types.t_stamp.TStamp"]
    """<p>Provides the date and time that the instance was created.</p>"""
    preferred_backup_window: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p> Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>BackupRetentionPeriod</code>. </p>"""
    backup_retention_period: NotRequired["aws_sdk_docdb.types.integer.Integer"]
    """<p>Specifies the number of days for which automatic snapshots are retained.</p>"""
    vpc_security_groups: NotRequired[
        "aws_sdk_docdb.types.vpc_security_group_membership_list.VpcSecurityGroupMembershipList"
    ]
    """<p>Provides a list of VPC security group elements that the instance belongs to.</p>"""
    availability_zone: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>Specifies the name of the Availability Zone that the instance is located in.</p>"""
    db_subnet_group: NotRequired["aws_sdk_docdb.types.db_subnet_group.DBSubnetGroup"]
    """<p>Specifies information on the subnet group that is associated with the instance, including the name, description, and subnets in the subnet group.</p>"""
    preferred_maintenance_window: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p>"""
    pending_modified_values: NotRequired[
        "aws_sdk_docdb.types.pending_modified_values.PendingModifiedValues"
    ]
    """<p>Specifies that changes to the instance are pending. This element is included only when changes are pending. Specific changes are identified by subelements.</p>"""
    latest_restorable_time: NotRequired["aws_sdk_docdb.types.t_stamp.TStamp"]
    """<p>Specifies the latest time to which a database can be restored with point-in-time restore.</p>"""
    engine_version: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>Indicates the database engine version.</p>"""
    auto_minor_version_upgrade: NotRequired["aws_sdk_docdb.types.boolean.Boolean"]
    """<p>Does not apply. This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.</p>"""
    publicly_accessible: NotRequired["aws_sdk_docdb.types.boolean.Boolean"]
    """<p>Not supported. Amazon DocumentDB does not currently support public endpoints. The value of <code>PubliclyAccessible</code> is always <code>false</code>.</p>"""
    status_infos: NotRequired[
        "aws_sdk_docdb.types.db_instance_status_info_list.DBInstanceStatusInfoList"
    ]
    """<p>The status of a read replica. If the instance is not a read replica, this is blank.</p>"""
    db_cluster_identifier: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>Contains the name of the cluster that the instance is a member of if the instance is a member of a cluster.</p>"""
    storage_encrypted: NotRequired["aws_sdk_docdb.types.boolean.Boolean"]
    """<p>Specifies whether or not the instance is encrypted.</p>"""
    kms_key_id: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p> If <code>StorageEncrypted</code> is <code>true</code>, the KMS key identifier for the encrypted instance. </p>"""
    dbi_resource_id: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The Amazon Web Services Region-unique, immutable identifier for the instance. This identifier is found in CloudTrail log entries whenever the KMS key for the instance is accessed.</p>"""
    ca_certificate_identifier: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The identifier of the CA certificate for this DB instance.</p>"""
    copy_tags_to_snapshot: NotRequired[
        "aws_sdk_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.</p>"""
    promotion_tier: NotRequired["aws_sdk_docdb.types.integer_optional.IntegerOptional"]
    """<p>A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.</p>"""
    db_instance_arn: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the instance.</p>"""
    enabled_cloudwatch_logs_exports: NotRequired[
        "aws_sdk_docdb.types.log_type_list.LogTypeList"
    ]
    """<p>A list of log types that this instance is configured to export to CloudWatch Logs.</p>"""
    certificate_details: NotRequired[
        "aws_sdk_docdb.types.certificate_details.CertificateDetails"
    ]
    """<p>The details of the DB instance's server certificate.</p>"""
    performance_insights_enabled: NotRequired[
        "aws_sdk_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set to <code>true</code> if Amazon RDS Performance Insights is enabled for the DB instance, and otherwise <code>false</code>.</p>"""
    performance_insights_kms_key_id: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{prefix}.DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "db_instance_class" in value:
        pairs.append((f"{prefix}.DBInstanceClass", str(value["db_instance_class"])))
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "db_instance_status" in value:
        pairs.append((f"{prefix}.DBInstanceStatus", str(value["db_instance_status"])))
    if "endpoint" in value:
        import aws_sdk_docdb.types.endpoint

        aws_sdk_docdb.types.endpoint.serialize_query(
            value["endpoint"], pairs, f"{prefix}.Endpoint"
        )
    if "instance_create_time" in value:
        import aws_sdk_docdb.types.t_stamp

        aws_sdk_docdb.types.t_stamp.serialize_query(
            value["instance_create_time"], pairs, f"{prefix}.InstanceCreateTime"
        )
    if "preferred_backup_window" in value:
        pairs.append(
            (f"{prefix}.PreferredBackupWindow", str(value["preferred_backup_window"]))
        )
    if "backup_retention_period" in value:
        pairs.append(
            (f"{prefix}.BackupRetentionPeriod", str(value["backup_retention_period"]))
        )
    if "vpc_security_groups" in value:
        import aws_sdk_docdb.types.vpc_security_group_membership_list

        aws_sdk_docdb.types.vpc_security_group_membership_list.serialize_query(
            value["vpc_security_groups"], pairs, f"{prefix}.VpcSecurityGroups"
        )
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "db_subnet_group" in value:
        import aws_sdk_docdb.types.db_subnet_group

        aws_sdk_docdb.types.db_subnet_group.serialize_query(
            value["db_subnet_group"], pairs, f"{prefix}.DBSubnetGroup"
        )
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{prefix}.PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
        )
    if "pending_modified_values" in value:
        import aws_sdk_docdb.types.pending_modified_values

        aws_sdk_docdb.types.pending_modified_values.serialize_query(
            value["pending_modified_values"], pairs, f"{prefix}.PendingModifiedValues"
        )
    if "latest_restorable_time" in value:
        import aws_sdk_docdb.types.t_stamp

        aws_sdk_docdb.types.t_stamp.serialize_query(
            value["latest_restorable_time"], pairs, f"{prefix}.LatestRestorableTime"
        )
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "auto_minor_version_upgrade" in value:
        pairs.append(
            (
                f"{prefix}.AutoMinorVersionUpgrade",
                "true" if value["auto_minor_version_upgrade"] else "false",
            )
        )
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{prefix}.PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
            )
        )
    if "status_infos" in value:
        import aws_sdk_docdb.types.db_instance_status_info_list

        aws_sdk_docdb.types.db_instance_status_info_list.serialize_query(
            value["status_infos"], pairs, f"{prefix}.StatusInfos"
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "storage_encrypted" in value:
        pairs.append(
            (
                f"{prefix}.StorageEncrypted",
                "true" if value["storage_encrypted"] else "false",
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "dbi_resource_id" in value:
        pairs.append((f"{prefix}.DbiResourceId", str(value["dbi_resource_id"])))
    if "ca_certificate_identifier" in value:
        pairs.append(
            (
                f"{prefix}.CACertificateIdentifier",
                str(value["ca_certificate_identifier"]),
            )
        )
    if "copy_tags_to_snapshot" in value:
        pairs.append(
            (
                f"{prefix}.CopyTagsToSnapshot",
                "true" if value["copy_tags_to_snapshot"] else "false",
            )
        )
    if "promotion_tier" in value:
        pairs.append((f"{prefix}.PromotionTier", str(value["promotion_tier"])))
    if "db_instance_arn" in value:
        pairs.append((f"{prefix}.DBInstanceArn", str(value["db_instance_arn"])))
    if "enabled_cloudwatch_logs_exports" in value:
        import aws_sdk_docdb.types.log_type_list

        aws_sdk_docdb.types.log_type_list.serialize_query(
            value["enabled_cloudwatch_logs_exports"],
            pairs,
            f"{prefix}.EnabledCloudwatchLogsExports",
        )
    if "certificate_details" in value:
        import aws_sdk_docdb.types.certificate_details

        aws_sdk_docdb.types.certificate_details.serialize_query(
            value["certificate_details"], pairs, f"{prefix}.CertificateDetails"
        )
    if "performance_insights_enabled" in value:
        pairs.append(
            (
                f"{prefix}.PerformanceInsightsEnabled",
                "true" if value["performance_insights_enabled"] else "false",
            )
        )
    if "performance_insights_kms_key_id" in value:
        pairs.append(
            (
                f"{prefix}.PerformanceInsightsKMSKeyId",
                str(value["performance_insights_kms_key_id"]),
            )
        )


def deserialize_query(el: Element) -> DBInstance:
    out: DBInstance = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_db_instance_status = el.find("DBInstanceStatus")
    if child_db_instance_status is not None:
        out["db_instance_status"] = str(child_db_instance_status.text or "")
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        import aws_sdk_docdb.types.endpoint

        out["endpoint"] = aws_sdk_docdb.types.endpoint.deserialize_query(child_endpoint)
    child_instance_create_time = el.find("InstanceCreateTime")
    if child_instance_create_time is not None:
        import aws_sdk_docdb.types.t_stamp

        out["instance_create_time"] = aws_sdk_docdb.types.t_stamp.deserialize_query(
            child_instance_create_time
        )
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_vpc_security_groups = el.find("VpcSecurityGroups")
    if child_vpc_security_groups is not None:
        import aws_sdk_docdb.types.vpc_security_group_membership_list

        out["vpc_security_groups"] = (
            aws_sdk_docdb.types.vpc_security_group_membership_list.deserialize_query(
                child_vpc_security_groups
            )
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_db_subnet_group = el.find("DBSubnetGroup")
    if child_db_subnet_group is not None:
        import aws_sdk_docdb.types.db_subnet_group

        out["db_subnet_group"] = aws_sdk_docdb.types.db_subnet_group.deserialize_query(
            child_db_subnet_group
        )
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
    child_pending_modified_values = el.find("PendingModifiedValues")
    if child_pending_modified_values is not None:
        import aws_sdk_docdb.types.pending_modified_values

        out["pending_modified_values"] = (
            aws_sdk_docdb.types.pending_modified_values.deserialize_query(
                child_pending_modified_values
            )
        )
    child_latest_restorable_time = el.find("LatestRestorableTime")
    if child_latest_restorable_time is not None:
        import aws_sdk_docdb.types.t_stamp

        out["latest_restorable_time"] = aws_sdk_docdb.types.t_stamp.deserialize_query(
            child_latest_restorable_time
        )
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_auto_minor_version_upgrade = el.find("AutoMinorVersionUpgrade")
    if child_auto_minor_version_upgrade is not None:
        out["auto_minor_version_upgrade"] = (
            child_auto_minor_version_upgrade.text or ""
        ).lower() == "true"
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_status_infos = el.find("StatusInfos")
    if child_status_infos is not None:
        import aws_sdk_docdb.types.db_instance_status_info_list

        out["status_infos"] = (
            aws_sdk_docdb.types.db_instance_status_info_list.deserialize_query(
                child_status_infos
            )
        )
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_dbi_resource_id = el.find("DbiResourceId")
    if child_dbi_resource_id is not None:
        out["dbi_resource_id"] = str(child_dbi_resource_id.text or "")
    child_ca_certificate_identifier = el.find("CACertificateIdentifier")
    if child_ca_certificate_identifier is not None:
        out["ca_certificate_identifier"] = str(
            child_ca_certificate_identifier.text or ""
        )
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    child_promotion_tier = el.find("PromotionTier")
    if child_promotion_tier is not None:
        out["promotion_tier"] = int(child_promotion_tier.text or "")
    child_db_instance_arn = el.find("DBInstanceArn")
    if child_db_instance_arn is not None:
        out["db_instance_arn"] = str(child_db_instance_arn.text or "")
    child_enabled_cloudwatch_logs_exports = el.find("EnabledCloudwatchLogsExports")
    if child_enabled_cloudwatch_logs_exports is not None:
        import aws_sdk_docdb.types.log_type_list

        out["enabled_cloudwatch_logs_exports"] = (
            aws_sdk_docdb.types.log_type_list.deserialize_query(
                child_enabled_cloudwatch_logs_exports
            )
        )
    child_certificate_details = el.find("CertificateDetails")
    if child_certificate_details is not None:
        import aws_sdk_docdb.types.certificate_details

        out["certificate_details"] = (
            aws_sdk_docdb.types.certificate_details.deserialize_query(
                child_certificate_details
            )
        )
    child_performance_insights_enabled = el.find("PerformanceInsightsEnabled")
    if child_performance_insights_enabled is not None:
        out["performance_insights_enabled"] = (
            child_performance_insights_enabled.text or ""
        ).lower() == "true"
    child_performance_insights_kms_key_id = el.find("PerformanceInsightsKMSKeyId")
    if child_performance_insights_kms_key_id is not None:
        out["performance_insights_kms_key_id"] = str(
            child_performance_insights_kms_key_id.text or ""
        )
    return out
