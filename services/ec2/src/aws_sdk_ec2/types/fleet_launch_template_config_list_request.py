"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateConfigListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_launch_template_config_request

FleetLaunchTemplateConfigListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.fleet_launch_template_config_request.FleetLaunchTemplateConfigRequest"
]
