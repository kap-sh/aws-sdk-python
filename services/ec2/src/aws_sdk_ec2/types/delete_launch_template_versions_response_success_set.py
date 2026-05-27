"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplateVersionsResponseSuccessSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_launch_template_versions_response_success_item

DeleteLaunchTemplateVersionsResponseSuccessSet: TypeAlias = list[
    "aws_sdk_ec2.types.delete_launch_template_versions_response_success_item.DeleteLaunchTemplateVersionsResponseSuccessItem"
]
