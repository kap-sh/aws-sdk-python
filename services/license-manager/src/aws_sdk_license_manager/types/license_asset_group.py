"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn
    import aws_sdk_license_manager.types.date_time
    import aws_sdk_license_manager.types.license_asset_group_configuration_list
    import aws_sdk_license_manager.types.license_asset_group_property_list
    import aws_sdk_license_manager.types.license_asset_group_status
    import aws_sdk_license_manager.types.license_asset_ruleset_arn_list
    import aws_sdk_license_manager.types.string


class LicenseAssetGroup(TypedDict, closed=True):
    name: "aws_sdk_license_manager.types.string.String"
    """<p>License asset group name.</p>"""
    description: NotRequired["aws_sdk_license_manager.types.string.String"]
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
    status: "aws_sdk_license_manager.types.license_asset_group_status.LicenseAssetGroupStatus"
    """<p>License asset group status.</p>"""
    status_message: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>License asset group status message.</p>"""
    latest_usage_analysis_time: NotRequired[
        "aws_sdk_license_manager.types.date_time.DateTime"
    ]
    """<p>Latest usage analysis time.</p>"""
    latest_resource_discovery_time: NotRequired[
        "aws_sdk_license_manager.types.date_time.DateTime"
    ]
    """<p>Latest resource discovery time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetGroup) -> dict:
    out: dict = {}
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
    import aws_sdk_license_manager.types.license_asset_group_status

    out["Status"] = (
        aws_sdk_license_manager.types.license_asset_group_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "latest_usage_analysis_time" in value:
        import aws_sdk_license_manager.types.date_time

        out["LatestUsageAnalysisTime"] = (
            aws_sdk_license_manager.types.date_time.serialize_aws_json_1_1(
                value["latest_usage_analysis_time"]
            )
        )
    if "latest_resource_discovery_time" in value:
        import aws_sdk_license_manager.types.date_time

        out["LatestResourceDiscoveryTime"] = (
            aws_sdk_license_manager.types.date_time.serialize_aws_json_1_1(
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
            "LicenseAssetGroup.associated_license_asset_ruleset_ar_ns required"
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
        raise DeserializationError("LicenseAssetGroup.license_asset_group_arn required")
    if "Status" in data:
        import aws_sdk_license_manager.types.license_asset_group_status

        out["status"] = (
            aws_sdk_license_manager.types.license_asset_group_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("LicenseAssetGroup.status required")
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "LatestUsageAnalysisTime" in data:
        import aws_sdk_license_manager.types.date_time

        out["latest_usage_analysis_time"] = (
            aws_sdk_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["LatestUsageAnalysisTime"]
            )
        )
    if "LatestResourceDiscoveryTime" in data:
        import aws_sdk_license_manager.types.date_time

        out["latest_resource_discovery_time"] = (
            aws_sdk_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["LatestResourceDiscoveryTime"]
            )
        )
    return out
