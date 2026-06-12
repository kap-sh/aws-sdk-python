"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_configuration

LicenseConfigurations: TypeAlias = list[
    "aws_sdk_license_manager.types.license_configuration.LicenseConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseConfigurations) -> list:
    import aws_sdk_license_manager.types.license_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.license_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LicenseConfigurations:
    import aws_sdk_license_manager.types.license_configuration

    out: LicenseConfigurations = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.license_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
