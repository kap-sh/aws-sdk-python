"""Generated from Smithy shape ``com.amazonaws.ec2#BandwidthWeightingTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.bandwidth_weighting_type

BandwidthWeightingTypeList: TypeAlias = list[
    "aws_sdk_ec2.types.bandwidth_weighting_type.BandwidthWeightingType"
]
