"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetGroupConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_asset_group_configuration

LicenseAssetGroupConfigurationList: TypeAlias = list[
    "aws_sdk_license_manager.types.license_asset_group_configuration.LicenseAssetGroupConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetGroupConfigurationList) -> list:
    import aws_sdk_license_manager.types.license_asset_group_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.license_asset_group_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LicenseAssetGroupConfigurationList:
    import aws_sdk_license_manager.types.license_asset_group_configuration

    out: LicenseAssetGroupConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.license_asset_group_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
