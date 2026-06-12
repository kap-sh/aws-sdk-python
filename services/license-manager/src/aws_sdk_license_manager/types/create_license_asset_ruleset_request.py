"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseAssetRulesetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_asset_resource_description
    import aws_sdk_license_manager.types.license_asset_resource_name
    import aws_sdk_license_manager.types.license_asset_rule_list
    import aws_sdk_license_manager.types.string
    import aws_sdk_license_manager.types.tag_list


class CreateLicenseAssetRulesetRequest(TypedDict):
    name: "aws_sdk_license_manager.types.license_asset_resource_name.LicenseAssetResourceName"
    """<p>License asset ruleset name.</p>"""
    description: NotRequired[
        "aws_sdk_license_manager.types.license_asset_resource_description.LicenseAssetResourceDescription"
    ]
    """<p>License asset ruleset description.</p>"""
    rules: "aws_sdk_license_manager.types.license_asset_rule_list.LicenseAssetRuleList"
    """<p>License asset rules.</p>"""
    tags: NotRequired["aws_sdk_license_manager.types.tag_list.TagList"]
    """<p>Tags to add to the license asset ruleset.</p>"""
    client_token: "aws_sdk_license_manager.types.string.String"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseAssetRulesetRequest) -> dict:
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
    if "tags" in value:
        import aws_sdk_license_manager.types.tag_list

        out["Tags"] = aws_sdk_license_manager.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseAssetRulesetRequest:
    out: CreateLicenseAssetRulesetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateLicenseAssetRulesetRequest.name required")
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
        raise DeserializationError("CreateLicenseAssetRulesetRequest.rules required")
    if "Tags" in data:
        import aws_sdk_license_manager.types.tag_list

        out["tags"] = aws_sdk_license_manager.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "CreateLicenseAssetRulesetRequest.client_token required"
        )
    return out
