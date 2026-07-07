"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseAssetRulesetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_asset_ruleset


class GetLicenseAssetRulesetResponse(TypedDict, closed=True):
    license_asset_ruleset: (
        "aws_sdk_license_manager.types.license_asset_ruleset.LicenseAssetRuleset"
    )
    """<p>License asset ruleset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseAssetRulesetResponse) -> dict:
    out: dict = {}
    import aws_sdk_license_manager.types.license_asset_ruleset

    out["LicenseAssetRuleset"] = (
        aws_sdk_license_manager.types.license_asset_ruleset.serialize_aws_json_1_1(
            value["license_asset_ruleset"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseAssetRulesetResponse:
    out: GetLicenseAssetRulesetResponse = {}  # type: ignore[typeddict-item]
    if "LicenseAssetRuleset" in data:
        import aws_sdk_license_manager.types.license_asset_ruleset

        out["license_asset_ruleset"] = (
            aws_sdk_license_manager.types.license_asset_ruleset.deserialize_aws_json_1_1(
                data["LicenseAssetRuleset"]
            )
        )
    else:
        raise DeserializationError(
            "GetLicenseAssetRulesetResponse.license_asset_ruleset required"
        )
    return out
