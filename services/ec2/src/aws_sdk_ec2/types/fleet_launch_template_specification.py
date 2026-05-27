"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_name
    import aws_sdk_ec2.types.string


class FleetLaunchTemplateSpecification(TypedDict):
    launch_template_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the launch template.</p> <p>You must specify the <code>LaunchTemplateId</code> or the <code>LaunchTemplateName</code>, but not both.</p>"""
    launch_template_name: NotRequired[
        "aws_sdk_ec2.types.launch_template_name.LaunchTemplateName"
    ]
    """<p>The name of the launch template.</p> <p>You must specify the <code>LaunchTemplateName</code> or the <code>LaunchTemplateId</code>, but not both.</p>"""
    version: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The launch template version number, <code>$Latest</code>, or <code>$Default</code>. You must specify a value, otherwise the request fails.</p> <p>If the value is <code>$Latest</code>, Amazon EC2 uses the latest version of the launch template.</p> <p>If the value is <code>$Default</code>, Amazon EC2 uses the default version of the launch template.</p>"""
