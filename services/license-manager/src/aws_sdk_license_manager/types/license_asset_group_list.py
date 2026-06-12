"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_asset_group

LicenseAssetGroupList: TypeAlias = list[
    "aws_sdk_license_manager.types.license_asset_group.LicenseAssetGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetGroupList) -> list:
    import aws_sdk_license_manager.types.license_asset_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.license_asset_group.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LicenseAssetGroupList:
    import aws_sdk_license_manager.types.license_asset_group

    out: LicenseAssetGroupList = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.license_asset_group.deserialize_aws_json_1_1(
                item
            )
        )
    return out
