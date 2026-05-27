"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLaunchTemplateResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template
    import aws_sdk_ec2.types.validation_warning


class CreateLaunchTemplateResult(TypedDict):
    launch_template: NotRequired["aws_sdk_ec2.types.launch_template.LaunchTemplate"]
    """<p>Information about the launch template.</p>"""
    warning: NotRequired["aws_sdk_ec2.types.validation_warning.ValidationWarning"]
    """<p>If the launch template contains parameters or parameter combinations that are not valid, an error code and an error message are returned for each issue that's found.</p>"""
