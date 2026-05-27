"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_tag

IpamResourceTagList: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_resource_tag.IpamResourceTag"
]
