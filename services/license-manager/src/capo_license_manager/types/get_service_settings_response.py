"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetServiceSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.box_boolean
    import capo_license_manager.types.organization_configuration
    import capo_license_manager.types.service_status
    import capo_license_manager.types.string
    import capo_license_manager.types.string_list


class GetServiceSettingsResponse(TypedDict, closed=True):
    s3_bucket_arn: NotRequired["capo_license_manager.types.string.String"]
    """<p>Regional S3 bucket path for storing reports, license trail event data, discovery data, and so on.</p>"""
    sns_topic_arn: NotRequired["capo_license_manager.types.string.String"]
    """<p>SNS topic configured to receive notifications from License Manager.</p>"""
    organization_configuration: NotRequired[
        "capo_license_manager.types.organization_configuration.OrganizationConfiguration"
    ]
    """<p>Indicates whether Organizations is integrated with License Manager for cross-account discovery.</p>"""
    enable_cross_accounts_discovery: NotRequired[
        "capo_license_manager.types.box_boolean.BoxBoolean"
    ]
    """<p>Indicates whether cross-account discovery is enabled.</p>"""
    license_manager_resource_share_arn: NotRequired[
        "capo_license_manager.types.string.String"
    ]
    """<p>Amazon Resource Name (ARN) of the resource share. The License Manager management account provides member accounts with access to this share.</p>"""
    cross_region_discovery_home_region: NotRequired[
        "capo_license_manager.types.string.String"
    ]
    """<p>Cross region discovery home region.</p>"""
    cross_region_discovery_source_regions: NotRequired[
        "capo_license_manager.types.string_list.StringList"
    ]
    """<p>Cross region discovery source regions.</p>"""
    service_status: NotRequired[
        "capo_license_manager.types.service_status.ServiceStatus"
    ]
    """<p>Service status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetServiceSettingsResponse) -> dict:
    out: dict = {}
    if "s3_bucket_arn" in value:
        out["S3BucketArn"] = value["s3_bucket_arn"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "organization_configuration" in value:
        import capo_license_manager.types.organization_configuration

        out["OrganizationConfiguration"] = (
            capo_license_manager.types.organization_configuration.serialize_aws_json_1_1(
                value["organization_configuration"]
            )
        )
    if "enable_cross_accounts_discovery" in value:
        out["EnableCrossAccountsDiscovery"] = value["enable_cross_accounts_discovery"]
    if "license_manager_resource_share_arn" in value:
        out["LicenseManagerResourceShareArn"] = value[
            "license_manager_resource_share_arn"
        ]
    if "cross_region_discovery_home_region" in value:
        out["CrossRegionDiscoveryHomeRegion"] = value[
            "cross_region_discovery_home_region"
        ]
    if "cross_region_discovery_source_regions" in value:
        import capo_license_manager.types.string_list

        out["CrossRegionDiscoverySourceRegions"] = (
            capo_license_manager.types.string_list.serialize_aws_json_1_1(
                value["cross_region_discovery_source_regions"]
            )
        )
    if "service_status" in value:
        import capo_license_manager.types.service_status

        out["ServiceStatus"] = (
            capo_license_manager.types.service_status.serialize_aws_json_1_1(
                value["service_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetServiceSettingsResponse:
    out: GetServiceSettingsResponse = {}  # type: ignore[typeddict-item]
    if "S3BucketArn" in data:
        out["s3_bucket_arn"] = data["S3BucketArn"]
    if "SnsTopicArn" in data:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if "OrganizationConfiguration" in data:
        import capo_license_manager.types.organization_configuration

        out["organization_configuration"] = (
            capo_license_manager.types.organization_configuration.deserialize_aws_json_1_1(
                data["OrganizationConfiguration"]
            )
        )
    if "EnableCrossAccountsDiscovery" in data:
        out["enable_cross_accounts_discovery"] = data["EnableCrossAccountsDiscovery"]
    if "LicenseManagerResourceShareArn" in data:
        out["license_manager_resource_share_arn"] = data[
            "LicenseManagerResourceShareArn"
        ]
    if "CrossRegionDiscoveryHomeRegion" in data:
        out["cross_region_discovery_home_region"] = data[
            "CrossRegionDiscoveryHomeRegion"
        ]
    if "CrossRegionDiscoverySourceRegions" in data:
        import capo_license_manager.types.string_list

        out["cross_region_discovery_source_regions"] = (
            capo_license_manager.types.string_list.deserialize_aws_json_1_1(
                data["CrossRegionDiscoverySourceRegions"]
            )
        )
    if "ServiceStatus" in data:
        import capo_license_manager.types.service_status

        out["service_status"] = (
            capo_license_manager.types.service_status.deserialize_aws_json_1_1(
                data["ServiceStatus"]
            )
        )
    return out
