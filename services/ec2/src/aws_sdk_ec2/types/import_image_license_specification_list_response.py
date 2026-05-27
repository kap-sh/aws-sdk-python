"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageLicenseSpecificationListResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_image_license_configuration_response

ImportImageLicenseSpecificationListResponse: TypeAlias = list[
    "aws_sdk_ec2.types.import_image_license_configuration_response.ImportImageLicenseConfigurationResponse"
]
