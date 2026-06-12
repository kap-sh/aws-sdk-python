"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdatePartnerAppRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.client_token
    import aws_sdk_sagemaker.types.major_minor_version
    import aws_sdk_sagemaker.types.non_empty_string64
    import aws_sdk_sagemaker.types.partner_app_arn
    import aws_sdk_sagemaker.types.partner_app_config
    import aws_sdk_sagemaker.types.partner_app_maintenance_config
    import aws_sdk_sagemaker.types.tag_list


class UpdatePartnerAppRequest(TypedDict):
    arn: NotRequired["aws_sdk_sagemaker.types.partner_app_arn.PartnerAppArn"]
    """<p>The ARN of the SageMaker Partner AI App to update.</p>"""
    maintenance_config: NotRequired[
        "aws_sdk_sagemaker.types.partner_app_maintenance_config.PartnerAppMaintenanceConfig"
    ]
    """<p>Maintenance configuration settings for the SageMaker Partner AI App.</p>"""
    tier: NotRequired["aws_sdk_sagemaker.types.non_empty_string64.NonEmptyString64"]
    """<p>Indicates the instance type and size of the cluster attached to the SageMaker Partner AI App.</p>"""
    application_config: NotRequired[
        "aws_sdk_sagemaker.types.partner_app_config.PartnerAppConfig"
    ]
    """<p>Configuration settings for the SageMaker Partner AI App.</p>"""
    enable_iam_session_based_identity: NotRequired[
        "aws_sdk_sagemaker.types.boolean.Boolean"
    ]
    """<p>When set to <code>TRUE</code>, the SageMaker Partner AI App sets the Amazon Web Services IAM session name or the authenticated IAM user as the identity of the SageMaker Partner AI App user.</p>"""
    enable_auto_minor_version_upgrade: NotRequired[
        "aws_sdk_sagemaker.types.boolean.Boolean"
    ]
    """<p>When set to <code>TRUE</code>, the SageMaker Partner AI App is automatically upgraded to the latest minor version during the next scheduled maintenance window, if one is available.</p>"""
    app_version: NotRequired[
        "aws_sdk_sagemaker.types.major_minor_version.MajorMinorVersion"
    ]
    """<p>The semantic version to upgrade the SageMaker Partner AI App to. Must be the same semantic version returned in the <code>AvailableUpgrade</code> field from <code>DescribePartnerApp</code>. Version skipping and downgrades are not supported.</p>"""
    client_token: NotRequired["aws_sdk_sagemaker.types.client_token.ClientToken"]
    """<p>A unique token that guarantees that the call to this API is idempotent.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>Each tag consists of a key and an optional value. Tag keys must be unique per resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePartnerAppRequest) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "maintenance_config" in value:
        import aws_sdk_sagemaker.types.partner_app_maintenance_config

        out["MaintenanceConfig"] = (
            aws_sdk_sagemaker.types.partner_app_maintenance_config.serialize_aws_json_1_1(
                value["maintenance_config"]
            )
        )
    if "tier" in value:
        out["Tier"] = value["tier"]
    if "application_config" in value:
        import aws_sdk_sagemaker.types.partner_app_config

        out["ApplicationConfig"] = (
            aws_sdk_sagemaker.types.partner_app_config.serialize_aws_json_1_1(
                value["application_config"]
            )
        )
    if "enable_iam_session_based_identity" in value:
        out["EnableIamSessionBasedIdentity"] = value[
            "enable_iam_session_based_identity"
        ]
    if "enable_auto_minor_version_upgrade" in value:
        out["EnableAutoMinorVersionUpgrade"] = value[
            "enable_auto_minor_version_upgrade"
        ]
    if "app_version" in value:
        out["AppVersion"] = value["app_version"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePartnerAppRequest:
    out: UpdatePartnerAppRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "MaintenanceConfig" in data:
        import aws_sdk_sagemaker.types.partner_app_maintenance_config

        out["maintenance_config"] = (
            aws_sdk_sagemaker.types.partner_app_maintenance_config.deserialize_aws_json_1_1(
                data["MaintenanceConfig"]
            )
        )
    if "Tier" in data:
        out["tier"] = data["Tier"]
    if "ApplicationConfig" in data:
        import aws_sdk_sagemaker.types.partner_app_config

        out["application_config"] = (
            aws_sdk_sagemaker.types.partner_app_config.deserialize_aws_json_1_1(
                data["ApplicationConfig"]
            )
        )
    if "EnableIamSessionBasedIdentity" in data:
        out["enable_iam_session_based_identity"] = data["EnableIamSessionBasedIdentity"]
    if "EnableAutoMinorVersionUpgrade" in data:
        out["enable_auto_minor_version_upgrade"] = data["EnableAutoMinorVersionUpgrade"]
    if "AppVersion" in data:
        out["app_version"] = data["AppVersion"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
