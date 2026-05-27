"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyLaunchTemplateResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template


class ModifyLaunchTemplateResult(TypedDict):
    launch_template: NotRequired["aws_sdk_ec2.types.launch_template.LaunchTemplate"]
    """<p>Information about the launch template.</p>"""
