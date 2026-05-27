"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateOverridesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_launch_template_overrides

FleetLaunchTemplateOverridesList: TypeAlias = list[
    "aws_sdk_ec2.types.fleet_launch_template_overrides.FleetLaunchTemplateOverrides"
]
