"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryConnectSettingsDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.availability_zones
    import aws_sdk_directory_service.types.ip_addrs
    import aws_sdk_directory_service.types.ip_v6_addrs
    import aws_sdk_directory_service.types.security_group_id
    import aws_sdk_directory_service.types.subnet_ids
    import aws_sdk_directory_service.types.user_name
    import aws_sdk_directory_service.types.vpc_id


class DirectoryConnectSettingsDescription(TypedDict, closed=True):
    vpc_id: NotRequired["aws_sdk_directory_service.types.vpc_id.VpcId"]
    """<p>The identifier of the VPC that the AD Connector is in.</p>"""
    subnet_ids: NotRequired["aws_sdk_directory_service.types.subnet_ids.SubnetIds"]
    """<p>A list of subnet identifiers in the VPC that the AD Connector is in.</p>"""
    customer_user_name: NotRequired[
        "aws_sdk_directory_service.types.user_name.UserName"
    ]
    """<p>The user name of the service account in your self-managed directory.</p>"""
    security_group_id: NotRequired[
        "aws_sdk_directory_service.types.security_group_id.SecurityGroupId"
    ]
    """<p>The security group identifier for the AD Connector directory.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_directory_service.types.availability_zones.AvailabilityZones"
    ]
    """<p>The Availability Zones that the directory is in.</p>"""
    connect_ips: NotRequired["aws_sdk_directory_service.types.ip_addrs.IpAddrs"]
    """<p>The IP addresses of the AD Connector servers.</p>"""
    connect_ips_v6: NotRequired["aws_sdk_directory_service.types.ip_v6_addrs.IpV6Addrs"]
    """<p>The IPv6 addresses of the AD Connector servers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryConnectSettingsDescription) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import aws_sdk_directory_service.types.subnet_ids

        out["SubnetIds"] = (
            aws_sdk_directory_service.types.subnet_ids.serialize_aws_json_1_1(
                value["subnet_ids"]
            )
        )
    if "customer_user_name" in value:
        out["CustomerUserName"] = value["customer_user_name"]
    if "security_group_id" in value:
        out["SecurityGroupId"] = value["security_group_id"]
    if "availability_zones" in value:
        import aws_sdk_directory_service.types.availability_zones

        out["AvailabilityZones"] = (
            aws_sdk_directory_service.types.availability_zones.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    if "connect_ips" in value:
        import aws_sdk_directory_service.types.ip_addrs

        out["ConnectIps"] = (
            aws_sdk_directory_service.types.ip_addrs.serialize_aws_json_1_1(
                value["connect_ips"]
            )
        )
    if "connect_ips_v6" in value:
        import aws_sdk_directory_service.types.ip_v6_addrs

        out["ConnectIpsV6"] = (
            aws_sdk_directory_service.types.ip_v6_addrs.serialize_aws_json_1_1(
                value["connect_ips_v6"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectoryConnectSettingsDescription:
    out: DirectoryConnectSettingsDescription = {}  # type: ignore[typeddict-item]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SubnetIds" in data:
        import aws_sdk_directory_service.types.subnet_ids

        out["subnet_ids"] = (
            aws_sdk_directory_service.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    if "CustomerUserName" in data:
        out["customer_user_name"] = data["CustomerUserName"]
    if "SecurityGroupId" in data:
        out["security_group_id"] = data["SecurityGroupId"]
    if "AvailabilityZones" in data:
        import aws_sdk_directory_service.types.availability_zones

        out["availability_zones"] = (
            aws_sdk_directory_service.types.availability_zones.deserialize_aws_json_1_1(
                data["AvailabilityZones"]
            )
        )
    if "ConnectIps" in data:
        import aws_sdk_directory_service.types.ip_addrs

        out["connect_ips"] = (
            aws_sdk_directory_service.types.ip_addrs.deserialize_aws_json_1_1(
                data["ConnectIps"]
            )
        )
    if "ConnectIpsV6" in data:
        import aws_sdk_directory_service.types.ip_v6_addrs

        out["connect_ips_v6"] = (
            aws_sdk_directory_service.types.ip_v6_addrs.deserialize_aws_json_1_1(
                data["ConnectIpsV6"]
            )
        )
    return out
