"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateOverridesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_overrides

LaunchTemplateOverridesList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_overrides.LaunchTemplateOverrides"
]
