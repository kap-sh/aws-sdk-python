"""Generated from Smithy shape ``com.amazonaws.efs#MountTargetDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_efs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_efs.types.availability_zone_id
    import aws_sdk_efs.types.availability_zone_name
    import aws_sdk_efs.types.aws_account_id
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.ip_address
    import aws_sdk_efs.types.ipv6_address
    import aws_sdk_efs.types.life_cycle_state
    import aws_sdk_efs.types.mount_target_id
    import aws_sdk_efs.types.network_interface_id
    import aws_sdk_efs.types.subnet_id
    import aws_sdk_efs.types.vpc_id


class MountTargetDescription(TypedDict, closed=True):
    owner_id: NotRequired["aws_sdk_efs.types.aws_account_id.AwsAccountId"]
    """<p>Amazon Web Services account ID that owns the resource.</p>"""
    mount_target_id: "aws_sdk_efs.types.mount_target_id.MountTargetId"
    """<p>System-assigned mount target ID.</p>"""
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system for which the mount target is intended.</p>"""
    subnet_id: "aws_sdk_efs.types.subnet_id.SubnetId"
    """<p>The ID of the mount target's subnet.</p>"""
    life_cycle_state: "aws_sdk_efs.types.life_cycle_state.LifeCycleState"
    """<p>Lifecycle state of the mount target.</p>"""
    ip_address: NotRequired["aws_sdk_efs.types.ip_address.IpAddress"]
    """<p>Address at which the file system can be mounted by using the mount target.</p>"""
    ipv6_address: NotRequired["aws_sdk_efs.types.ipv6_address.Ipv6Address"]
    """<p>The IPv6 address for the mount target.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_efs.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface that Amazon EFS created when it created the mount target.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_efs.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The unique and consistent identifier of the Availability Zone that the mount target resides in. For example, <code>use1-az1</code> is an AZ ID for the us-east-1 Region and it has the same location in every Amazon Web Services account.</p>"""
    availability_zone_name: NotRequired[
        "aws_sdk_efs.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The name of the Availability Zone in which the mount target is located. Availability Zones are independently mapped to names for each Amazon Web Services account. For example, the Availability Zone <code>us-east-1a</code> for your Amazon Web Services account might not be the same location as <code>us-east-1a</code> for another Amazon Web Services account.</p>"""
    vpc_id: NotRequired["aws_sdk_efs.types.vpc_id.VpcId"]
    """<p>The virtual private cloud (VPC) ID that the mount target is configured in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MountTargetDescription) -> dict:
    out: dict = {}
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    out["MountTargetId"] = value["mount_target_id"]
    out["FileSystemId"] = value["file_system_id"]
    out["SubnetId"] = value["subnet_id"]
    import aws_sdk_efs.types.life_cycle_state

    out["LifeCycleState"] = aws_sdk_efs.types.life_cycle_state.serialize_json(
        value["life_cycle_state"]
    )
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "ipv6_address" in value:
        out["Ipv6Address"] = value["ipv6_address"]
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    if "availability_zone_name" in value:
        out["AvailabilityZoneName"] = value["availability_zone_name"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> MountTargetDescription:
    out: MountTargetDescription = {}  # type: ignore[typeddict-item]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "MountTargetId" in data:
        out["mount_target_id"] = data["MountTargetId"]
    else:
        raise DeserializationError("MountTargetDescription.mount_target_id required")
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    else:
        raise DeserializationError("MountTargetDescription.file_system_id required")
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    else:
        raise DeserializationError("MountTargetDescription.subnet_id required")
    if "LifeCycleState" in data:
        import aws_sdk_efs.types.life_cycle_state

        out["life_cycle_state"] = aws_sdk_efs.types.life_cycle_state.deserialize_json(
            data["LifeCycleState"]
        )
    else:
        raise DeserializationError("MountTargetDescription.life_cycle_state required")
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "Ipv6Address" in data:
        out["ipv6_address"] = data["Ipv6Address"]
    if "NetworkInterfaceId" in data:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    if "AvailabilityZoneId" in data:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    if "AvailabilityZoneName" in data:
        out["availability_zone_name"] = data["AvailabilityZoneName"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    return out
