"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateTagSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_tag_specification

LaunchTemplateTagSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_tag_specification.LaunchTemplateTagSpecification"
]
