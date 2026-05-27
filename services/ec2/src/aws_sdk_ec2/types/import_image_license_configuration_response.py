"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageLicenseConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ImportImageLicenseConfigurationResponse(TypedDict):
    license_configuration_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of a license configuration.</p>"""
