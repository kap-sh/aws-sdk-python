"""Generated from Smithy shape ``com.amazonaws.ec2#LicenseSpecificationListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.license_configuration_request

LicenseSpecificationListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.license_configuration_request.LicenseConfigurationRequest"
]
