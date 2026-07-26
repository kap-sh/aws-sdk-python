"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.license_asset_rule

LicenseAssetRuleList: TypeAlias = list[
    "capo_license_manager.types.license_asset_rule.LicenseAssetRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetRuleList) -> list:
    import capo_license_manager.types.license_asset_rule

    out: list = []
    for item in value:
        out.append(
            capo_license_manager.types.license_asset_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LicenseAssetRuleList:
    import capo_license_manager.types.license_asset_rule

    out: LicenseAssetRuleList = []
    for item in data:
        out.append(
            capo_license_manager.types.license_asset_rule.deserialize_aws_json_1_1(item)
        )
    return out
