"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListLicenseAssetRulesetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_asset_ruleset_list
    import aws_sdk_license_manager.types.string


class ListLicenseAssetRulesetsResponse(TypedDict, closed=True):
    license_asset_rulesets: NotRequired[
        "aws_sdk_license_manager.types.license_asset_ruleset_list.LicenseAssetRulesetList"
    ]
    """<p>License asset rulesets.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLicenseAssetRulesetsResponse) -> dict:
    out: dict = {}
    if "license_asset_rulesets" in value:
        import aws_sdk_license_manager.types.license_asset_ruleset_list

        out["LicenseAssetRulesets"] = (
            aws_sdk_license_manager.types.license_asset_ruleset_list.serialize_aws_json_1_1(
                value["license_asset_rulesets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLicenseAssetRulesetsResponse:
    out: ListLicenseAssetRulesetsResponse = {}  # type: ignore[typeddict-item]
    if "LicenseAssetRulesets" in data:
        import aws_sdk_license_manager.types.license_asset_ruleset_list

        out["license_asset_rulesets"] = (
            aws_sdk_license_manager.types.license_asset_ruleset_list.deserialize_aws_json_1_1(
                data["LicenseAssetRulesets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
