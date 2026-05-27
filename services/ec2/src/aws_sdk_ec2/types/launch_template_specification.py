"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_id
    import aws_sdk_ec2.types.string


class LaunchTemplateSpecification(TypedDict):
    launch_template_id: NotRequired[
        "aws_sdk_ec2.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>The ID of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""
    launch_template_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""
    version: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The launch template version number, <code>$Latest</code>, or <code>$Default</code>.</p> <p>A value of <code>$Latest</code> uses the latest version of the launch template.</p> <p>A value of <code>$Default</code> uses the default version of the launch template.</p> <p>Default: The default version of the launch template.</p>"""
