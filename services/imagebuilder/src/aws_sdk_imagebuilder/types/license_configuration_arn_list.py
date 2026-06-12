"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LicenseConfigurationArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.license_configuration_arn

LicenseConfigurationArnList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.license_configuration_arn.LicenseConfigurationArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: LicenseConfigurationArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> LicenseConfigurationArnList:
    return list(data)
