"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetTagSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_fleet_tag_specification

SpotFleetTagSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.spot_fleet_tag_specification.SpotFleetTagSpecification"
]
