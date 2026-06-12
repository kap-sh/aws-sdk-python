"""Generated from Smithy shape ``com.amazonaws.licensemanager#UpdateLicenseAssetGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn
    import aws_sdk_license_manager.types.license_asset_group_configuration_list
    import aws_sdk_license_manager.types.license_asset_group_property_list
    import aws_sdk_license_manager.types.license_asset_group_status
    import aws_sdk_license_manager.types.license_asset_resource_description
    import aws_sdk_license_manager.types.license_asset_resource_name
    import aws_sdk_license_manager.types.license_asset_ruleset_arn_list
    import aws_sdk_license_manager.types.string


class UpdateLicenseAssetGroupRequest(TypedDict):
    name: NotRequired[
        "aws_sdk_license_manager.types.license_asset_resource_name.LicenseAssetResourceName"
    ]
    """<p>License asset group name.</p>"""
    description: NotRequired[
        "aws_sdk_license_manager.types.license_asset_resource_description.LicenseAssetResourceDescription"
    ]
    """<p>License asset group description.</p>"""
    license_asset_group_configurations: NotRequired[
        "aws_sdk_license_manager.types.license_asset_group_configuration_list.LicenseAssetGroupConfigurationList"
    ]
    """<p>License asset group configurations.</p>"""
    associated_license_asset_ruleset_ar_ns: "aws_sdk_license_manager.types.license_asset_ruleset_arn_list.LicenseAssetRulesetArnList"
    """<p>ARNs of associated license asset rulesets.</p>"""
    properties: NotRequired[
        "aws_sdk_license_manager.types.license_asset_group_property_list.LicenseAssetGroupPropertyList"
    ]
    """<p>License asset group properties.</p>"""
    license_asset_group_arn: "aws_sdk_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license asset group.</p>"""
    status: NotRequired[
        "aws_sdk_license_manager.types.license_asset_group_status.LicenseAssetGroupStatus"
    ]
    """<p>License asset group status. The possible values are <code>ACTIVE</code> | <code>DISABLED</code>.</p>"""
    client_token: "aws_sdk_license_manager.types.string.String"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLicenseAssetGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "license_asset_group_configurations" in value:
        import aws_sdk_license_manager.types.license_asset_group_configuration_list

        out["LicenseAssetGroupConfigurations"] = (
            aws_sdk_license_manager.types.license_asset_group_configuration_list.serialize_aws_json_1_1(
                value["license_asset_group_configurations"]
            )
        )
    import aws_sdk_license_manager.types.license_asset_ruleset_arn_list

    out["AssociatedLicenseAssetRulesetARNs"] = (
        aws_sdk_license_manager.types.license_asset_ruleset_arn_list.serialize_aws_json_1_1(
            value["associated_license_asset_ruleset_ar_ns"]
        )
    )
    if "properties" in value:
        import aws_sdk_license_manager.types.license_asset_group_property_list

        out["Properties"] = (
            aws_sdk_license_manager.types.license_asset_group_property_list.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    out["LicenseAssetGroupArn"] = value["license_asset_group_arn"]
    if "status" in value:
        import aws_sdk_license_manager.types.license_asset_group_status

        out["Status"] = (
            aws_sdk_license_manager.types.license_asset_group_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLicenseAssetGroupRequest:
    out: UpdateLicenseAssetGroupRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LicenseAssetGroupConfigurations" in data:
        import aws_sdk_license_manager.types.license_asset_group_configuration_list

        out["license_asset_group_configurations"] = (
            aws_sdk_license_manager.types.license_asset_group_configuration_list.deserialize_aws_json_1_1(
                data["LicenseAssetGroupConfigurations"]
            )
        )
    if "AssociatedLicenseAssetRulesetARNs" in data:
        import aws_sdk_license_manager.types.license_asset_ruleset_arn_list

        out["associated_license_asset_ruleset_ar_ns"] = (
            aws_sdk_license_manager.types.license_asset_ruleset_arn_list.deserialize_aws_json_1_1(
                data["AssociatedLicenseAssetRulesetARNs"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLicenseAssetGroupRequest.associated_license_asset_ruleset_ar_ns required"
        )
    if "Properties" in data:
        import aws_sdk_license_manager.types.license_asset_group_property_list

        out["properties"] = (
            aws_sdk_license_manager.types.license_asset_group_property_list.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if "LicenseAssetGroupArn" in data:
        out["license_asset_group_arn"] = data["LicenseAssetGroupArn"]
    else:
        raise DeserializationError(
            "UpdateLicenseAssetGroupRequest.license_asset_group_arn required"
        )
    if "Status" in data:
        import aws_sdk_license_manager.types.license_asset_group_status

        out["status"] = (
            aws_sdk_license_manager.types.license_asset_group_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "UpdateLicenseAssetGroupRequest.client_token required"
        )
    return out
