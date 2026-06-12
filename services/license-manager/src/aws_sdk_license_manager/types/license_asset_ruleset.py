"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetRuleset``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn
    import aws_sdk_license_manager.types.license_asset_rule_list
    import aws_sdk_license_manager.types.string


class LicenseAssetRuleset(TypedDict):
    name: "aws_sdk_license_manager.types.string.String"
    """<p>License asset ruleset name.</p>"""
    description: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>License asset ruleset description.</p>"""
    rules: "aws_sdk_license_manager.types.license_asset_rule_list.LicenseAssetRuleList"
    """<p>License asset rules.</p>"""
    license_asset_ruleset_arn: "aws_sdk_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license asset ruleset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetRuleset) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_license_manager.types.license_asset_rule_list

    out["Rules"] = (
        aws_sdk_license_manager.types.license_asset_rule_list.serialize_aws_json_1_1(
            value["rules"]
        )
    )
    out["LicenseAssetRulesetArn"] = value["license_asset_ruleset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseAssetRuleset:
    out: LicenseAssetRuleset = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("LicenseAssetRuleset.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Rules" in data:
        import aws_sdk_license_manager.types.license_asset_rule_list

        out["rules"] = (
            aws_sdk_license_manager.types.license_asset_rule_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    else:
        raise DeserializationError("LicenseAssetRuleset.rules required")
    if "LicenseAssetRulesetArn" in data:
        out["license_asset_ruleset_arn"] = data["LicenseAssetRulesetArn"]
    else:
        raise DeserializationError(
            "LicenseAssetRuleset.license_asset_ruleset_arn required"
        )
    return out
