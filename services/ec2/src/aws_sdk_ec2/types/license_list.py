"""Generated from Smithy shape ``com.amazonaws.ec2#LicenseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.license_configuration

LicenseList: TypeAlias = list[
    "aws_sdk_ec2.types.license_configuration.LicenseConfiguration"
]
