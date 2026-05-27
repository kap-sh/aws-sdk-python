"""Generated from Smithy shape ``com.amazonaws.ec2#VpcIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_id

VpcIdStringList: TypeAlias = list["aws_sdk_ec2.types.vpc_id.VpcId"]
