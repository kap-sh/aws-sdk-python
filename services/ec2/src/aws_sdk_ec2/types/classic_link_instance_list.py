"""Generated from Smithy shape ``com.amazonaws.ec2#ClassicLinkInstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.classic_link_instance

ClassicLinkInstanceList: TypeAlias = list[
    "aws_sdk_ec2.types.classic_link_instance.ClassicLinkInstance"
]
