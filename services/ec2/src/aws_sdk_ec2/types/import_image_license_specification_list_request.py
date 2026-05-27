"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageLicenseSpecificationListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_image_license_configuration_request

ImportImageLicenseSpecificationListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.import_image_license_configuration_request.ImportImageLicenseConfigurationRequest"
]
