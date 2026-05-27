"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateTagSpecificationRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_tag_specification_request

LaunchTemplateTagSpecificationRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_tag_specification_request.LaunchTemplateTagSpecificationRequest"
]
