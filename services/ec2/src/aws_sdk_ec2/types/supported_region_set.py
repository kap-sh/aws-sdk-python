"""Generated from Smithy shape ``com.amazonaws.ec2#SupportedRegionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.supported_region_detail

SupportedRegionSet: TypeAlias = list[
    "aws_sdk_ec2.types.supported_region_detail.SupportedRegionDetail"
]
