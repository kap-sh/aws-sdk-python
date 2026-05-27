"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateVersionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_version

LaunchTemplateVersionSet: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_version.LaunchTemplateVersion"
]
