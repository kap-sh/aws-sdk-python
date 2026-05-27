"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_launch_template_specification
    import aws_sdk_ec2.types.launch_template_overrides_list


class LaunchTemplateConfig(TypedDict):
    launch_template_specification: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_specification.FleetLaunchTemplateSpecification"
    ]
    """<p>The launch template to use. Make sure that the launch template does not contain the <code>NetworkInterfaceId</code> parameter because you can't specify a network interface ID in a Spot Fleet.</p>"""
    overrides: NotRequired[
        "aws_sdk_ec2.types.launch_template_overrides_list.LaunchTemplateOverridesList"
    ]
    """<p>Any parameters that you specify override the same parameters in the launch template.</p>"""
