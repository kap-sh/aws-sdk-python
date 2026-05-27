"""Generated from Smithy shape ``com.amazonaws.ec2#VpcList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc

VpcList: TypeAlias = list["aws_sdk_ec2.types.vpc.Vpc"]
