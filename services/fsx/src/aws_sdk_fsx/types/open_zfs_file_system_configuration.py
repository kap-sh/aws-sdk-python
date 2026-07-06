"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSFileSystemConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.automatic_backup_retention_days
    import aws_sdk_fsx.types.daily_time
    import aws_sdk_fsx.types.disk_iops_configuration
    import aws_sdk_fsx.types.flag
    import aws_sdk_fsx.types.ip_address
    import aws_sdk_fsx.types.ip_address_range
    import aws_sdk_fsx.types.ipv6_address_range
    import aws_sdk_fsx.types.megabytes_per_second
    import aws_sdk_fsx.types.open_zfs_deployment_type
    import aws_sdk_fsx.types.open_zfs_read_cache_configuration
    import aws_sdk_fsx.types.route_table_ids
    import aws_sdk_fsx.types.subnet_id
    import aws_sdk_fsx.types.volume_id
    import aws_sdk_fsx.types.weekly_time


class OpenZFSFileSystemConfiguration(TypedDict, closed=True):
    automatic_backup_retention_days: NotRequired[
        "aws_sdk_fsx.types.automatic_backup_retention_days.AutomaticBackupRetentionDays"
    ]
    copy_tags_to_backups: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>A Boolean value indicating whether tags on the file system should be copied to backups. If it's set to <code>true</code>, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesn't specify any tags. If this value is <code>true</code> and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value. </p>"""
    copy_tags_to_volumes: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to <code>false</code>. If it's set to <code>true</code>, all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is <code>true</code> and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value. </p>"""
    daily_automatic_backup_start_time: NotRequired[
        "aws_sdk_fsx.types.daily_time.DailyTime"
    ]
    deployment_type: NotRequired[
        "aws_sdk_fsx.types.open_zfs_deployment_type.OpenZFSDeploymentType"
    ]
    """<p>Specifies the file-system deployment type. Amazon FSx for OpenZFS supports <code>MULTI_AZ_1</code>, <code>SINGLE_AZ_HA_2</code>, <code>SINGLE_AZ_HA_1</code>, <code>SINGLE_AZ_2</code>, and <code>SINGLE_AZ_1</code>.</p>"""
    throughput_capacity: NotRequired[
        "aws_sdk_fsx.types.megabytes_per_second.MegabytesPerSecond"
    ]
    """<p>The throughput of an Amazon FSx file system, measured in megabytes per second (MBps).</p>"""
    weekly_maintenance_start_time: NotRequired[
        "aws_sdk_fsx.types.weekly_time.WeeklyTime"
    ]
    disk_iops_configuration: NotRequired[
        "aws_sdk_fsx.types.disk_iops_configuration.DiskIopsConfiguration"
    ]
    root_volume_id: NotRequired["aws_sdk_fsx.types.volume_id.VolumeId"]
    """<p>The ID of the root volume of the OpenZFS file system. </p>"""
    preferred_subnet_id: NotRequired["aws_sdk_fsx.types.subnet_id.SubnetId"]
    """<p>Required when <code>DeploymentType</code> is set to <code>MULTI_AZ_1</code>. This specifies the subnet in which you want the preferred file server to be located.</p>"""
    endpoint_ip_address_range: NotRequired[
        "aws_sdk_fsx.types.ip_address_range.IpAddressRange"
    ]
    """<p>(Multi-AZ only) Specifies the IPv4 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /28 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables.</p>"""
    endpoint_ipv6_address_range: NotRequired[
        "aws_sdk_fsx.types.ipv6_address_range.Ipv6AddressRange"
    ]
    """<p>(Multi-AZ only) Specifies the IPv6 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /118 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.</p>"""
    route_table_ids: NotRequired["aws_sdk_fsx.types.route_table_ids.RouteTableIds"]
    """<p>(Multi-AZ only) The VPC route tables in which your file system's endpoints are created.</p>"""
    endpoint_ip_address: NotRequired["aws_sdk_fsx.types.ip_address.IpAddress"]
    """<p>The IPv4 address of the endpoint that is used to access data or to manage the file system.</p>"""
    endpoint_ipv6_address: NotRequired["aws_sdk_fsx.types.ip_address.IpAddress"]
    """<p>The IPv6 address of the endpoint that is used to access data or to manage the file system.</p>"""
    read_cache_configuration: NotRequired[
        "aws_sdk_fsx.types.open_zfs_read_cache_configuration.OpenZFSReadCacheConfiguration"
    ]
    """<p> Required when <code>StorageType</code> is set to <code>INTELLIGENT_TIERING</code>. Specifies the optional provisioned SSD read cache. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSFileSystemConfiguration) -> dict:
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
    if "deployment_type" in value:
        import aws_sdk_fsx.types.open_zfs_deployment_type

        out["DeploymentType"] = (
            aws_sdk_fsx.types.open_zfs_deployment_type.serialize_aws_json_1_1(
                value["deployment_type"]
            )
        )
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
    if "root_volume_id" in value:
        out["RootVolumeId"] = value["root_volume_id"]
    if "preferred_subnet_id" in value:
        out["PreferredSubnetId"] = value["preferred_subnet_id"]
    if "endpoint_ip_address_range" in value:
        out["EndpointIpAddressRange"] = value["endpoint_ip_address_range"]
    if "endpoint_ipv6_address_range" in value:
        out["EndpointIpv6AddressRange"] = value["endpoint_ipv6_address_range"]
    if "route_table_ids" in value:
        import aws_sdk_fsx.types.route_table_ids

        out["RouteTableIds"] = aws_sdk_fsx.types.route_table_ids.serialize_aws_json_1_1(
            value["route_table_ids"]
        )
    if "endpoint_ip_address" in value:
        out["EndpointIpAddress"] = value["endpoint_ip_address"]
    if "endpoint_ipv6_address" in value:
        out["EndpointIpv6Address"] = value["endpoint_ipv6_address"]
    if "read_cache_configuration" in value:
        import aws_sdk_fsx.types.open_zfs_read_cache_configuration

        out["ReadCacheConfiguration"] = (
            aws_sdk_fsx.types.open_zfs_read_cache_configuration.serialize_aws_json_1_1(
                value["read_cache_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenZFSFileSystemConfiguration:
    out: OpenZFSFileSystemConfiguration = {}  # type: ignore[typeddict-item]
    if "AutomaticBackupRetentionDays" in data:
        out["automatic_backup_retention_days"] = data["AutomaticBackupRetentionDays"]
    if "CopyTagsToBackups" in data:
        out["copy_tags_to_backups"] = data["CopyTagsToBackups"]
    if "CopyTagsToVolumes" in data:
        out["copy_tags_to_volumes"] = data["CopyTagsToVolumes"]
    if "DailyAutomaticBackupStartTime" in data:
        out["daily_automatic_backup_start_time"] = data["DailyAutomaticBackupStartTime"]
    if "DeploymentType" in data:
        import aws_sdk_fsx.types.open_zfs_deployment_type

        out["deployment_type"] = (
            aws_sdk_fsx.types.open_zfs_deployment_type.deserialize_aws_json_1_1(
                data["DeploymentType"]
            )
        )
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
    if "RootVolumeId" in data:
        out["root_volume_id"] = data["RootVolumeId"]
    if "PreferredSubnetId" in data:
        out["preferred_subnet_id"] = data["PreferredSubnetId"]
    if "EndpointIpAddressRange" in data:
        out["endpoint_ip_address_range"] = data["EndpointIpAddressRange"]
    if "EndpointIpv6AddressRange" in data:
        out["endpoint_ipv6_address_range"] = data["EndpointIpv6AddressRange"]
    if "RouteTableIds" in data:
        import aws_sdk_fsx.types.route_table_ids

        out["route_table_ids"] = (
            aws_sdk_fsx.types.route_table_ids.deserialize_aws_json_1_1(
                data["RouteTableIds"]
            )
        )
    if "EndpointIpAddress" in data:
        out["endpoint_ip_address"] = data["EndpointIpAddress"]
    if "EndpointIpv6Address" in data:
        out["endpoint_ipv6_address"] = data["EndpointIpv6Address"]
    if "ReadCacheConfiguration" in data:
        import aws_sdk_fsx.types.open_zfs_read_cache_configuration

        out["read_cache_configuration"] = (
            aws_sdk_fsx.types.open_zfs_read_cache_configuration.deserialize_aws_json_1_1(
                data["ReadCacheConfiguration"]
            )
        )
    return out
