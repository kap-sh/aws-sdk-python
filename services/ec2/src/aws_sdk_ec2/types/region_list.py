"""Generated from Smithy shape ``com.amazonaws.ec2#RegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.region

RegionList: TypeAlias = list["aws_sdk_ec2.types.region.Region"]
