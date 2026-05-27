"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLaunchTemplateVersionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_version
    import aws_sdk_ec2.types.validation_warning


class CreateLaunchTemplateVersionResult(TypedDict):
    launch_template_version: NotRequired[
        "aws_sdk_ec2.types.launch_template_version.LaunchTemplateVersion"
    ]
    """<p>Information about the launch template version.</p>"""
    warning: NotRequired["aws_sdk_ec2.types.validation_warning.ValidationWarning"]
    """<p>If the new version of the launch template contains parameters or parameter combinations that are not valid, an error code and an error message are returned for each issue that's found.</p>"""
