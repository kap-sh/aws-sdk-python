"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateLicenseSpecificationListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_license_configuration_request

LaunchTemplateLicenseSpecificationListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_license_configuration_request.LaunchTemplateLicenseConfigurationRequest"
]
