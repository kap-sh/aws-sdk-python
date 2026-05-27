"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateLicenseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_license_configuration

LaunchTemplateLicenseList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_license_configuration.LaunchTemplateLicenseConfiguration"
]
