"""Generated from Smithy shape ``com.amazonaws.ec2#CidrBlockSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cidr_block

CidrBlockSet: TypeAlias = list["aws_sdk_ec2.types.cidr_block.CidrBlock"]
