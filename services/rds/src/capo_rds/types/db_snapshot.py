"""Generated from Smithy shape ``com.amazonaws.rds#DBSnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.additional_storage_volumes_list
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.integer
    import capo_rds.types.integer_optional
    import capo_rds.types.processor_feature_list
    import capo_rds.types.storage_encryption_type
    import capo_rds.types.string
    import capo_rds.types.t_stamp
    import capo_rds.types.tag_list


class DBSnapshot(TypedDict, closed=True):
    db_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the identifier for the DB snapshot.</p>"""
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the DB instance identifier of the DB instance this DB snapshot was created from.</p>"""
    snapshot_create_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>Specifies when the snapshot was taken in Coordinated Universal Time (UTC). Changes for the copy when the snapshot is copied.</p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the name of the database engine.</p>"""
    allocated_storage: NotRequired["capo_rds.types.integer.Integer"]
    """<p>Specifies the allocated storage size in gibibytes (GiB).</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the status of this DB snapshot.</p>"""
    port: NotRequired["capo_rds.types.integer.Integer"]
    """<p>Specifies the port that the database engine was listening on at the time of the snapshot.</p>"""
    availability_zone: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.</p>"""
    vpc_id: NotRequired["capo_rds.types.string.String"]
    """<p>Provides the VPC ID associated with the DB snapshot.</p>"""
    instance_create_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>Specifies the time in Coordinated Universal Time (UTC) when the DB instance, from which the snapshot was taken, was created.</p>"""
    master_username: NotRequired["capo_rds.types.string.String"]
    """<p>Provides the master username for the DB snapshot.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the version of the database engine.</p>"""
    license_model: NotRequired["capo_rds.types.string.String"]
    """<p>License model information for the restored DB instance.</p>"""
    snapshot_type: NotRequired["capo_rds.types.string.String"]
    """<p>Provides the type of the DB snapshot.</p>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.</p>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>Specifies the storage throughput for the DB snapshot.</p>"""
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>Provides the option group name for the DB snapshot.</p>"""
    percent_progress: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The percentage of the estimated data that has been transferred.</p>"""
    source_region: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services Region that the DB snapshot was created in or copied from.</p>"""
    source_db_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB snapshot Amazon Resource Name (ARN) that the DB snapshot was copied from. It only has a value in the case of a cross-account or cross-Region copy.</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the storage type associated with DB snapshot.</p>"""
    tde_credential_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN from the key store with which to associate the instance for TDE encryption.</p>"""
    encrypted: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the DB snapshot is encrypted.</p>"""
    storage_encryption_type: NotRequired[
        "capo_rds.types.storage_encryption_type.StorageEncryptionType"
    ]
    """<p>The type of encryption used to protect data at rest in the DB snapshot. Possible values:</p> <ul> <li> <p> <code>none</code> - The DB snapshot is not encrypted.</p> </li> <li> <p> <code>sse-rds</code> - The DB snapshot is encrypted using an Amazon Web Services owned KMS key.</p> </li> <li> <p> <code>sse-kms</code> - The DB snapshot is encrypted using a customer managed KMS key or Amazon Web Services managed KMS key.</p> </li> </ul>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automatic DB snapshots are retained.</p>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>BackupRetentionPeriod</code>.</p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>If <code>Encrypted</code> is true, the Amazon Web Services KMS key identifier for the encrypted DB snapshot.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p>"""
    db_snapshot_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the DB snapshot.</p>"""
    timezone: NotRequired["capo_rds.types.string.String"]
    """<p>The time zone of the DB snapshot. In most cases, the <code>Timezone</code> element is empty. <code>Timezone</code> content appears only for snapshots taken from Microsoft SQL Server DB instances that were created with a time zone specified.</p>"""
    iam_database_authentication_enabled: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts is enabled.</p>"""
    processor_features: NotRequired[
        "capo_rds.types.processor_feature_list.ProcessorFeatureList"
    ]
    """<p>The number of CPU cores and the number of threads per core for the DB instance class of the DB instance when the DB snapshot was created.</p>"""
    dbi_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the source DB instance, which can't be changed and which is unique to an Amazon Web Services Region.</p>"""
    tag_list: NotRequired["capo_rds.types.tag_list.TagList"]
    snapshot_target: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies where manual snapshots are stored: Dedicated Local Zones, Amazon Web Services Outposts or the Amazon Web Services Region.</p>"""
    original_snapshot_create_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>Specifies the time of the CreateDBSnapshot operation in Coordinated Universal Time (UTC). Doesn't change when the snapshot is copied.</p>"""
    snapshot_database_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The timestamp of the most recent transaction applied to the database that you're backing up. Thus, if you restore a snapshot, SnapshotDatabaseTime is the most recent transaction in the restored DB instance. In contrast, originalSnapshotCreateTime specifies the system time that the snapshot completed.</p> <p>If you back up a read replica, you can determine the replica lag by comparing SnapshotDatabaseTime with originalSnapshotCreateTime. For example, if originalSnapshotCreateTime is two hours later than SnapshotDatabaseTime, then the replica lag is two hours.</p>"""
    db_system_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Oracle system identifier (SID), which is the name of the Oracle database instance that manages your database files. The Oracle SID is also the name of your CDB.</p>"""
    multi_tenant: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the snapshot is of a DB instance using the multi-tenant configuration (TRUE) or the single-tenant configuration (FALSE).</p>"""
    dedicated_log_volume: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the DB instance has a dedicated log volume (DLV) enabled.</p>"""
    additional_storage_volumes: NotRequired[
        "capo_rds.types.additional_storage_volumes_list.AdditionalStorageVolumesList"
    ]
    """<p>The additional storage volumes associated with the DB snapshot. RDS supports additional storage volumes for RDS for Oracle and RDS for SQL Server.</p>"""
    snapshot_availability_zone: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the name of the Availability Zone where RDS stores the DB snapshot. This value is valid only for snapshots that RDS stores on a Dedicated Local Zone.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSnapshot, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_snapshot_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBSnapshotIdentifier", str(value["db_snapshot_identifier"]))
        )
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "snapshot_create_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["snapshot_create_time"], pairs, f"{key_prefix}SnapshotCreateTime"
        )
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "instance_create_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["instance_create_time"], pairs, f"{key_prefix}InstanceCreateTime"
        )
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "snapshot_type" in value:
        pairs.append((f"{key_prefix}SnapshotType", str(value["snapshot_type"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "storage_throughput" in value:
        pairs.append(
            (f"{key_prefix}StorageThroughput", str(value["storage_throughput"]))
        )
    if "option_group_name" in value:
        pairs.append((f"{key_prefix}OptionGroupName", str(value["option_group_name"])))
    if "percent_progress" in value:
        pairs.append((f"{key_prefix}PercentProgress", str(value["percent_progress"])))
    if "source_region" in value:
        pairs.append((f"{key_prefix}SourceRegion", str(value["source_region"])))
    if "source_db_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDBSnapshotIdentifier",
                str(value["source_db_snapshot_identifier"]),
            )
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "tde_credential_arn" in value:
        pairs.append(
            (f"{key_prefix}TdeCredentialArn", str(value["tde_credential_arn"]))
        )
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "storage_encryption_type" in value:
        import capo_rds.types.storage_encryption_type

        capo_rds.types.storage_encryption_type.serialize_query(
            value["storage_encryption_type"],
            pairs,
            f"{key_prefix}StorageEncryptionType",
        )
    if "backup_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}BackupRetentionPeriod",
                str(value["backup_retention_period"]),
            )
        )
    if "preferred_backup_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredBackupWindow",
                str(value["preferred_backup_window"]),
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "db_snapshot_arn" in value:
        pairs.append((f"{key_prefix}DBSnapshotArn", str(value["db_snapshot_arn"])))
    if "timezone" in value:
        pairs.append((f"{key_prefix}Timezone", str(value["timezone"])))
    if "iam_database_authentication_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}IAMDatabaseAuthenticationEnabled",
                "true" if value["iam_database_authentication_enabled"] else "false",
            )
        )
    if "processor_features" in value:
        import capo_rds.types.processor_feature_list

        capo_rds.types.processor_feature_list.serialize_query(
            value["processor_features"], pairs, f"{key_prefix}ProcessorFeatures"
        )
    if "dbi_resource_id" in value:
        pairs.append((f"{key_prefix}DbiResourceId", str(value["dbi_resource_id"])))
    if "tag_list" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{key_prefix}TagList"
        )
    if "snapshot_target" in value:
        pairs.append((f"{key_prefix}SnapshotTarget", str(value["snapshot_target"])))
    if "original_snapshot_create_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["original_snapshot_create_time"],
            pairs,
            f"{key_prefix}OriginalSnapshotCreateTime",
        )
    if "snapshot_database_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["snapshot_database_time"], pairs, f"{key_prefix}SnapshotDatabaseTime"
        )
    if "db_system_id" in value:
        pairs.append((f"{key_prefix}DBSystemId", str(value["db_system_id"])))
    if "multi_tenant" in value:
        pairs.append(
            (f"{key_prefix}MultiTenant", "true" if value["multi_tenant"] else "false")
        )
    if "dedicated_log_volume" in value:
        pairs.append(
            (
                f"{key_prefix}DedicatedLogVolume",
                "true" if value["dedicated_log_volume"] else "false",
            )
        )
    if "additional_storage_volumes" in value:
        import capo_rds.types.additional_storage_volumes_list

        capo_rds.types.additional_storage_volumes_list.serialize_query(
            value["additional_storage_volumes"],
            pairs,
            f"{key_prefix}AdditionalStorageVolumes",
        )
    if "snapshot_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshotAvailabilityZone",
                str(value["snapshot_availability_zone"]),
            )
        )


def deserialize_query(el: Element) -> DBSnapshot:
    out: DBSnapshot = {}  # type: ignore[typeddict-item]
    child_db_snapshot_identifier = el.find("DBSnapshotIdentifier")
    if child_db_snapshot_identifier is not None:
        out["db_snapshot_identifier"] = str(child_db_snapshot_identifier.text or "")
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_snapshot_create_time = el.find("SnapshotCreateTime")
    if child_snapshot_create_time is not None:
        import capo_rds.types.t_stamp

        out["snapshot_create_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_snapshot_create_time
        )
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_instance_create_time = el.find("InstanceCreateTime")
    if child_instance_create_time is not None:
        import capo_rds.types.t_stamp

        out["instance_create_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_instance_create_time
        )
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_snapshot_type = el.find("SnapshotType")
    if child_snapshot_type is not None:
        out["snapshot_type"] = str(child_snapshot_type.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_storage_throughput = el.find("StorageThroughput")
    if child_storage_throughput is not None:
        out["storage_throughput"] = int(child_storage_throughput.text or "")
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    child_percent_progress = el.find("PercentProgress")
    if child_percent_progress is not None:
        out["percent_progress"] = int(child_percent_progress.text or "")
    child_source_region = el.find("SourceRegion")
    if child_source_region is not None:
        out["source_region"] = str(child_source_region.text or "")
    child_source_db_snapshot_identifier = el.find("SourceDBSnapshotIdentifier")
    if child_source_db_snapshot_identifier is not None:
        out["source_db_snapshot_identifier"] = str(
            child_source_db_snapshot_identifier.text or ""
        )
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_tde_credential_arn = el.find("TdeCredentialArn")
    if child_tde_credential_arn is not None:
        out["tde_credential_arn"] = str(child_tde_credential_arn.text or "")
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_storage_encryption_type = el.find("StorageEncryptionType")
    if child_storage_encryption_type is not None:
        import capo_rds.types.storage_encryption_type

        out["storage_encryption_type"] = (
            capo_rds.types.storage_encryption_type.deserialize_query(
                child_storage_encryption_type
            )
        )
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_db_snapshot_arn = el.find("DBSnapshotArn")
    if child_db_snapshot_arn is not None:
        out["db_snapshot_arn"] = str(child_db_snapshot_arn.text or "")
    child_timezone = el.find("Timezone")
    if child_timezone is not None:
        out["timezone"] = str(child_timezone.text or "")
    child_iam_database_authentication_enabled = el.find(
        "IAMDatabaseAuthenticationEnabled"
    )
    if child_iam_database_authentication_enabled is not None:
        out["iam_database_authentication_enabled"] = (
            child_iam_database_authentication_enabled.text or ""
        ).lower() == "true"
    child_processor_features = el.find("ProcessorFeatures")
    if child_processor_features is not None:
        import capo_rds.types.processor_feature_list

        out["processor_features"] = (
            capo_rds.types.processor_feature_list.deserialize_query(
                child_processor_features
            )
        )
    child_dbi_resource_id = el.find("DbiResourceId")
    if child_dbi_resource_id is not None:
        out["dbi_resource_id"] = str(child_dbi_resource_id.text or "")
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_rds.types.tag_list

        out["tag_list"] = capo_rds.types.tag_list.deserialize_query(child_tag_list)
    child_snapshot_target = el.find("SnapshotTarget")
    if child_snapshot_target is not None:
        out["snapshot_target"] = str(child_snapshot_target.text or "")
    child_original_snapshot_create_time = el.find("OriginalSnapshotCreateTime")
    if child_original_snapshot_create_time is not None:
        import capo_rds.types.t_stamp

        out["original_snapshot_create_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_original_snapshot_create_time
        )
    child_snapshot_database_time = el.find("SnapshotDatabaseTime")
    if child_snapshot_database_time is not None:
        import capo_rds.types.t_stamp

        out["snapshot_database_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_snapshot_database_time
        )
    child_db_system_id = el.find("DBSystemId")
    if child_db_system_id is not None:
        out["db_system_id"] = str(child_db_system_id.text or "")
    child_multi_tenant = el.find("MultiTenant")
    if child_multi_tenant is not None:
        out["multi_tenant"] = (child_multi_tenant.text or "").lower() == "true"
    child_dedicated_log_volume = el.find("DedicatedLogVolume")
    if child_dedicated_log_volume is not None:
        out["dedicated_log_volume"] = (
            child_dedicated_log_volume.text or ""
        ).lower() == "true"
    child_additional_storage_volumes = el.find("AdditionalStorageVolumes")
    if child_additional_storage_volumes is not None:
        import capo_rds.types.additional_storage_volumes_list

        out["additional_storage_volumes"] = (
            capo_rds.types.additional_storage_volumes_list.deserialize_query(
                child_additional_storage_volumes
            )
        )
    child_snapshot_availability_zone = el.find("SnapshotAvailabilityZone")
    if child_snapshot_availability_zone is not None:
        out["snapshot_availability_zone"] = str(
            child_snapshot_availability_zone.text or ""
        )
    return out
