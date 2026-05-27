"""Generated from Smithy shape ``com.amazonaws.ec2#RequestIpamResourceTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.request_ipam_resource_tag

RequestIpamResourceTagList: TypeAlias = list[
    "aws_sdk_ec2.types.request_ipam_resource_tag.RequestIpamResourceTag"
]
