"""Generated from Smithy shape ``com.amazonaws.licensemanager#UpdateLicenseAssetRulesetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.license_asset_resource_description
    import capo_license_manager.types.license_asset_resource_name
    import capo_license_manager.types.license_asset_rule_list
    import capo_license_manager.types.string


class UpdateLicenseAssetRulesetRequest(TypedDict, closed=True):
    name: NotRequired[
        "capo_license_manager.types.license_asset_resource_name.LicenseAssetResourceName"
    ]
    """<p>License asset ruleset name.</p>"""
    description: NotRequired[
        "capo_license_manager.types.license_asset_resource_description.LicenseAssetResourceDescription"
    ]
    """<p>License asset ruleset description.</p>"""
    rules: "capo_license_manager.types.license_asset_rule_list.LicenseAssetRuleList"
    """<p>License asset rules.</p>"""
    license_asset_ruleset_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license asset ruleset.</p>"""
    client_token: "capo_license_manager.types.string.String"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLicenseAssetRulesetRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_license_manager.types.license_asset_rule_list

    out["Rules"] = (
        capo_license_manager.types.license_asset_rule_list.serialize_aws_json_1_1(
            value["rules"]
        )
    )
    out["LicenseAssetRulesetArn"] = value["license_asset_ruleset_arn"]
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLicenseAssetRulesetRequest:
    out: UpdateLicenseAssetRulesetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Rules" in data:
        import capo_license_manager.types.license_asset_rule_list

        out["rules"] = (
            capo_license_manager.types.license_asset_rule_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    else:
        raise DeserializationError("UpdateLicenseAssetRulesetRequest.rules required")
    if "LicenseAssetRulesetArn" in data:
        out["license_asset_ruleset_arn"] = data["LicenseAssetRulesetArn"]
    else:
        raise DeserializationError(
            "UpdateLicenseAssetRulesetRequest.license_asset_ruleset_arn required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "UpdateLicenseAssetRulesetRequest.client_token required"
        )
    return out
