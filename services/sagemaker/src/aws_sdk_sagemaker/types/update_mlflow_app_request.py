"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateMlflowAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.account_default_status
    import aws_sdk_sagemaker.types.default_domain_id_list
    import aws_sdk_sagemaker.types.mlflow_app_arn
    import aws_sdk_sagemaker.types.mlflow_app_name
    import aws_sdk_sagemaker.types.model_registration_mode
    import aws_sdk_sagemaker.types.s3_uri
    import aws_sdk_sagemaker.types.weekly_maintenance_window_start


class UpdateMlflowAppRequest(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_sagemaker.types.mlflow_app_arn.MlflowAppArn"]
    """<p>The ARN of the MLflow App to update.</p>"""
    name: NotRequired["aws_sdk_sagemaker.types.mlflow_app_name.MlflowAppName"]
    """<p>The name of the MLflow App to update.</p>"""
    artifact_store_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The new S3 URI for the general purpose bucket to use as the artifact store for the MLflow App.</p>"""
    model_registration_mode: NotRequired[
        "aws_sdk_sagemaker.types.model_registration_mode.ModelRegistrationMode"
    ]
    """<p>Whether to enable or disable automatic registration of new MLflow models to the SageMaker Model Registry. To enable automatic model registration, set this value to <code>AutoModelRegistrationEnabled</code>. To disable automatic model registration, set this value to <code>AutoModelRegistrationDisabled</code>. If not specified, <code>AutomaticModelRegistration</code> defaults to <code>AutoModelRegistrationEnabled</code> </p>"""
    weekly_maintenance_window_start: NotRequired[
        "aws_sdk_sagemaker.types.weekly_maintenance_window_start.WeeklyMaintenanceWindowStart"
    ]
    """<p>The new weekly maintenance window start day and time to update. The maintenance window day and time should be in Coordinated Universal Time (UTC) 24-hour standard time. For example: TUE:03:30.</p>"""
    default_domain_id_list: NotRequired[
        "aws_sdk_sagemaker.types.default_domain_id_list.DefaultDomainIdList"
    ]
    """<p>List of SageMaker Domain IDs for which this MLflow App is the default.</p>"""
    account_default_status: NotRequired[
        "aws_sdk_sagemaker.types.account_default_status.AccountDefaultStatus"
    ]
    """<p>Indicates whether this this MLflow App is the default for the account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMlflowAppRequest) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "artifact_store_uri" in value:
        out["ArtifactStoreUri"] = value["artifact_store_uri"]
    if "model_registration_mode" in value:
        import aws_sdk_sagemaker.types.model_registration_mode

        out["ModelRegistrationMode"] = (
            aws_sdk_sagemaker.types.model_registration_mode.serialize_aws_json_1_1(
                value["model_registration_mode"]
            )
        )
    if "weekly_maintenance_window_start" in value:
        out["WeeklyMaintenanceWindowStart"] = value["weekly_maintenance_window_start"]
    if "default_domain_id_list" in value:
        import aws_sdk_sagemaker.types.default_domain_id_list

        out["DefaultDomainIdList"] = (
            aws_sdk_sagemaker.types.default_domain_id_list.serialize_aws_json_1_1(
                value["default_domain_id_list"]
            )
        )
    if "account_default_status" in value:
        import aws_sdk_sagemaker.types.account_default_status

        out["AccountDefaultStatus"] = (
            aws_sdk_sagemaker.types.account_default_status.serialize_aws_json_1_1(
                value["account_default_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMlflowAppRequest:
    out: UpdateMlflowAppRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ArtifactStoreUri" in data:
        out["artifact_store_uri"] = data["ArtifactStoreUri"]
    if "ModelRegistrationMode" in data:
        import aws_sdk_sagemaker.types.model_registration_mode

        out["model_registration_mode"] = (
            aws_sdk_sagemaker.types.model_registration_mode.deserialize_aws_json_1_1(
                data["ModelRegistrationMode"]
            )
        )
    if "WeeklyMaintenanceWindowStart" in data:
        out["weekly_maintenance_window_start"] = data["WeeklyMaintenanceWindowStart"]
    if "DefaultDomainIdList" in data:
        import aws_sdk_sagemaker.types.default_domain_id_list

        out["default_domain_id_list"] = (
            aws_sdk_sagemaker.types.default_domain_id_list.deserialize_aws_json_1_1(
                data["DefaultDomainIdList"]
            )
        )
    if "AccountDefaultStatus" in data:
        import aws_sdk_sagemaker.types.account_default_status

        out["account_default_status"] = (
            aws_sdk_sagemaker.types.account_default_status.deserialize_aws_json_1_1(
                data["AccountDefaultStatus"]
            )
        )
    return out
