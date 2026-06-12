"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePartnerAppRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.client_token
    import aws_sdk_sagemaker.types.kms_key_id
    import aws_sdk_sagemaker.types.non_empty_string64
    import aws_sdk_sagemaker.types.partner_app_auth_type
    import aws_sdk_sagemaker.types.partner_app_config
    import aws_sdk_sagemaker.types.partner_app_maintenance_config
    import aws_sdk_sagemaker.types.partner_app_name
    import aws_sdk_sagemaker.types.partner_app_type
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.tag_list


class CreatePartnerAppRequest(TypedDict):
    name: NotRequired["aws_sdk_sagemaker.types.partner_app_name.PartnerAppName"]
    """<p>The name to give the SageMaker Partner AI App.</p>"""
    type: NotRequired["aws_sdk_sagemaker.types.partner_app_type.PartnerAppType"]
    """<p>The type of SageMaker Partner AI App to create. Must be one of the following: <code>lakera-guard</code>, <code>comet</code>, <code>deepchecks-llm-evaluation</code>, or <code>fiddler</code>.</p>"""
    execution_role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role that the partner application uses.</p>"""
    kms_key_id: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>SageMaker Partner AI Apps uses Amazon Web Services KMS to encrypt data at rest using an Amazon Web Services managed key by default. For more control, specify a customer managed key.</p>"""
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
    auth_type: NotRequired[
        "aws_sdk_sagemaker.types.partner_app_auth_type.PartnerAppAuthType"
    ]
    """<p>The authorization type that users use to access the SageMaker Partner AI App.</p>"""
    enable_iam_session_based_identity: NotRequired[
        "aws_sdk_sagemaker.types.boolean.Boolean"
    ]
    """<p>When set to <code>TRUE</code>, the SageMaker Partner AI App sets the Amazon Web Services IAM session name or the authenticated IAM user as the identity of the SageMaker Partner AI App user.</p>"""
    enable_auto_minor_version_upgrade: NotRequired[
        "aws_sdk_sagemaker.types.boolean.Boolean"
    ]
    """<p>When set to <code>TRUE</code>, the SageMaker Partner AI App is automatically upgraded to the latest minor version during the next scheduled maintenance window, if one is available. Default is <code>FALSE</code>.</p>"""
    client_token: NotRequired["aws_sdk_sagemaker.types.client_token.ClientToken"]
    """<p>A unique token that guarantees that the call to this API is idempotent.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>Each tag consists of a key and an optional value. Tag keys must be unique per resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePartnerAppRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_sagemaker.types.partner_app_type

        out["Type"] = aws_sdk_sagemaker.types.partner_app_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
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
    if "auth_type" in value:
        import aws_sdk_sagemaker.types.partner_app_auth_type

        out["AuthType"] = (
            aws_sdk_sagemaker.types.partner_app_auth_type.serialize_aws_json_1_1(
                value["auth_type"]
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePartnerAppRequest:
    out: CreatePartnerAppRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_sagemaker.types.partner_app_type

        out["type"] = aws_sdk_sagemaker.types.partner_app_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
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
    if "AuthType" in data:
        import aws_sdk_sagemaker.types.partner_app_auth_type

        out["auth_type"] = (
            aws_sdk_sagemaker.types.partner_app_auth_type.deserialize_aws_json_1_1(
                data["AuthType"]
            )
        )
    if "EnableIamSessionBasedIdentity" in data:
        out["enable_iam_session_based_identity"] = data["EnableIamSessionBasedIdentity"]
    if "EnableAutoMinorVersionUpgrade" in data:
        out["enable_auto_minor_version_upgrade"] = data["EnableAutoMinorVersionUpgrade"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
