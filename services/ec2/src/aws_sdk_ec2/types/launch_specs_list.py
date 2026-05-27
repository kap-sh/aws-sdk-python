"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchSpecsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_fleet_launch_specification

LaunchSpecsList: TypeAlias = list[
    "aws_sdk_ec2.types.spot_fleet_launch_specification.SpotFleetLaunchSpecification"
]
