"""Generated from Smithy shape ``com.amazonaws.fsx#OntapFileSystemConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.admin_password
    import aws_sdk_fsx.types.automatic_backup_retention_days
    import aws_sdk_fsx.types.daily_time
    import aws_sdk_fsx.types.disk_iops_configuration
    import aws_sdk_fsx.types.file_system_endpoints
    import aws_sdk_fsx.types.ha_pairs
    import aws_sdk_fsx.types.ip_address_range
    import aws_sdk_fsx.types.ipv6_address_range
    import aws_sdk_fsx.types.megabytes_per_second
    import aws_sdk_fsx.types.ontap_deployment_type
    import aws_sdk_fsx.types.route_table_ids
    import aws_sdk_fsx.types.subnet_id
    import aws_sdk_fsx.types.throughput_capacity_per_ha_pair
    import aws_sdk_fsx.types.weekly_time


class OntapFileSystemConfiguration(TypedDict):
    automatic_backup_retention_days: NotRequired[
        "aws_sdk_fsx.types.automatic_backup_retention_days.AutomaticBackupRetentionDays"
    ]
    daily_automatic_backup_start_time: NotRequired[
        "aws_sdk_fsx.types.daily_time.DailyTime"
    ]
    deployment_type: NotRequired[
        "aws_sdk_fsx.types.ontap_deployment_type.OntapDeploymentType"
    ]
    r"""<p>Specifies the FSx for ONTAP file system deployment type in use in the file system. </p> <ul> <li> <p> <code>MULTI_AZ_1</code> - A high availability file system configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. This is a first-generation FSx for ONTAP file system.</p> </li> <li> <p> <code>MULTI_AZ_2</code> - A high availability file system configured for Multi-AZ redundancy to tolerate temporary AZ unavailability. This is a second-generation FSx for ONTAP file system.</p> </li> <li> <p> <code>SINGLE_AZ_1</code> - A file system configured for Single-AZ redundancy. This is a first-generation FSx for ONTAP file system.</p> </li> <li> <p> <code>SINGLE_AZ_2</code> - A file system configured with multiple high-availability (HA) pairs for Single-AZ redundancy. This is a second-generation FSx for ONTAP file system.</p> </li> </ul> <p>For information about the use cases for Multi-AZ and Single-AZ deployments, refer to <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-multiAZ.html\">Choosing Multi-AZ or Single-AZ file system deployment</a>. </p>"""
    endpoint_ip_address_range: NotRequired[
        "aws_sdk_fsx.types.ip_address_range.IpAddressRange"
    ]
    """<p>(Multi-AZ only) Specifies the IPv4 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API, Amazon FSx selects an unused IP address range for you from the 198.19.* range. By default in the Amazon FSx console, Amazon FSx chooses the last 64 IP addresses from the VPC’s primary CIDR range to use as the endpoint IP address range for the file system. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables.</p>"""
    endpoints: NotRequired[
        "aws_sdk_fsx.types.file_system_endpoints.FileSystemEndpoints"
    ]
    """<p>The <code>Management</code> and <code>Intercluster</code> endpoints that are used to access data or to manage the file system using the NetApp ONTAP CLI, REST API, or NetApp SnapMirror.</p>"""
    disk_iops_configuration: NotRequired[
        "aws_sdk_fsx.types.disk_iops_configuration.DiskIopsConfiguration"
    ]
    """<p>The SSD IOPS configuration for the ONTAP file system, specifying the number of provisioned IOPS and the provision mode.</p>"""
    preferred_subnet_id: NotRequired["aws_sdk_fsx.types.subnet_id.SubnetId"]
    route_table_ids: NotRequired["aws_sdk_fsx.types.route_table_ids.RouteTableIds"]
    """<p>(Multi-AZ only) The VPC route tables in which your file system's endpoints are created.</p>"""
    throughput_capacity: NotRequired[
        "aws_sdk_fsx.types.megabytes_per_second.MegabytesPerSecond"
    ]
    weekly_maintenance_start_time: NotRequired[
        "aws_sdk_fsx.types.weekly_time.WeeklyTime"
    ]
    fsx_admin_password: NotRequired["aws_sdk_fsx.types.admin_password.AdminPassword"]
    """<p>You can use the <code>fsxadmin</code> user account to access the NetApp ONTAP CLI and REST API. The password value is always redacted in the response.</p>"""
    ha_pairs: NotRequired["aws_sdk_fsx.types.ha_pairs.HAPairs"]
    r"""<p>Specifies how many high-availability (HA) file server pairs the file system will have. The default value is 1. The value of this property affects the values of <code>StorageCapacity</code>, <code>Iops</code>, and <code>ThroughputCapacity</code>. For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/HA-pairs.html\">High-availability (HA) pairs</a> in the FSx for ONTAP user guide.</p> <p>Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:</p> <ul> <li> <p>The value of <code>HAPairs</code> is less than 1 or greater than 12.</p> </li> <li> <p>The value of <code>HAPairs</code> is greater than 1 and the value of <code>DeploymentType</code> is <code>SINGLE_AZ_1</code>, <code>MULTI_AZ_1</code>, or <code>MULTI_AZ_2</code>.</p> </li> </ul>"""
    throughput_capacity_per_ha_pair: NotRequired[
        "aws_sdk_fsx.types.throughput_capacity_per_ha_pair.ThroughputCapacityPerHAPair"
    ]
    """<p>Use to choose the throughput capacity per HA pair. When the value of <code>HAPairs</code> is equal to 1, the value of <code>ThroughputCapacityPerHAPair</code> is the total throughput for the file system.</p> <p>This field and <code>ThroughputCapacity</code> cannot be defined in the same API call, but one is required.</p> <p>This field and <code>ThroughputCapacity</code> are the same for file systems with one HA pair.</p> <ul> <li> <p>For <code>SINGLE_AZ_1</code> and <code>MULTI_AZ_1</code> file systems, valid values are 128, 256, 512, 1024, 2048, or 4096 MBps.</p> </li> <li> <p>For <code>SINGLE_AZ_2</code>, valid values are 1536, 3072, or 6144 MBps.</p> </li> <li> <p>For <code>MULTI_AZ_2</code>, valid values are 384, 768, 1536, 3072, or 6144 MBps.</p> </li> </ul> <p>Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:</p> <ul> <li> <p>The value of <code>ThroughputCapacity</code> and <code>ThroughputCapacityPerHAPair</code> are not the same value.</p> </li> <li> <p>The value of deployment type is <code>SINGLE_AZ_2</code> and <code>ThroughputCapacity</code> / <code>ThroughputCapacityPerHAPair</code> is not a valid HA pair (a value between 1 and 12).</p> </li> <li> <p>The value of <code>ThroughputCapacityPerHAPair</code> is not a valid value.</p> </li> </ul>"""
    endpoint_ipv6_address_range: NotRequired[
        "aws_sdk_fsx.types.ipv6_address_range.Ipv6AddressRange"
    ]
    """<p>(Multi-AZ only) Specifies the IPv6 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /118 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OntapFileSystemConfiguration) -> dict:
    out: dict = {}
    if "automatic_backup_retention_days" in value:
        out["AutomaticBackupRetentionDays"] = value["automatic_backup_retention_days"]
    if "daily_automatic_backup_start_time" in value:
        out["DailyAutomaticBackupStartTime"] = value[
            "daily_automatic_backup_start_time"
        ]
    if "deployment_type" in value:
        import aws_sdk_fsx.types.ontap_deployment_type

        out["DeploymentType"] = (
            aws_sdk_fsx.types.ontap_deployment_type.serialize_aws_json_1_1(
                value["deployment_type"]
            )
        )
    if "endpoint_ip_address_range" in value:
        out["EndpointIpAddressRange"] = value["endpoint_ip_address_range"]
    if "endpoints" in value:
        import aws_sdk_fsx.types.file_system_endpoints

        out["Endpoints"] = (
            aws_sdk_fsx.types.file_system_endpoints.serialize_aws_json_1_1(
                value["endpoints"]
            )
        )
    if "disk_iops_configuration" in value:
        import aws_sdk_fsx.types.disk_iops_configuration

        out["DiskIopsConfiguration"] = (
            aws_sdk_fsx.types.disk_iops_configuration.serialize_aws_json_1_1(
                value["disk_iops_configuration"]
            )
        )
    if "preferred_subnet_id" in value:
        out["PreferredSubnetId"] = value["preferred_subnet_id"]
    if "route_table_ids" in value:
        import aws_sdk_fsx.types.route_table_ids

        out["RouteTableIds"] = aws_sdk_fsx.types.route_table_ids.serialize_aws_json_1_1(
            value["route_table_ids"]
        )
    if "throughput_capacity" in value:
        out["ThroughputCapacity"] = value["throughput_capacity"]
    if "weekly_maintenance_start_time" in value:
        out["WeeklyMaintenanceStartTime"] = value["weekly_maintenance_start_time"]
    if "fsx_admin_password" in value:
        out["FsxAdminPassword"] = value["fsx_admin_password"]
    if "ha_pairs" in value:
        out["HAPairs"] = value["ha_pairs"]
    if "throughput_capacity_per_ha_pair" in value:
        out["ThroughputCapacityPerHAPair"] = value["throughput_capacity_per_ha_pair"]
    if "endpoint_ipv6_address_range" in value:
        out["EndpointIpv6AddressRange"] = value["endpoint_ipv6_address_range"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OntapFileSystemConfiguration:
    out: OntapFileSystemConfiguration = {}  # type: ignore[typeddict-item]
    if "AutomaticBackupRetentionDays" in data:
        out["automatic_backup_retention_days"] = data["AutomaticBackupRetentionDays"]
    if "DailyAutomaticBackupStartTime" in data:
        out["daily_automatic_backup_start_time"] = data["DailyAutomaticBackupStartTime"]
    if "DeploymentType" in data:
        import aws_sdk_fsx.types.ontap_deployment_type

        out["deployment_type"] = (
            aws_sdk_fsx.types.ontap_deployment_type.deserialize_aws_json_1_1(
                data["DeploymentType"]
            )
        )
    if "EndpointIpAddressRange" in data:
        out["endpoint_ip_address_range"] = data["EndpointIpAddressRange"]
    if "Endpoints" in data:
        import aws_sdk_fsx.types.file_system_endpoints

        out["endpoints"] = (
            aws_sdk_fsx.types.file_system_endpoints.deserialize_aws_json_1_1(
                data["Endpoints"]
            )
        )
    if "DiskIopsConfiguration" in data:
        import aws_sdk_fsx.types.disk_iops_configuration

        out["disk_iops_configuration"] = (
            aws_sdk_fsx.types.disk_iops_configuration.deserialize_aws_json_1_1(
                data["DiskIopsConfiguration"]
            )
        )
    if "PreferredSubnetId" in data:
        out["preferred_subnet_id"] = data["PreferredSubnetId"]
    if "RouteTableIds" in data:
        import aws_sdk_fsx.types.route_table_ids

        out["route_table_ids"] = (
            aws_sdk_fsx.types.route_table_ids.deserialize_aws_json_1_1(
                data["RouteTableIds"]
            )
        )
    if "ThroughputCapacity" in data:
        out["throughput_capacity"] = data["ThroughputCapacity"]
    if "WeeklyMaintenanceStartTime" in data:
        out["weekly_maintenance_start_time"] = data["WeeklyMaintenanceStartTime"]
    if "FsxAdminPassword" in data:
        out["fsx_admin_password"] = data["FsxAdminPassword"]
    if "HAPairs" in data:
        out["ha_pairs"] = data["HAPairs"]
    if "ThroughputCapacityPerHAPair" in data:
        out["throughput_capacity_per_ha_pair"] = data["ThroughputCapacityPerHAPair"]
    if "EndpointIpv6AddressRange" in data:
        out["endpoint_ipv6_address_range"] = data["EndpointIpv6AddressRange"]
    return out
