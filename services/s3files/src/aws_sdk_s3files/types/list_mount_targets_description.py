"""Generated from Smithy shape ``com.amazonaws.s3files#ListMountTargetsDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3files.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3files.types.availability_zone_id
    import aws_sdk_s3files.types.aws_account_id
    import aws_sdk_s3files.types.file_system_id
    import aws_sdk_s3files.types.ipv4_address
    import aws_sdk_s3files.types.ipv6_address
    import aws_sdk_s3files.types.life_cycle_state
    import aws_sdk_s3files.types.mount_target_id
    import aws_sdk_s3files.types.network_interface_id
    import aws_sdk_s3files.types.status_message
    import aws_sdk_s3files.types.subnet_id
    import aws_sdk_s3files.types.vpc_id


class ListMountTargetsDescription(TypedDict, closed=True):
    availability_zone_id: NotRequired[
        "aws_sdk_s3files.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The Availability Zone ID where the mount target is located.</p>"""
    file_system_id: NotRequired["aws_sdk_s3files.types.file_system_id.FileSystemId"]
    """<p>The ID of the S3 File System.</p>"""
    ipv4_address: NotRequired["aws_sdk_s3files.types.ipv4_address.Ipv4Address"]
    """<p>The IPv4 address of the mount target.</p>"""
    ipv6_address: NotRequired["aws_sdk_s3files.types.ipv6_address.Ipv6Address"]
    """<p>The IPv6 address of the mount target.</p>"""
    status: NotRequired["aws_sdk_s3files.types.life_cycle_state.LifeCycleState"]
    """<p>The current status of the mount target.</p>"""
    status_message: NotRequired["aws_sdk_s3files.types.status_message.StatusMessage"]
    """<p>Additional information about the mount target status.</p>"""
    mount_target_id: "aws_sdk_s3files.types.mount_target_id.MountTargetId"
    """<p>The ID of the mount target.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_s3files.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface associated with the mount target.</p>"""
    owner_id: "aws_sdk_s3files.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID of the mount target owner.</p>"""
    subnet_id: "aws_sdk_s3files.types.subnet_id.SubnetId"
    """<p>The ID of the subnet where the mount target is located.</p>"""
    vpc_id: NotRequired["aws_sdk_s3files.types.vpc_id.VpcId"]
    """<p>The ID of the VPC where the mount target is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMountTargetsDescription) -> dict:
    out: dict = {}
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "file_system_id" in value:
        out["fileSystemId"] = value["file_system_id"]
    if "ipv4_address" in value:
        out["ipv4Address"] = value["ipv4_address"]
    if "ipv6_address" in value:
        out["ipv6Address"] = value["ipv6_address"]
    if "status" in value:
        import aws_sdk_s3files.types.life_cycle_state

        out["status"] = aws_sdk_s3files.types.life_cycle_state.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    out["mountTargetId"] = value["mount_target_id"]
    if "network_interface_id" in value:
        out["networkInterfaceId"] = value["network_interface_id"]
    out["ownerId"] = value["owner_id"]
    out["subnetId"] = value["subnet_id"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> ListMountTargetsDescription:
    out: ListMountTargetsDescription = {}  # type: ignore[typeddict-item]
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if "fileSystemId" in data:
        out["file_system_id"] = data["fileSystemId"]
    if "ipv4Address" in data:
        out["ipv4_address"] = data["ipv4Address"]
    if "ipv6Address" in data:
        out["ipv6_address"] = data["ipv6Address"]
    if "status" in data:
        import aws_sdk_s3files.types.life_cycle_state

        out["status"] = aws_sdk_s3files.types.life_cycle_state.deserialize_json(
            data["status"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "mountTargetId" in data:
        out["mount_target_id"] = data["mountTargetId"]
    else:
        raise DeserializationError(
            "ListMountTargetsDescription.mount_target_id required"
        )
    if "networkInterfaceId" in data:
        out["network_interface_id"] = data["networkInterfaceId"]
    if "ownerId" in data:
        out["owner_id"] = data["ownerId"]
    else:
        raise DeserializationError("ListMountTargetsDescription.owner_id required")
    if "subnetId" in data:
        out["subnet_id"] = data["subnetId"]
    else:
        raise DeserializationError("ListMountTargetsDescription.subnet_id required")
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    return out
