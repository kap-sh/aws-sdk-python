"""Generated from Smithy shape ``com.amazonaws.licensemanager#UpdateServiceSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.box_boolean
    import aws_sdk_license_manager.types.organization_configuration
    import aws_sdk_license_manager.types.string
    import aws_sdk_license_manager.types.string_list


class UpdateServiceSettingsRequest(TypedDict):
    s3_bucket_arn: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the Amazon S3 bucket where the License Manager information is stored.</p>"""
    sns_topic_arn: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the Amazon SNS topic used for License Manager alerts.</p>"""
    organization_configuration: NotRequired[
        "aws_sdk_license_manager.types.organization_configuration.OrganizationConfiguration"
    ]
    """<p>Enables integration with Organizations for cross-account discovery.</p>"""
    enable_cross_accounts_discovery: NotRequired[
        "aws_sdk_license_manager.types.box_boolean.BoxBoolean"
    ]
    """<p>Activates cross-account discovery.</p>"""
    enabled_discovery_source_regions: NotRequired[
        "aws_sdk_license_manager.types.string_list.StringList"
    ]
    """<p>Cross region discovery enabled source regions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateServiceSettingsRequest) -> dict:
    out: dict = {}
    if "s3_bucket_arn" in value:
        out["S3BucketArn"] = value["s3_bucket_arn"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "organization_configuration" in value:
        import aws_sdk_license_manager.types.organization_configuration

        out["OrganizationConfiguration"] = (
            aws_sdk_license_manager.types.organization_configuration.serialize_aws_json_1_1(
                value["organization_configuration"]
            )
        )
    if "enable_cross_accounts_discovery" in value:
        out["EnableCrossAccountsDiscovery"] = value["enable_cross_accounts_discovery"]
    if "enabled_discovery_source_regions" in value:
        import aws_sdk_license_manager.types.string_list

        out["EnabledDiscoverySourceRegions"] = (
            aws_sdk_license_manager.types.string_list.serialize_aws_json_1_1(
                value["enabled_discovery_source_regions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateServiceSettingsRequest:
    out: UpdateServiceSettingsRequest = {}  # type: ignore[typeddict-item]
    if "S3BucketArn" in data:
        out["s3_bucket_arn"] = data["S3BucketArn"]
    if "SnsTopicArn" in data:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if "OrganizationConfiguration" in data:
        import aws_sdk_license_manager.types.organization_configuration

        out["organization_configuration"] = (
            aws_sdk_license_manager.types.organization_configuration.deserialize_aws_json_1_1(
                data["OrganizationConfiguration"]
            )
        )
    if "EnableCrossAccountsDiscovery" in data:
        out["enable_cross_accounts_discovery"] = data["EnableCrossAccountsDiscovery"]
    if "EnabledDiscoverySourceRegions" in data:
        import aws_sdk_license_manager.types.string_list

        out["enabled_discovery_source_regions"] = (
            aws_sdk_license_manager.types.string_list.deserialize_aws_json_1_1(
                data["EnabledDiscoverySourceRegions"]
            )
        )
    return out
