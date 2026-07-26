"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribePartnerAppResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.available_upgrade
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.error_info
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.non_empty_string64
    import capo_sagemaker.types.partner_app_arn
    import capo_sagemaker.types.partner_app_auth_type
    import capo_sagemaker.types.partner_app_config
    import capo_sagemaker.types.partner_app_maintenance_config
    import capo_sagemaker.types.partner_app_name
    import capo_sagemaker.types.partner_app_status
    import capo_sagemaker.types.partner_app_type
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.string2048
    import capo_sagemaker.types.timestamp


class DescribePartnerAppResponse(TypedDict, closed=True):
    arn: NotRequired["capo_sagemaker.types.partner_app_arn.PartnerAppArn"]
    """<p>The ARN of the SageMaker Partner AI App that was described.</p>"""
    name: NotRequired["capo_sagemaker.types.partner_app_name.PartnerAppName"]
    """<p>The name of the SageMaker Partner AI App.</p>"""
    type: NotRequired["capo_sagemaker.types.partner_app_type.PartnerAppType"]
    """<p>The type of SageMaker Partner AI App. Must be one of the following: <code>lakera-guard</code>, <code>comet</code>, <code>deepchecks-llm-evaluation</code>, or <code>fiddler</code>.</p>"""
    status: NotRequired["capo_sagemaker.types.partner_app_status.PartnerAppStatus"]
    """<p>The status of the SageMaker Partner AI App.</p> <ul> <li> <p>Creating: SageMaker AI is creating the partner AI app. The partner AI app is not available during creation.</p> </li> <li> <p>Updating: SageMaker AI is updating the partner AI app. The partner AI app is not available when updating.</p> </li> <li> <p>Deleting: SageMaker AI is deleting the partner AI app. The partner AI app is not available during deletion.</p> </li> <li> <p>Available: The partner AI app is provisioned and accessible.</p> </li> <li> <p>Failed: The partner AI app is in a failed state and isn't available. SageMaker AI is investigating the issue. For further guidance, contact Amazon Web Services Support.</p> </li> <li> <p>UpdateFailed: The partner AI app couldn't be updated but is available.</p> </li> <li> <p>Deleted: The partner AI app is permanently deleted and not available.</p> </li> </ul>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the SageMaker Partner AI App was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the SageMaker Partner AI App was last modified.</p>"""
    execution_role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role associated with the SageMaker Partner AI App.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS customer managed key used to encrypt the data at rest associated with SageMaker Partner AI Apps.</p>"""
    base_url: NotRequired["capo_sagemaker.types.string2048.String2048"]
    """<p>The URL of the SageMaker Partner AI App that the Application SDK uses to support in-app calls for the user.</p>"""
    maintenance_config: NotRequired[
        "capo_sagemaker.types.partner_app_maintenance_config.PartnerAppMaintenanceConfig"
    ]
    """<p>Maintenance configuration settings for the SageMaker Partner AI App.</p>"""
    tier: NotRequired["capo_sagemaker.types.non_empty_string64.NonEmptyString64"]
    """<p>The instance type and size of the cluster attached to the SageMaker Partner AI App.</p>"""
    version: NotRequired["capo_sagemaker.types.non_empty_string64.NonEmptyString64"]
    """<p>The version of the SageMaker Partner AI App.</p>"""
    application_config: NotRequired[
        "capo_sagemaker.types.partner_app_config.PartnerAppConfig"
    ]
    """<p>Configuration settings for the SageMaker Partner AI App.</p>"""
    auth_type: NotRequired[
        "capo_sagemaker.types.partner_app_auth_type.PartnerAppAuthType"
    ]
    """<p>The authorization type that users use to access the SageMaker Partner AI App.</p>"""
    enable_iam_session_based_identity: NotRequired[
        "capo_sagemaker.types.boolean.Boolean"
    ]
    """<p>When set to <code>TRUE</code>, the SageMaker Partner AI App sets the Amazon Web Services IAM session name or the authenticated IAM user as the identity of the SageMaker Partner AI App user.</p>"""
    error: NotRequired["capo_sagemaker.types.error_info.ErrorInfo"]
    """<p>This is an error field object that contains the error code and the reason for an operation failure.</p>"""
    enable_auto_minor_version_upgrade: NotRequired[
        "capo_sagemaker.types.boolean.Boolean"
    ]
    """<p>Indicates whether the SageMaker Partner AI App is configured for automatic minor version upgrades during scheduled maintenance windows.</p>"""
    current_version_eol_date: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The end-of-life date for the current version of the SageMaker Partner AI App.</p>"""
    available_upgrade: NotRequired[
        "capo_sagemaker.types.available_upgrade.AvailableUpgrade"
    ]
    """<p>A map of available minor version upgrades for the SageMaker Partner AI App. The key is the semantic version number, and the value is a list of release notes for that version. A null value indicates no upgrades are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePartnerAppResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_sagemaker.types.partner_app_type

        out["Type"] = capo_sagemaker.types.partner_app_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "status" in value:
        import capo_sagemaker.types.partner_app_status

        out["Status"] = capo_sagemaker.types.partner_app_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "base_url" in value:
        out["BaseUrl"] = value["base_url"]
    if "maintenance_config" in value:
        import capo_sagemaker.types.partner_app_maintenance_config

        out["MaintenanceConfig"] = (
            capo_sagemaker.types.partner_app_maintenance_config.serialize_aws_json_1_1(
                value["maintenance_config"]
            )
        )
    if "tier" in value:
        out["Tier"] = value["tier"]
    if "version" in value:
        out["Version"] = value["version"]
    if "application_config" in value:
        import capo_sagemaker.types.partner_app_config

        out["ApplicationConfig"] = (
            capo_sagemaker.types.partner_app_config.serialize_aws_json_1_1(
                value["application_config"]
            )
        )
    if "auth_type" in value:
        import capo_sagemaker.types.partner_app_auth_type

        out["AuthType"] = (
            capo_sagemaker.types.partner_app_auth_type.serialize_aws_json_1_1(
                value["auth_type"]
            )
        )
    if "enable_iam_session_based_identity" in value:
        out["EnableIamSessionBasedIdentity"] = value[
            "enable_iam_session_based_identity"
        ]
    if "error" in value:
        import capo_sagemaker.types.error_info

        out["Error"] = capo_sagemaker.types.error_info.serialize_aws_json_1_1(
            value["error"]
        )
    if "enable_auto_minor_version_upgrade" in value:
        out["EnableAutoMinorVersionUpgrade"] = value[
            "enable_auto_minor_version_upgrade"
        ]
    if "current_version_eol_date" in value:
        import capo_sagemaker.types.timestamp

        out["CurrentVersionEolDate"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["current_version_eol_date"]
            )
        )
    if "available_upgrade" in value:
        import capo_sagemaker.types.available_upgrade

        out["AvailableUpgrade"] = (
            capo_sagemaker.types.available_upgrade.serialize_aws_json_1_1(
                value["available_upgrade"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePartnerAppResponse:
    out: DescribePartnerAppResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import capo_sagemaker.types.partner_app_type

        out["type"] = capo_sagemaker.types.partner_app_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Status" in data:
        import capo_sagemaker.types.partner_app_status

        out["status"] = (
            capo_sagemaker.types.partner_app_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "BaseUrl" in data:
        out["base_url"] = data["BaseUrl"]
    if "MaintenanceConfig" in data:
        import capo_sagemaker.types.partner_app_maintenance_config

        out["maintenance_config"] = (
            capo_sagemaker.types.partner_app_maintenance_config.deserialize_aws_json_1_1(
                data["MaintenanceConfig"]
            )
        )
    if "Tier" in data:
        out["tier"] = data["Tier"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "ApplicationConfig" in data:
        import capo_sagemaker.types.partner_app_config

        out["application_config"] = (
            capo_sagemaker.types.partner_app_config.deserialize_aws_json_1_1(
                data["ApplicationConfig"]
            )
        )
    if "AuthType" in data:
        import capo_sagemaker.types.partner_app_auth_type

        out["auth_type"] = (
            capo_sagemaker.types.partner_app_auth_type.deserialize_aws_json_1_1(
                data["AuthType"]
            )
        )
    if "EnableIamSessionBasedIdentity" in data:
        out["enable_iam_session_based_identity"] = data["EnableIamSessionBasedIdentity"]
    if "Error" in data:
        import capo_sagemaker.types.error_info

        out["error"] = capo_sagemaker.types.error_info.deserialize_aws_json_1_1(
            data["Error"]
        )
    if "EnableAutoMinorVersionUpgrade" in data:
        out["enable_auto_minor_version_upgrade"] = data["EnableAutoMinorVersionUpgrade"]
    if "CurrentVersionEolDate" in data:
        import capo_sagemaker.types.timestamp

        out["current_version_eol_date"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CurrentVersionEolDate"]
            )
        )
    if "AvailableUpgrade" in data:
        import capo_sagemaker.types.available_upgrade

        out["available_upgrade"] = (
            capo_sagemaker.types.available_upgrade.deserialize_aws_json_1_1(
                data["AvailableUpgrade"]
            )
        )
    return out
