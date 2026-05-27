"""Generated from Smithy shape ``com.amazonaws.ec2#ResponseError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_error_code
    import aws_sdk_ec2.types.string


class ResponseError(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.launch_template_error_code.LaunchTemplateErrorCode"
    ]
    """<p>The error code.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The error message, if applicable.</p>"""
