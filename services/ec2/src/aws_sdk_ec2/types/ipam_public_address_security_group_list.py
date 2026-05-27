"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressSecurityGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_public_address_security_group

IpamPublicAddressSecurityGroupList: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_public_address_security_group.IpamPublicAddressSecurityGroup"
]
