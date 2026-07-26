"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConfigurationUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.license_configuration_usage

LicenseConfigurationUsageList: TypeAlias = list[
    "capo_license_manager.types.license_configuration_usage.LicenseConfigurationUsage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseConfigurationUsageList) -> list:
    import capo_license_manager.types.license_configuration_usage

    out: list = []
    for item in value:
        out.append(
            capo_license_manager.types.license_configuration_usage.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LicenseConfigurationUsageList:
    import capo_license_manager.types.license_configuration_usage

    out: LicenseConfigurationUsageList = []
    for item in data:
        out.append(
            capo_license_manager.types.license_configuration_usage.deserialize_aws_json_1_1(
                item
            )
        )
    return out
