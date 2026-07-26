"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetRulesetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.license_asset_ruleset

LicenseAssetRulesetList: TypeAlias = list[
    "capo_license_manager.types.license_asset_ruleset.LicenseAssetRuleset"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetRulesetList) -> list:
    import capo_license_manager.types.license_asset_ruleset

    out: list = []
    for item in value:
        out.append(
            capo_license_manager.types.license_asset_ruleset.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LicenseAssetRulesetList:
    import capo_license_manager.types.license_asset_ruleset

    out: LicenseAssetRulesetList = []
    for item in data:
        out.append(
            capo_license_manager.types.license_asset_ruleset.deserialize_aws_json_1_1(
                item
            )
        )
    return out
