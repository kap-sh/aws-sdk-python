"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheLustreConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_cache_lustre_deployment_type
    import aws_sdk_fsx.types.file_cache_lustre_metadata_configuration
    import aws_sdk_fsx.types.lustre_file_system_mount_name
    import aws_sdk_fsx.types.lustre_log_configuration
    import aws_sdk_fsx.types.per_unit_storage_throughput
    import aws_sdk_fsx.types.weekly_time


class FileCacheLustreConfiguration(TypedDict):
    per_unit_storage_throughput: NotRequired[
        "aws_sdk_fsx.types.per_unit_storage_throughput.PerUnitStorageThroughput"
    ]
    """<p>Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. Cache throughput capacity is equal to Storage capacity (TiB) * PerUnitStorageThroughput (MB/s/TiB). The only supported value is <code>1000</code>.</p>"""
    deployment_type: NotRequired[
        "aws_sdk_fsx.types.file_cache_lustre_deployment_type.FileCacheLustreDeploymentType"
    ]
    """<p>The deployment type of the Amazon File Cache resource, which must be <code>CACHE_1</code>.</p>"""
    mount_name: NotRequired[
        "aws_sdk_fsx.types.lustre_file_system_mount_name.LustreFileSystemMountName"
    ]
    """<p>You use the <code>MountName</code> value when mounting the cache. If you pass a cache ID to the <code>DescribeFileCaches</code> operation, it returns the the <code>MountName</code> value as part of the cache's description.</p>"""
    weekly_maintenance_start_time: NotRequired[
        "aws_sdk_fsx.types.weekly_time.WeeklyTime"
    ]
    metadata_configuration: NotRequired[
        "aws_sdk_fsx.types.file_cache_lustre_metadata_configuration.FileCacheLustreMetadataConfiguration"
    ]
    """<p>The configuration for a Lustre MDT (Metadata Target) storage volume.</p>"""
    log_configuration: NotRequired[
        "aws_sdk_fsx.types.lustre_log_configuration.LustreLogConfiguration"
    ]
    """<p>The configuration for Lustre logging used to write the enabled logging events for your Amazon File Cache resource to Amazon CloudWatch Logs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCacheLustreConfiguration) -> dict:
    out: dict = {}
    if "per_unit_storage_throughput" in value:
        out["PerUnitStorageThroughput"] = value["per_unit_storage_throughput"]
    if "deployment_type" in value:
        import aws_sdk_fsx.types.file_cache_lustre_deployment_type

        out["DeploymentType"] = (
            aws_sdk_fsx.types.file_cache_lustre_deployment_type.serialize_aws_json_1_1(
                value["deployment_type"]
            )
        )
    if "mount_name" in value:
        out["MountName"] = value["mount_name"]
    if "weekly_maintenance_start_time" in value:
        out["WeeklyMaintenanceStartTime"] = value["weekly_maintenance_start_time"]
    if "metadata_configuration" in value:
        import aws_sdk_fsx.types.file_cache_lustre_metadata_configuration

        out["MetadataConfiguration"] = (
            aws_sdk_fsx.types.file_cache_lustre_metadata_configuration.serialize_aws_json_1_1(
                value["metadata_configuration"]
            )
        )
    if "log_configuration" in value:
        import aws_sdk_fsx.types.lustre_log_configuration

        out["LogConfiguration"] = (
            aws_sdk_fsx.types.lustre_log_configuration.serialize_aws_json_1_1(
                value["log_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileCacheLustreConfiguration:
    out: FileCacheLustreConfiguration = {}  # type: ignore[typeddict-item]
    if "PerUnitStorageThroughput" in data:
        out["per_unit_storage_throughput"] = data["PerUnitStorageThroughput"]
    if "DeploymentType" in data:
        import aws_sdk_fsx.types.file_cache_lustre_deployment_type

        out["deployment_type"] = (
            aws_sdk_fsx.types.file_cache_lustre_deployment_type.deserialize_aws_json_1_1(
                data["DeploymentType"]
            )
        )
    if "MountName" in data:
        out["mount_name"] = data["MountName"]
    if "WeeklyMaintenanceStartTime" in data:
        out["weekly_maintenance_start_time"] = data["WeeklyMaintenanceStartTime"]
    if "MetadataConfiguration" in data:
        import aws_sdk_fsx.types.file_cache_lustre_metadata_configuration

        out["metadata_configuration"] = (
            aws_sdk_fsx.types.file_cache_lustre_metadata_configuration.deserialize_aws_json_1_1(
                data["MetadataConfiguration"]
            )
        )
    if "LogConfiguration" in data:
        import aws_sdk_fsx.types.lustre_log_configuration

        out["log_configuration"] = (
            aws_sdk_fsx.types.lustre_log_configuration.deserialize_aws_json_1_1(
                data["LogConfiguration"]
            )
        )
    return out
