"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_config

LaunchTemplateConfigList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_config.LaunchTemplateConfig"
]
