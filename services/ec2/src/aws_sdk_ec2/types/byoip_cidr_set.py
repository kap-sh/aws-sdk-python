"""Generated from Smithy shape ``com.amazonaws.ec2#ByoipCidrSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.byoip_cidr

ByoipCidrSet: TypeAlias = list["aws_sdk_ec2.types.byoip_cidr.ByoipCidr"]
