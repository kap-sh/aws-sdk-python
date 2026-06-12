"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeAppResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_arn
    import aws_sdk_sagemaker.types.app_name
    import aws_sdk_sagemaker.types.app_status
    import aws_sdk_sagemaker.types.app_type
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.domain_id
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.feature_status
    import aws_sdk_sagemaker.types.resource_spec
    import aws_sdk_sagemaker.types.space_name
    import aws_sdk_sagemaker.types.studio_lifecycle_config_arn
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.user_profile_name


class DescribeAppResponse(TypedDict):
    app_arn: NotRequired["aws_sdk_sagemaker.types.app_arn.AppArn"]
    """<p>The Amazon Resource Name (ARN) of the app.</p>"""
    app_type: NotRequired["aws_sdk_sagemaker.types.app_type.AppType"]
    """<p>The type of app.</p>"""
    app_name: NotRequired["aws_sdk_sagemaker.types.app_name.AppName"]
    """<p>The name of the app.</p>"""
    domain_id: NotRequired["aws_sdk_sagemaker.types.domain_id.DomainId"]
    """<p>The domain ID.</p>"""
    user_profile_name: NotRequired[
        "aws_sdk_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>The user profile name.</p>"""
    space_name: NotRequired["aws_sdk_sagemaker.types.space_name.SpaceName"]
    """<p>The name of the space. If this value is not set, then <code>UserProfileName</code> must be set.</p>"""
    status: NotRequired["aws_sdk_sagemaker.types.app_status.AppStatus"]
    """<p>The status.</p>"""
    effective_trusted_identity_propagation_status: NotRequired[
        "aws_sdk_sagemaker.types.feature_status.FeatureStatus"
    ]
    """<p>The effective status of Trusted Identity Propagation (TIP) for this application. When enabled, user identities from IAM Identity Center are being propagated through the application to TIP enabled Amazon Web Services services. When disabled, standard IAM role-based access is used. </p>"""
    recovery_mode: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p> Indicates whether the application is launched in recovery mode. </p>"""
    last_health_check_timestamp: NotRequired[
        "aws_sdk_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the last health check.</p>"""
    last_user_activity_timestamp: NotRequired[
        "aws_sdk_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the last user's activity. <code>LastUserActivityTimestamp</code> is also updated when SageMaker AI performs health checks without user activity. As a result, this value is set to the same value as <code>LastHealthCheckTimestamp</code>.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of the application.</p> <note> <p>After an application has been shut down for 24 hours, SageMaker AI deletes all metadata for the application. To be considered an update and retain application metadata, applications must be restarted within 24 hours after the previous application has been shut down. After this time window, creation of an application is considered a new application rather than an update of the previous application.</p> </note>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>The failure reason.</p>"""
    resource_spec: NotRequired["aws_sdk_sagemaker.types.resource_spec.ResourceSpec"]
    """<p>The instance type and the Amazon Resource Name (ARN) of the SageMaker AI image created on the instance.</p>"""
    built_in_lifecycle_config_arn: NotRequired[
        "aws_sdk_sagemaker.types.studio_lifecycle_config_arn.StudioLifecycleConfigArn"
    ]
    """<p>The lifecycle configuration that runs before the default lifecycle configuration</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAppResponse) -> dict:
    out: dict = {}
    if "app_arn" in value:
        out["AppArn"] = value["app_arn"]
    if "app_type" in value:
        import aws_sdk_sagemaker.types.app_type

        out["AppType"] = aws_sdk_sagemaker.types.app_type.serialize_aws_json_1_1(
            value["app_type"]
        )
    if "app_name" in value:
        out["AppName"] = value["app_name"]
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "user_profile_name" in value:
        out["UserProfileName"] = value["user_profile_name"]
    if "space_name" in value:
        out["SpaceName"] = value["space_name"]
    if "status" in value:
        import aws_sdk_sagemaker.types.app_status

        out["Status"] = aws_sdk_sagemaker.types.app_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "effective_trusted_identity_propagation_status" in value:
        import aws_sdk_sagemaker.types.feature_status

        out["EffectiveTrustedIdentityPropagationStatus"] = (
            aws_sdk_sagemaker.types.feature_status.serialize_aws_json_1_1(
                value["effective_trusted_identity_propagation_status"]
            )
        )
    if "recovery_mode" in value:
        out["RecoveryMode"] = value["recovery_mode"]
    if "last_health_check_timestamp" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastHealthCheckTimestamp"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_health_check_timestamp"]
            )
        )
    if "last_user_activity_timestamp" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastUserActivityTimestamp"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_user_activity_timestamp"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "resource_spec" in value:
        import aws_sdk_sagemaker.types.resource_spec

        out["ResourceSpec"] = (
            aws_sdk_sagemaker.types.resource_spec.serialize_aws_json_1_1(
                value["resource_spec"]
            )
        )
    if "built_in_lifecycle_config_arn" in value:
        out["BuiltInLifecycleConfigArn"] = value["built_in_lifecycle_config_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAppResponse:
    out: DescribeAppResponse = {}  # type: ignore[typeddict-item]
    if "AppArn" in data:
        out["app_arn"] = data["AppArn"]
    if "AppType" in data:
        import aws_sdk_sagemaker.types.app_type

        out["app_type"] = aws_sdk_sagemaker.types.app_type.deserialize_aws_json_1_1(
            data["AppType"]
        )
    if "AppName" in data:
        out["app_name"] = data["AppName"]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "UserProfileName" in data:
        out["user_profile_name"] = data["UserProfileName"]
    if "SpaceName" in data:
        out["space_name"] = data["SpaceName"]
    if "Status" in data:
        import aws_sdk_sagemaker.types.app_status

        out["status"] = aws_sdk_sagemaker.types.app_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "EffectiveTrustedIdentityPropagationStatus" in data:
        import aws_sdk_sagemaker.types.feature_status

        out["effective_trusted_identity_propagation_status"] = (
            aws_sdk_sagemaker.types.feature_status.deserialize_aws_json_1_1(
                data["EffectiveTrustedIdentityPropagationStatus"]
            )
        )
    if "RecoveryMode" in data:
        out["recovery_mode"] = data["RecoveryMode"]
    if "LastHealthCheckTimestamp" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_health_check_timestamp"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastHealthCheckTimestamp"]
            )
        )
    if "LastUserActivityTimestamp" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_user_activity_timestamp"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastUserActivityTimestamp"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "ResourceSpec" in data:
        import aws_sdk_sagemaker.types.resource_spec

        out["resource_spec"] = (
            aws_sdk_sagemaker.types.resource_spec.deserialize_aws_json_1_1(
                data["ResourceSpec"]
            )
        )
    if "BuiltInLifecycleConfigArn" in data:
        out["built_in_lifecycle_config_arn"] = data["BuiltInLifecycleConfigArn"]
    return out
