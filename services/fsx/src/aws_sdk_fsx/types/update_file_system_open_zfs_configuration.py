"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateFileSystemOpenZFSConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.automatic_backup_retention_days
    import aws_sdk_fsx.types.daily_time
    import aws_sdk_fsx.types.disk_iops_configuration
    import aws_sdk_fsx.types.flag
    import aws_sdk_fsx.types.ipv6_address_range
    import aws_sdk_fsx.types.megabytes_per_second
    import aws_sdk_fsx.types.open_zfs_read_cache_configuration
    import aws_sdk_fsx.types.route_table_ids
    import aws_sdk_fsx.types.weekly_time


class UpdateFileSystemOpenZFSConfiguration(TypedDict):
    automatic_backup_retention_days: NotRequired[
        "aws_sdk_fsx.types.automatic_backup_retention_days.AutomaticBackupRetentionDays"
    ]
    copy_tags_to_backups: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>A Boolean value indicating whether tags for the file system should be copied to backups. This value defaults to <code>false</code>. If it's set to <code>true</code>, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is <code>true</code> and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.</p>"""
    copy_tags_to_volumes: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to <code>false</code>. If it's set to <code>true</code>, all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is <code>true</code> and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.</p>"""
    daily_automatic_backup_start_time: NotRequired[
        "aws_sdk_fsx.types.daily_time.DailyTime"
    ]
    throughput_capacity: NotRequired[
        "aws_sdk_fsx.types.megabytes_per_second.MegabytesPerSecond"
    ]
    """<p>The throughput of an Amazon FSx for OpenZFS file system, measured in megabytes per second (MB/s). Valid values depend on the DeploymentType you choose, as follows:</p> <ul> <li> <p>For <code>MULTI_AZ_1</code> and <code>SINGLE_AZ_2</code>, valid values are 160, 320, 640, 1280, 2560, 3840, 5120, 7680, or 10240 MB/s.</p> </li> <li> <p>For <code>SINGLE_AZ_1</code>, valid values are 64, 128, 256, 512, 1024, 2048, 3072, or 4096 MB/s.</p> </li> </ul>"""
    weekly_maintenance_start_time: NotRequired[
        "aws_sdk_fsx.types.weekly_time.WeeklyTime"
    ]
    disk_iops_configuration: NotRequired[
        "aws_sdk_fsx.types.disk_iops_configuration.DiskIopsConfiguration"
    ]
    add_route_table_ids: NotRequired["aws_sdk_fsx.types.route_table_ids.RouteTableIds"]
    """<p>(Multi-AZ only) A list of IDs of new virtual private cloud (VPC) route tables to associate (add) with your Amazon FSx for OpenZFS file system.</p>"""
    remove_route_table_ids: NotRequired[
        "aws_sdk_fsx.types.route_table_ids.RouteTableIds"
    ]
    """<p>(Multi-AZ only) A list of IDs of existing virtual private cloud (VPC) route tables to disassociate (remove) from your Amazon FSx for OpenZFS file system. You can use the API operation to retrieve the list of VPC route table IDs for a file system.</p>"""
    read_cache_configuration: NotRequired[
        "aws_sdk_fsx.types.open_zfs_read_cache_configuration.OpenZFSReadCacheConfiguration"
    ]
    """<p> The configuration for the optional provisioned SSD read cache on file systems that use the Intelligent-Tiering storage class.</p>"""
    endpoint_ipv6_address_range: NotRequired[
        "aws_sdk_fsx.types.ipv6_address_range.Ipv6AddressRange"
    ]
    """<p>(Multi-AZ only) Specifies the IPv6 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /118 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFileSystemOpenZFSConfiguration) -> dict:
    out: dict = {}
    if "automatic_backup_retention_days" in value:
        out["AutomaticBackupRetentionDays"] = value["automatic_backup_retention_days"]
    if "copy_tags_to_backups" in value:
        out["CopyTagsToBackups"] = value["copy_tags_to_backups"]
    if "copy_tags_to_volumes" in value:
        out["CopyTagsToVolumes"] = value["copy_tags_to_volumes"]
    if "daily_automatic_backup_start_time" in value:
        out["DailyAutomaticBackupStartTime"] = value[
            "daily_automatic_backup_start_time"
        ]
    if "throughput_capacity" in value:
        out["ThroughputCapacity"] = value["throughput_capacity"]
    if "weekly_maintenance_start_time" in value:
        out["WeeklyMaintenanceStartTime"] = value["weekly_maintenance_start_time"]
    if "disk_iops_configuration" in value:
        import aws_sdk_fsx.types.disk_iops_configuration

        out["DiskIopsConfiguration"] = (
            aws_sdk_fsx.types.disk_iops_configuration.serialize_aws_json_1_1(
                value["disk_iops_configuration"]
            )
        )
    if "add_route_table_ids" in value:
        import aws_sdk_fsx.types.route_table_ids

        out["AddRouteTableIds"] = (
            aws_sdk_fsx.types.route_table_ids.serialize_aws_json_1_1(
                value["add_route_table_ids"]
            )
        )
    if "remove_route_table_ids" in value:
        import aws_sdk_fsx.types.route_table_ids

        out["RemoveRouteTableIds"] = (
            aws_sdk_fsx.types.route_table_ids.serialize_aws_json_1_1(
                value["remove_route_table_ids"]
            )
        )
    if "read_cache_configuration" in value:
        import aws_sdk_fsx.types.open_zfs_read_cache_configuration

        out["ReadCacheConfiguration"] = (
            aws_sdk_fsx.types.open_zfs_read_cache_configuration.serialize_aws_json_1_1(
                value["read_cache_configuration"]
            )
        )
    if "endpoint_ipv6_address_range" in value:
        out["EndpointIpv6AddressRange"] = value["endpoint_ipv6_address_range"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFileSystemOpenZFSConfiguration:
    out: UpdateFileSystemOpenZFSConfiguration = {}  # type: ignore[typeddict-item]
    if "AutomaticBackupRetentionDays" in data:
        out["automatic_backup_retention_days"] = data["AutomaticBackupRetentionDays"]
    if "CopyTagsToBackups" in data:
        out["copy_tags_to_backups"] = data["CopyTagsToBackups"]
    if "CopyTagsToVolumes" in data:
        out["copy_tags_to_volumes"] = data["CopyTagsToVolumes"]
    if "DailyAutomaticBackupStartTime" in data:
        out["daily_automatic_backup_start_time"] = data["DailyAutomaticBackupStartTime"]
    if "ThroughputCapacity" in data:
        out["throughput_capacity"] = data["ThroughputCapacity"]
    if "WeeklyMaintenanceStartTime" in data:
        out["weekly_maintenance_start_time"] = data["WeeklyMaintenanceStartTime"]
    if "DiskIopsConfiguration" in data:
        import aws_sdk_fsx.types.disk_iops_configuration

        out["disk_iops_configuration"] = (
            aws_sdk_fsx.types.disk_iops_configuration.deserialize_aws_json_1_1(
                data["DiskIopsConfiguration"]
            )
        )
    if "AddRouteTableIds" in data:
        import aws_sdk_fsx.types.route_table_ids

        out["add_route_table_ids"] = (
            aws_sdk_fsx.types.route_table_ids.deserialize_aws_json_1_1(
                data["AddRouteTableIds"]
            )
        )
    if "RemoveRouteTableIds" in data:
        import aws_sdk_fsx.types.route_table_ids

        out["remove_route_table_ids"] = (
            aws_sdk_fsx.types.route_table_ids.deserialize_aws_json_1_1(
                data["RemoveRouteTableIds"]
            )
        )
    if "ReadCacheConfiguration" in data:
        import aws_sdk_fsx.types.open_zfs_read_cache_configuration

        out["read_cache_configuration"] = (
            aws_sdk_fsx.types.open_zfs_read_cache_configuration.deserialize_aws_json_1_1(
                data["ReadCacheConfiguration"]
            )
        )
    if "EndpointIpv6AddressRange" in data:
        out["endpoint_ipv6_address_range"] = data["EndpointIpv6AddressRange"]
    return out
