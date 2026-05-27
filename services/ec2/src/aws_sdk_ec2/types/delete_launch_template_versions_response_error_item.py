"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplateVersionsResponseErrorItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.response_error
    import aws_sdk_ec2.types.string


class DeleteLaunchTemplateVersionsResponseErrorItem(TypedDict):
    launch_template_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the launch template.</p>"""
    launch_template_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the launch template.</p>"""
    version_number: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The version number of the launch template.</p>"""
    response_error: NotRequired["aws_sdk_ec2.types.response_error.ResponseError"]
    """<p>Information about the error.</p>"""
