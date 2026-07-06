"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateMlflowAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.account_default_status
    import aws_sdk_sagemaker.types.default_domain_id_list
    import aws_sdk_sagemaker.types.mlflow_app_name
    import aws_sdk_sagemaker.types.model_registration_mode
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.s3_uri
    import aws_sdk_sagemaker.types.tag_list
    import aws_sdk_sagemaker.types.weekly_maintenance_window_start


class CreateMlflowAppRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_sagemaker.types.mlflow_app_name.MlflowAppName"]
    """<p>A string identifying the MLflow app name. This string is not part of the tracking server ARN.</p>"""
    artifact_store_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The S3 URI for a general purpose bucket to use as the MLflow App artifact store.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) for an IAM role in your account that the MLflow App uses to access the artifact store in Amazon S3. The role should have the <code>AmazonS3FullAccess</code> permission.</p>"""
    model_registration_mode: NotRequired[
        "aws_sdk_sagemaker.types.model_registration_mode.ModelRegistrationMode"
    ]
    """<p>Whether to enable or disable automatic registration of new MLflow models to the SageMaker Model Registry. To enable automatic model registration, set this value to <code>AutoModelRegistrationEnabled</code>. To disable automatic model registration, set this value to <code>AutoModelRegistrationDisabled</code>. If not specified, <code>AutomaticModelRegistration</code> defaults to <code>AutoModelRegistrationDisabled</code>.</p>"""
    weekly_maintenance_window_start: NotRequired[
        "aws_sdk_sagemaker.types.weekly_maintenance_window_start.WeeklyMaintenanceWindowStart"
    ]
    """<p>The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time that weekly maintenance updates are scheduled. For example: TUE:03:30.</p>"""
    account_default_status: NotRequired[
        "aws_sdk_sagemaker.types.account_default_status.AccountDefaultStatus"
    ]
    """<p>Indicates whether this MLflow app is the default for the entire account.</p>"""
    default_domain_id_list: NotRequired[
        "aws_sdk_sagemaker.types.default_domain_id_list.DefaultDomainIdList"
    ]
    """<p>List of SageMaker domain IDs for which this MLflow App is used as the default.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>Tags consisting of key-value pairs used to manage metadata for the MLflow App.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMlflowAppRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "artifact_store_uri" in value:
        out["ArtifactStoreUri"] = value["artifact_store_uri"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "model_registration_mode" in value:
        import aws_sdk_sagemaker.types.model_registration_mode

        out["ModelRegistrationMode"] = (
            aws_sdk_sagemaker.types.model_registration_mode.serialize_aws_json_1_1(
                value["model_registration_mode"]
            )
        )
    if "weekly_maintenance_window_start" in value:
        out["WeeklyMaintenanceWindowStart"] = value["weekly_maintenance_window_start"]
    if "account_default_status" in value:
        import aws_sdk_sagemaker.types.account_default_status

        out["AccountDefaultStatus"] = (
            aws_sdk_sagemaker.types.account_default_status.serialize_aws_json_1_1(
                value["account_default_status"]
            )
        )
    if "default_domain_id_list" in value:
        import aws_sdk_sagemaker.types.default_domain_id_list

        out["DefaultDomainIdList"] = (
            aws_sdk_sagemaker.types.default_domain_id_list.serialize_aws_json_1_1(
                value["default_domain_id_list"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMlflowAppRequest:
    out: CreateMlflowAppRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ArtifactStoreUri" in data:
        out["artifact_store_uri"] = data["ArtifactStoreUri"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "ModelRegistrationMode" in data:
        import aws_sdk_sagemaker.types.model_registration_mode

        out["model_registration_mode"] = (
            aws_sdk_sagemaker.types.model_registration_mode.deserialize_aws_json_1_1(
                data["ModelRegistrationMode"]
            )
        )
    if "WeeklyMaintenanceWindowStart" in data:
        out["weekly_maintenance_window_start"] = data["WeeklyMaintenanceWindowStart"]
    if "AccountDefaultStatus" in data:
        import aws_sdk_sagemaker.types.account_default_status

        out["account_default_status"] = (
            aws_sdk_sagemaker.types.account_default_status.deserialize_aws_json_1_1(
                data["AccountDefaultStatus"]
            )
        )
    if "DefaultDomainIdList" in data:
        import aws_sdk_sagemaker.types.default_domain_id_list

        out["default_domain_id_list"] = (
            aws_sdk_sagemaker.types.default_domain_id_list.deserialize_aws_json_1_1(
                data["DefaultDomainIdList"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
