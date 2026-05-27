"""Generated from Smithy shape ``com.amazonaws.ec2#NitroTpmSupportedVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nitro_tpm_supported_version_type

NitroTpmSupportedVersionsList: TypeAlias = list[
    "aws_sdk_ec2.types.nitro_tpm_supported_version_type.NitroTpmSupportedVersionType"
]
