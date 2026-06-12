"""Generated from Smithy shape ``com.amazonaws.fsx#CreateFileSystemLustreConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.archive_path
    import aws_sdk_fsx.types.auto_import_policy_type
    import aws_sdk_fsx.types.automatic_backup_retention_days
    import aws_sdk_fsx.types.create_file_system_lustre_metadata_configuration
    import aws_sdk_fsx.types.daily_time
    import aws_sdk_fsx.types.data_compression_type
    import aws_sdk_fsx.types.drive_cache_type
    import aws_sdk_fsx.types.flag
    import aws_sdk_fsx.types.lustre_deployment_type
    import aws_sdk_fsx.types.lustre_log_create_configuration
    import aws_sdk_fsx.types.lustre_read_cache_configuration
    import aws_sdk_fsx.types.lustre_root_squash_configuration
    import aws_sdk_fsx.types.megabytes
    import aws_sdk_fsx.types.per_unit_storage_throughput
    import aws_sdk_fsx.types.throughput_capacity_mbps
    import aws_sdk_fsx.types.weekly_time


class CreateFileSystemLustreConfiguration(TypedDict):
    weekly_maintenance_start_time: NotRequired[
        "aws_sdk_fsx.types.weekly_time.WeeklyTime"
    ]
    """<p>(Optional) The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.</p>"""
    import_path: NotRequired["aws_sdk_fsx.types.archive_path.ArchivePath"]
    """<p>(Optional) The path to the Amazon S3 bucket (including the optional prefix) that you're using as the data repository for your Amazon FSx for Lustre file system. The root of your FSx for Lustre file system will be mapped to the root of the Amazon S3 bucket you select. An example is <code>s3://import-bucket/optional-prefix</code>. If you specify a prefix after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.</p> <note> <p>This parameter is not supported for file systems with a data repository association.</p> </note>"""
    export_path: NotRequired["aws_sdk_fsx.types.archive_path.ArchivePath"]
    """<p>(Optional) Specifies the path in the Amazon S3 bucket where the root of your Amazon FSx file system is exported. The path must use the same Amazon S3 bucket as specified in ImportPath. You can provide an optional prefix to which new and changed data is to be exported from your Amazon FSx for Lustre file system. If an <code>ExportPath</code> value is not provided, Amazon FSx sets a default export path, <code>s3://import-bucket/FSxLustre[creation-timestamp]</code>. The timestamp is in UTC format, for example <code>s3://import-bucket/FSxLustre20181105T222312Z</code>.</p> <p>The Amazon S3 export bucket must be the same as the import bucket specified by <code>ImportPath</code>. If you specify only a bucket name, such as <code>s3://import-bucket</code>, you get a 1:1 mapping of file system objects to S3 bucket objects. This mapping means that the input data in S3 is overwritten on export. If you provide a custom prefix in the export path, such as <code>s3://import-bucket/[custom-optional-prefix]</code>, Amazon FSx exports the contents of your file system to that export prefix in the Amazon S3 bucket.</p> <note> <p>This parameter is not supported for file systems with a data repository association.</p> </note>"""
    imported_file_chunk_size: NotRequired["aws_sdk_fsx.types.megabytes.Megabytes"]
    """<p>(Optional) For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.</p> <p>The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.</p> <note> <p>This parameter is not supported for file systems with a data repository association.</p> </note>"""
    deployment_type: NotRequired[
        "aws_sdk_fsx.types.lustre_deployment_type.LustreDeploymentType"
    ]
    """<p>(Optional) Choose <code>SCRATCH_1</code> and <code>SCRATCH_2</code> deployment types when you need temporary storage and shorter-term processing of data. The <code>SCRATCH_2</code> deployment type provides in-transit encryption of data and higher burst throughput capacity than <code>SCRATCH_1</code>.</p> <p>Choose <code>PERSISTENT_1</code> for longer-term storage and for throughput-focused workloads that aren’t latency-sensitive. <code>PERSISTENT_1</code> supports encryption of data in transit, and is available in all Amazon Web Services Regions in which FSx for Lustre is available.</p> <p>Choose <code>PERSISTENT_2</code> for longer-term storage and for latency-sensitive workloads that require the highest levels of IOPS/throughput. <code>PERSISTENT_2</code> supports the SSD and Intelligent-Tiering storage classes. You can optionally specify a metadata configuration mode for <code>PERSISTENT_2</code> which supports increasing metadata performance. <code>PERSISTENT_2</code> is available in a limited number of Amazon Web Services Regions. For more information, and an up-to-date list of Amazon Web Services Regions in which <code>PERSISTENT_2</code> is available, see <a href=\"https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-fsx-lustre.html\">Deployment and storage class options for FSx for Lustre file systems</a> in the <i>Amazon FSx for Lustre User Guide</i>.</p> <note> <p>If you choose <code>PERSISTENT_2</code>, and you set <code>FileSystemTypeVersion</code> to <code>2.10</code>, the <code>CreateFileSystem</code> operation fails.</p> </note> <p>Encryption of data in transit is automatically turned on when you access <code>SCRATCH_2</code>, <code>PERSISTENT_1</code>, and <code>PERSISTENT_2</code> file systems from Amazon EC2 instances that support automatic encryption in the Amazon Web Services Regions where they are available. For more information about encryption in transit for FSx for Lustre file systems, see <a href=\"https://docs.aws.amazon.com/fsx/latest/LustreGuide/encryption-in-transit-fsxl.html\">Encrypting data in transit</a> in the <i>Amazon FSx for Lustre User Guide</i>.</p> <p>(Default = <code>SCRATCH_1</code>)</p>"""
    auto_import_policy: NotRequired[
        "aws_sdk_fsx.types.auto_import_policy_type.AutoImportPolicyType"
    ]
    """<p> (Optional) When you create your file system, your existing S3 objects appear as file and directory listings. Use this parameter to choose how Amazon FSx keeps your file and directory listings up to date as you add or modify objects in your linked S3 bucket. <code>AutoImportPolicy</code> can have the following values:</p> <ul> <li> <p> <code>NONE</code> - (Default) AutoImport is off. Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update file and directory listings for any new or changed objects after choosing this option.</p> </li> <li> <p> <code>NEW</code> - AutoImport is on. Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system. </p> </li> <li> <p> <code>NEW_CHANGED</code> - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option.</p> </li> <li> <p> <code>NEW_CHANGED_DELETED</code> - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/LustreGuide/older-deployment-types.html#legacy-auto-import-from-s3\"> Automatically import updates from your S3 bucket</a>.</p> <note> <p>This parameter is not supported for file systems with a data repository association.</p> </note>"""
    per_unit_storage_throughput: NotRequired[
        "aws_sdk_fsx.types.per_unit_storage_throughput.PerUnitStorageThroughput"
    ]
    """<p>Required with <code>PERSISTENT_1</code> and <code>PERSISTENT_2</code> deployment types using an SSD or HDD storage class, provisions the amount of read and write throughput for each 1 tebibyte (TiB) of file system storage capacity, in MB/s/TiB. File system throughput capacity is calculated by multiplying ﬁle system storage capacity (TiB) by the <code>PerUnitStorageThroughput</code> (MB/s/TiB). For a 2.4-TiB ﬁle system, provisioning 50 MB/s/TiB of <code>PerUnitStorageThroughput</code> yields 120 MB/s of ﬁle system throughput. You pay for the amount of throughput that you provision. </p> <p>Valid values:</p> <ul> <li> <p>For <code>PERSISTENT_1</code> SSD storage: 50, 100, 200 MB/s/TiB.</p> </li> <li> <p>For <code>PERSISTENT_1</code> HDD storage: 12, 40 MB/s/TiB.</p> </li> <li> <p>For <code>PERSISTENT_2</code> SSD storage: 125, 250, 500, 1000 MB/s/TiB.</p> </li> </ul>"""
    daily_automatic_backup_start_time: NotRequired[
        "aws_sdk_fsx.types.daily_time.DailyTime"
    ]
    automatic_backup_retention_days: NotRequired[
        "aws_sdk_fsx.types.automatic_backup_retention_days.AutomaticBackupRetentionDays"
    ]
    """<p>The number of days to retain automatic backups. Setting this property to <code>0</code> disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is <code>0</code>.</p>"""
    copy_tags_to_backups: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>(Optional) Not available for use with file systems that are linked to a data repository. A boolean flag indicating whether tags for the file system should be copied to backups. The default value is false. If <code>CopyTagsToBackups</code> is set to true, all file system tags are copied to all automatic and user-initiated backups when the user doesn't specify any backup-specific tags. If <code>CopyTagsToBackups</code> is set to true and you specify one or more backup tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.</p> <p>(Default = <code>false</code>)</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-backups-fsx.html\"> Working with backups</a> in the <i>Amazon FSx for Lustre User Guide</i>.</p>"""
    drive_cache_type: NotRequired["aws_sdk_fsx.types.drive_cache_type.DriveCacheType"]
    """<p>The type of drive cache used by <code>PERSISTENT_1</code> file systems that are provisioned with HDD storage devices. This parameter is required when storage type is HDD. Set this property to <code>READ</code> to improve the performance for frequently accessed files by caching up to 20% of the total storage capacity of the file system.</p> <p>This parameter is required when <code>StorageType</code> is set to <code>HDD</code>.</p>"""
    data_compression_type: NotRequired[
        "aws_sdk_fsx.types.data_compression_type.DataCompressionType"
    ]
    """<p>Sets the data compression configuration for the file system. <code>DataCompressionType</code> can have the following values:</p> <ul> <li> <p> <code>NONE</code> - (Default) Data compression is turned off when the file system is created.</p> </li> <li> <p> <code>LZ4</code> - Data compression is turned on with the LZ4 algorithm.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html\">Lustre data compression</a> in the <i>Amazon FSx for Lustre User Guide</i>.</p>"""
    efa_enabled: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>(Optional) Specifies whether Elastic Fabric Adapter (EFA) and GPUDirect Storage (GDS) support is enabled for the Amazon FSx for Lustre file system.</p> <p>(Default = <code>false</code>)</p>"""
    log_configuration: NotRequired[
        "aws_sdk_fsx.types.lustre_log_create_configuration.LustreLogCreateConfiguration"
    ]
    """<p>The Lustre logging configuration used when creating an Amazon FSx for Lustre file system. When logging is enabled, Lustre logs error and warning events for data repositories associated with your file system to Amazon CloudWatch Logs.</p>"""
    root_squash_configuration: NotRequired[
        "aws_sdk_fsx.types.lustre_root_squash_configuration.LustreRootSquashConfiguration"
    ]
    """<p>The Lustre root squash configuration used when creating an Amazon FSx for Lustre file system. When enabled, root squash restricts root-level access from clients that try to access your file system as a root user.</p>"""
    metadata_configuration: NotRequired[
        "aws_sdk_fsx.types.create_file_system_lustre_metadata_configuration.CreateFileSystemLustreMetadataConfiguration"
    ]
    """<p>The Lustre metadata performance configuration for the creation of an FSx for Lustre file system using a <code>PERSISTENT_2</code> deployment type.</p>"""
    throughput_capacity: NotRequired[
        "aws_sdk_fsx.types.throughput_capacity_mbps.ThroughputCapacityMbps"
    ]
    """<p>Specifies the throughput of an FSx for Lustre file system using the Intelligent-Tiering storage class, measured in megabytes per second (MBps). Valid values are 4000 MBps or multiples of 4000 MBps. You pay for the amount of throughput that you provision.</p>"""
    data_read_cache_configuration: NotRequired[
        "aws_sdk_fsx.types.lustre_read_cache_configuration.LustreReadCacheConfiguration"
    ]
    """<p>Specifies the optional provisioned SSD read cache on FSx for Lustre file systems that use the Intelligent-Tiering storage class. Required when <code>StorageType</code> is set to <code>INTELLIGENT_TIERING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFileSystemLustreConfiguration) -> dict:
    out: dict = {}
    if "weekly_maintenance_start_time" in value:
        out["WeeklyMaintenanceStartTime"] = value["weekly_maintenance_start_time"]
    if "import_path" in value:
        out["ImportPath"] = value["import_path"]
    if "export_path" in value:
        out["ExportPath"] = value["export_path"]
    if "imported_file_chunk_size" in value:
        out["ImportedFileChunkSize"] = value["imported_file_chunk_size"]
    if "deployment_type" in value:
        import aws_sdk_fsx.types.lustre_deployment_type

        out["DeploymentType"] = (
            aws_sdk_fsx.types.lustre_deployment_type.serialize_aws_json_1_1(
                value["deployment_type"]
            )
        )
    if "auto_import_policy" in value:
        import aws_sdk_fsx.types.auto_import_policy_type

        out["AutoImportPolicy"] = (
            aws_sdk_fsx.types.auto_import_policy_type.serialize_aws_json_1_1(
                value["auto_import_policy"]
            )
        )
    if "per_unit_storage_throughput" in value:
        out["PerUnitStorageThroughput"] = value["per_unit_storage_throughput"]
    if "daily_automatic_backup_start_time" in value:
        out["DailyAutomaticBackupStartTime"] = value[
            "daily_automatic_backup_start_time"
        ]
    if "automatic_backup_retention_days" in value:
        out["AutomaticBackupRetentionDays"] = value["automatic_backup_retention_days"]
    if "copy_tags_to_backups" in value:
        out["CopyTagsToBackups"] = value["copy_tags_to_backups"]
    if "drive_cache_type" in value:
        import aws_sdk_fsx.types.drive_cache_type

        out["DriveCacheType"] = (
            aws_sdk_fsx.types.drive_cache_type.serialize_aws_json_1_1(
                value["drive_cache_type"]
            )
        )
    if "data_compression_type" in value:
        import aws_sdk_fsx.types.data_compression_type

        out["DataCompressionType"] = (
            aws_sdk_fsx.types.data_compression_type.serialize_aws_json_1_1(
                value["data_compression_type"]
            )
        )
    if "efa_enabled" in value:
        out["EfaEnabled"] = value["efa_enabled"]
    if "log_configuration" in value:
        import aws_sdk_fsx.types.lustre_log_create_configuration

        out["LogConfiguration"] = (
            aws_sdk_fsx.types.lustre_log_create_configuration.serialize_aws_json_1_1(
                value["log_configuration"]
            )
        )
    if "root_squash_configuration" in value:
        import aws_sdk_fsx.types.lustre_root_squash_configuration

        out["RootSquashConfiguration"] = (
            aws_sdk_fsx.types.lustre_root_squash_configuration.serialize_aws_json_1_1(
                value["root_squash_configuration"]
            )
        )
    if "metadata_configuration" in value:
        import aws_sdk_fsx.types.create_file_system_lustre_metadata_configuration

        out["MetadataConfiguration"] = (
            aws_sdk_fsx.types.create_file_system_lustre_metadata_configuration.serialize_aws_json_1_1(
                value["metadata_configuration"]
            )
        )
    if "throughput_capacity" in value:
        out["ThroughputCapacity"] = value["throughput_capacity"]
    if "data_read_cache_configuration" in value:
        import aws_sdk_fsx.types.lustre_read_cache_configuration

        out["DataReadCacheConfiguration"] = (
            aws_sdk_fsx.types.lustre_read_cache_configuration.serialize_aws_json_1_1(
                value["data_read_cache_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFileSystemLustreConfiguration:
    out: CreateFileSystemLustreConfiguration = {}  # type: ignore[typeddict-item]
    if "WeeklyMaintenanceStartTime" in data:
        out["weekly_maintenance_start_time"] = data["WeeklyMaintenanceStartTime"]
    if "ImportPath" in data:
        out["import_path"] = data["ImportPath"]
    if "ExportPath" in data:
        out["export_path"] = data["ExportPath"]
    if "ImportedFileChunkSize" in data:
        out["imported_file_chunk_size"] = data["ImportedFileChunkSize"]
    if "DeploymentType" in data:
        import aws_sdk_fsx.types.lustre_deployment_type

        out["deployment_type"] = (
            aws_sdk_fsx.types.lustre_deployment_type.deserialize_aws_json_1_1(
                data["DeploymentType"]
            )
        )
    if "AutoImportPolicy" in data:
        import aws_sdk_fsx.types.auto_import_policy_type

        out["auto_import_policy"] = (
            aws_sdk_fsx.types.auto_import_policy_type.deserialize_aws_json_1_1(
                data["AutoImportPolicy"]
            )
        )
    if "PerUnitStorageThroughput" in data:
        out["per_unit_storage_throughput"] = data["PerUnitStorageThroughput"]
    if "DailyAutomaticBackupStartTime" in data:
        out["daily_automatic_backup_start_time"] = data["DailyAutomaticBackupStartTime"]
    if "AutomaticBackupRetentionDays" in data:
        out["automatic_backup_retention_days"] = data["AutomaticBackupRetentionDays"]
    if "CopyTagsToBackups" in data:
        out["copy_tags_to_backups"] = data["CopyTagsToBackups"]
    if "DriveCacheType" in data:
        import aws_sdk_fsx.types.drive_cache_type

        out["drive_cache_type"] = (
            aws_sdk_fsx.types.drive_cache_type.deserialize_aws_json_1_1(
                data["DriveCacheType"]
            )
        )
    if "DataCompressionType" in data:
        import aws_sdk_fsx.types.data_compression_type

        out["data_compression_type"] = (
            aws_sdk_fsx.types.data_compression_type.deserialize_aws_json_1_1(
                data["DataCompressionType"]
            )
        )
    if "EfaEnabled" in data:
        out["efa_enabled"] = data["EfaEnabled"]
    if "LogConfiguration" in data:
        import aws_sdk_fsx.types.lustre_log_create_configuration

        out["log_configuration"] = (
            aws_sdk_fsx.types.lustre_log_create_configuration.deserialize_aws_json_1_1(
                data["LogConfiguration"]
            )
        )
    if "RootSquashConfiguration" in data:
        import aws_sdk_fsx.types.lustre_root_squash_configuration

        out["root_squash_configuration"] = (
            aws_sdk_fsx.types.lustre_root_squash_configuration.deserialize_aws_json_1_1(
                data["RootSquashConfiguration"]
            )
        )
    if "MetadataConfiguration" in data:
        import aws_sdk_fsx.types.create_file_system_lustre_metadata_configuration

        out["metadata_configuration"] = (
            aws_sdk_fsx.types.create_file_system_lustre_metadata_configuration.deserialize_aws_json_1_1(
                data["MetadataConfiguration"]
            )
        )
    if "ThroughputCapacity" in data:
        out["throughput_capacity"] = data["ThroughputCapacity"]
    if "DataReadCacheConfiguration" in data:
        import aws_sdk_fsx.types.lustre_read_cache_configuration

        out["data_read_cache_configuration"] = (
            aws_sdk_fsx.types.lustre_read_cache_configuration.deserialize_aws_json_1_1(
                data["DataReadCacheConfiguration"]
            )
        )
    return out
