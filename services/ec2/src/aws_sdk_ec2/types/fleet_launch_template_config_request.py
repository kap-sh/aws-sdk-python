"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_launch_template_overrides_list_request
    import aws_sdk_ec2.types.fleet_launch_template_specification_request


class FleetLaunchTemplateConfigRequest(TypedDict):
    launch_template_specification: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_specification_request.FleetLaunchTemplateSpecificationRequest"
    ]
    """<p>The launch template to use. You must specify either the launch template ID or launch template name in the request. </p>"""
    overrides: NotRequired[
        "aws_sdk_ec2.types.fleet_launch_template_overrides_list_request.FleetLaunchTemplateOverridesListRequest"
    ]
    """<p>Any parameters that you specify override the same parameters in the launch template.</p> <p>For fleets of type <code>request</code> and <code>maintain</code>, a maximum of 300 items is allowed across all launch templates.</p>"""
