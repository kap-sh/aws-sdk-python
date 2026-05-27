"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_launch_template_overrides_list
    import aws_sdk_ec2.types.fleet_launch_template_specification


class FleetLaunchTemplateConfig(TypedDict):
    launch_template_specification: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_specification.FleetLaunchTemplateSpecification"
    ]
    """<p>The launch template.</p>"""
    overrides: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_overrides_list.FleetLaunchTemplateOverridesList"
    ]
    """<p>Any parameters that you specify override the same parameters in the launch template.</p>"""
