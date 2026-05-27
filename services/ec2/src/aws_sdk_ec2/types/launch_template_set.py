"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template

LaunchTemplateSet: TypeAlias = list["aws_sdk_ec2.types.launch_template.LaunchTemplate"]
