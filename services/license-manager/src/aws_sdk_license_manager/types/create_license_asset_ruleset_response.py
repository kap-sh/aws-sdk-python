"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseAssetRulesetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string


class CreateLicenseAssetRulesetResponse(TypedDict, closed=True):
    license_asset_ruleset_arn: "aws_sdk_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the license asset ruleset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseAssetRulesetResponse) -> dict:
    out: dict = {}
    out["LicenseAssetRulesetArn"] = value["license_asset_ruleset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseAssetRulesetResponse:
    out: CreateLicenseAssetRulesetResponse = {}  # type: ignore[typeddict-item]
    if "LicenseAssetRulesetArn" in data:
        out["license_asset_ruleset_arn"] = data["LicenseAssetRulesetArn"]
    else:
        raise DeserializationError(
            "CreateLicenseAssetRulesetResponse.license_asset_ruleset_arn required"
        )
    return out
