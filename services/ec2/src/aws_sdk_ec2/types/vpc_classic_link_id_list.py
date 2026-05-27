"""Generated from Smithy shape ``com.amazonaws.ec2#VpcClassicLinkIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_id

VpcClassicLinkIdList: TypeAlias = list["aws_sdk_ec2.types.vpc_id.VpcId"]
