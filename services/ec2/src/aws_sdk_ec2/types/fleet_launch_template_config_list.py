"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_launch_template_config

FleetLaunchTemplateConfigList: TypeAlias = list[
    "aws_sdk_ec2.types.fleet_launch_template_config.FleetLaunchTemplateConfig"
]
