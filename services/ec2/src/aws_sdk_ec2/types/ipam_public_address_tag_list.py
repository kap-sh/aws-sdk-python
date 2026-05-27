"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_public_address_tag

IpamPublicAddressTagList: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_public_address_tag.IpamPublicAddressTag"
]
