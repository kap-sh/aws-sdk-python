"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplateVersionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_launch_template_versions_response_error_set
    import aws_sdk_ec2.types.delete_launch_template_versions_response_success_set


class DeleteLaunchTemplateVersionsResult(TypedDict):
    successfully_deleted_launch_template_versions: NotRequired[
        "aws_sdk_ec2.types.delete_launch_template_versions_response_success_set.DeleteLaunchTemplateVersionsResponseSuccessSet"
    ]
    """<p>Information about the launch template versions that were successfully deleted.</p>"""
    unsuccessfully_deleted_launch_template_versions: NotRequired[
        "aws_sdk_ec2.types.delete_launch_template_versions_response_error_set.DeleteLaunchTemplateVersionsResponseErrorSet"
    ]
    """<p>Information about the launch template versions that could not be deleted.</p>"""
