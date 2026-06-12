"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConfigurationUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_configuration_usage

LicenseConfigurationUsageList: TypeAlias = list[
    "aws_sdk_license_manager.types.license_configuration_usage.LicenseConfigurationUsage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseConfigurationUsageList) -> list:
    import aws_sdk_license_manager.types.license_configuration_usage

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.license_configuration_usage.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LicenseConfigurationUsageList:
    import aws_sdk_license_manager.types.license_configuration_usage

    out: LicenseConfigurationUsageList = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.license_configuration_usage.deserialize_aws_json_1_1(
                item
            )
        )
    return out
