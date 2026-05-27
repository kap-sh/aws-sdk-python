"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateAndOverridesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_launch_template_overrides
    import aws_sdk_ec2.types.fleet_launch_template_specification


class LaunchTemplateAndOverridesResponse(TypedDict):
    launch_template_specification: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_specification.FleetLaunchTemplateSpecification"
    ]
    """<p>The launch template.</p>"""
    overrides: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_overrides.FleetLaunchTemplateOverrides"
    ]
    """<p>Any parameters that you specify override the same parameters in the launch template.</p>"""
