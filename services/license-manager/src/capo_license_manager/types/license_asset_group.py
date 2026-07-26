"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.date_time
    import capo_license_manager.types.license_asset_group_configuration_list
    import capo_license_manager.types.license_asset_group_property_list
    import capo_license_manager.types.license_asset_group_status
    import capo_license_manager.types.license_asset_ruleset_arn_list
    import capo_license_manager.types.string


class LicenseAssetGroup(TypedDict, closed=True):
    name: "capo_license_manager.types.string.String"
    """<p>License asset group name.</p>"""
    description: NotRequired["capo_license_manager.types.string.String"]
    """<p>License asset group description.</p>"""
    license_asset_group_configurations: NotRequired[
        "capo_license_manager.types.license_asset_group_configuration_list.LicenseAssetGroupConfigurationList"
    ]
    """<p>License asset group configurations.</p>"""
    associated_license_asset_ruleset_ar_ns: "capo_license_manager.types.license_asset_ruleset_arn_list.LicenseAssetRulesetArnList"
    """<p>ARNs of associated license asset rulesets.</p>"""
    properties: NotRequired[
        "capo_license_manager.types.license_asset_group_property_list.LicenseAssetGroupPropertyList"
    ]
    """<p>License asset group properties.</p>"""
    license_asset_group_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license asset group.</p>"""
    status: (
        "capo_license_manager.types.license_asset_group_status.LicenseAssetGroupStatus"
    )
    """<p>License asset group status.</p>"""
    status_message: NotRequired["capo_license_manager.types.string.String"]
    """<p>License asset group status message.</p>"""
    latest_usage_analysis_time: NotRequired[
        "capo_license_manager.types.date_time.DateTime"
    ]
    """<p>Latest usage analysis time.</p>"""
    latest_resource_discovery_time: NotRequired[
        "capo_license_manager.types.date_time.DateTime"
    ]
    """<p>Latest resource discovery time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetGroup) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "license_asset_group_configurations" in value:
        import capo_license_manager.types.license_asset_group_configuration_list

        out["LicenseAssetGroupConfigurations"] = (
            capo_license_manager.types.license_asset_group_configuration_list.serialize_aws_json_1_1(
                value["license_asset_group_configurations"]
            )
        )
    import capo_license_manager.types.license_asset_ruleset_arn_list

    out["AssociatedLicenseAssetRulesetARNs"] = (
        capo_license_manager.types.license_asset_ruleset_arn_list.serialize_aws_json_1_1(
            value["associated_license_asset_ruleset_ar_ns"]
        )
    )
    if "properties" in value:
        import capo_license_manager.types.license_asset_group_property_list

        out["Properties"] = (
            capo_license_manager.types.license_asset_group_property_list.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    out["LicenseAssetGroupArn"] = value["license_asset_group_arn"]
    import capo_license_manager.types.license_asset_group_status

    out["Status"] = (
        capo_license_manager.types.license_asset_group_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "latest_usage_analysis_time" in value:
        import capo_license_manager.types.date_time

        out["LatestUsageAnalysisTime"] = (
            capo_license_manager.types.date_time.serialize_aws_json_1_1(
                value["latest_usage_analysis_time"]
            )
        )
    if "latest_resource_discovery_time" in value:
        import capo_license_manager.types.date_time

        out["LatestResourceDiscoveryTime"] = (
            capo_license_manager.types.date_time.serialize_aws_json_1_1(
                value["latest_resource_discovery_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseAssetGroup:
    out: LicenseAssetGroup = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("LicenseAssetGroup.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "LicenseAssetGroupConfigurations" in data:
        import capo_license_manager.types.license_asset_group_configuration_list

        out["license_asset_group_configurations"] = (
            capo_license_manager.types.license_asset_group_configuration_list.deserialize_aws_json_1_1(
                data["LicenseAssetGroupConfigurations"]
            )
        )
    if "AssociatedLicenseAssetRulesetARNs" in data:
        import capo_license_manager.types.license_asset_ruleset_arn_list

        out["associated_license_asset_ruleset_ar_ns"] = (
            capo_license_manager.types.license_asset_ruleset_arn_list.deserialize_aws_json_1_1(
                data["AssociatedLicenseAssetRulesetARNs"]
            )
        )
    else:
        raise DeserializationError(
            "LicenseAssetGroup.associated_license_asset_ruleset_ar_ns required"
        )
    if "Properties" in data:
        import capo_license_manager.types.license_asset_group_property_list

        out["properties"] = (
            capo_license_manager.types.license_asset_group_property_list.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if "LicenseAssetGroupArn" in data:
        out["license_asset_group_arn"] = data["LicenseAssetGroupArn"]
    else:
        raise DeserializationError("LicenseAssetGroup.license_asset_group_arn required")
    if "Status" in data:
        import capo_license_manager.types.license_asset_group_status

        out["status"] = (
            capo_license_manager.types.license_asset_group_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("LicenseAssetGroup.status required")
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "LatestUsageAnalysisTime" in data:
        import capo_license_manager.types.date_time

        out["latest_usage_analysis_time"] = (
            capo_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["LatestUsageAnalysisTime"]
            )
        )
    if "LatestResourceDiscoveryTime" in data:
        import capo_license_manager.types.date_time

        out["latest_resource_discovery_time"] = (
            capo_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["LatestResourceDiscoveryTime"]
            )
        )
    return out
