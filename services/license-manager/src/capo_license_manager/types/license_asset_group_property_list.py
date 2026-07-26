"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetGroupPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.license_asset_group_property

LicenseAssetGroupPropertyList: TypeAlias = list[
    "capo_license_manager.types.license_asset_group_property.LicenseAssetGroupProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetGroupPropertyList) -> list:
    import capo_license_manager.types.license_asset_group_property

    out: list = []
    for item in value:
        out.append(
            capo_license_manager.types.license_asset_group_property.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LicenseAssetGroupPropertyList:
    import capo_license_manager.types.license_asset_group_property

    out: LicenseAssetGroupPropertyList = []
    for item in data:
        out.append(
            capo_license_manager.types.license_asset_group_property.deserialize_aws_json_1_1(
                item
            )
        )
    return out
