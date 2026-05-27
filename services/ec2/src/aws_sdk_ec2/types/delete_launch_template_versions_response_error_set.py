"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplateVersionsResponseErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_launch_template_versions_response_error_item

DeleteLaunchTemplateVersionsResponseErrorSet: TypeAlias = list[
    "aws_sdk_ec2.types.delete_launch_template_versions_response_error_item.DeleteLaunchTemplateVersionsResponseErrorItem"
]
