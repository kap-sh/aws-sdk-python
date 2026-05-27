"""Generated from Smithy shape ``com.amazonaws.ec2#VpcClassicLinkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_classic_link

VpcClassicLinkList: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_classic_link.VpcClassicLink"
]
