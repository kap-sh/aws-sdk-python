"""Generated from Smithy shape ``com.amazonaws.ec2#FastLaunchLaunchTemplateSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_id
    import aws_sdk_ec2.types.string


class FastLaunchLaunchTemplateSpecificationRequest(TypedDict):
    launch_template_id: NotRequired[
        "aws_sdk_ec2.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>Specify the ID of the launch template that the AMI should use for Windows fast launch.</p>"""
    launch_template_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specify the name of the launch template that the AMI should use for Windows fast launch.</p>"""
    version: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specify the version of the launch template that the AMI should use for Windows fast launch.</p>"""
