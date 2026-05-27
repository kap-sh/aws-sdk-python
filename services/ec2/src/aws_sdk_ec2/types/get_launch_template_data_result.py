"""Generated from Smithy shape ``com.amazonaws.ec2#GetLaunchTemplateDataResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.response_launch_template_data


class GetLaunchTemplateDataResult(TypedDict):
    launch_template_data: NotRequired[
        "aws_sdk_ec2.types.response_launch_template_data.ResponseLaunchTemplateData"
    ]
    """<p>The instance data.</p>"""
