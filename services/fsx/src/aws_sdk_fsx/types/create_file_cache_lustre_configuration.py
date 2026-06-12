"""Generated from Smithy shape ``com.amazonaws.fsx#CreateFileCacheLustreConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_cache_lustre_deployment_type
    import aws_sdk_fsx.types.file_cache_lustre_metadata_configuration
    import aws_sdk_fsx.types.per_unit_storage_throughput
    import aws_sdk_fsx.types.weekly_time


class CreateFileCacheLustreConfiguration(TypedDict):
    per_unit_storage_throughput: NotRequired[
        "aws_sdk_fsx.types.per_unit_storage_throughput.PerUnitStorageThroughput"
    ]
    """<p>Provisions the amount of read and write throughput for each 1 tebibyte (TiB) of cache storage capacity, in MB/s/TiB. The only supported value is <code>1000</code>.</p>"""
    deployment_type: NotRequired[
        "aws_sdk_fsx.types.file_cache_lustre_deployment_type.FileCacheLustreDeploymentType"
    ]
    """<p>Specifies the cache deployment type, which must be <code>CACHE_1</code>.</p>"""
    weekly_maintenance_start_time: NotRequired[
        "aws_sdk_fsx.types.weekly_time.WeeklyTime"
    ]
    metadata_configuration: NotRequired[
        "aws_sdk_fsx.types.file_cache_lustre_metadata_configuration.FileCacheLustreMetadataConfiguration"
    ]
    """<p>The configuration for a Lustre MDT (Metadata Target) storage volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFileCacheLustreConfiguration) -> dict:
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
    if "weekly_maintenance_start_time" in value:
        out["WeeklyMaintenanceStartTime"] = value["weekly_maintenance_start_time"]
    if "metadata_configuration" in value:
        import aws_sdk_fsx.types.file_cache_lustre_metadata_configuration

        out["MetadataConfiguration"] = (
            aws_sdk_fsx.types.file_cache_lustre_metadata_configuration.serialize_aws_json_1_1(
                value["metadata_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFileCacheLustreConfiguration:
    out: CreateFileCacheLustreConfiguration = {}  # type: ignore[typeddict-item]
    if "PerUnitStorageThroughput" in data:
        out["per_unit_storage_throughput"] = data["PerUnitStorageThroughput"]
    if "DeploymentType" in data:
        import aws_sdk_fsx.types.file_cache_lustre_deployment_type

        out["deployment_type"] = (
            aws_sdk_fsx.types.file_cache_lustre_deployment_type.deserialize_aws_json_1_1(
                data["DeploymentType"]
            )
        )
    if "WeeklyMaintenanceStartTime" in data:
        out["weekly_maintenance_start_time"] = data["WeeklyMaintenanceStartTime"]
    if "MetadataConfiguration" in data:
        import aws_sdk_fsx.types.file_cache_lustre_metadata_configuration

        out["metadata_configuration"] = (
            aws_sdk_fsx.types.file_cache_lustre_metadata_configuration.deserialize_aws_json_1_1(
                data["MetadataConfiguration"]
            )
        )
    return out
