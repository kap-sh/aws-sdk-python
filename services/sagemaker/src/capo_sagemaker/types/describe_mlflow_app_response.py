"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeMlflowAppResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.account_default_status
    import capo_sagemaker.types.default_domain_id_list
    import capo_sagemaker.types.maintenance_status
    import capo_sagemaker.types.mlflow_app_arn
    import capo_sagemaker.types.mlflow_app_name
    import capo_sagemaker.types.mlflow_app_status
    import capo_sagemaker.types.mlflow_version
    import capo_sagemaker.types.model_registration_mode
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.s3_uri
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context
    import capo_sagemaker.types.weekly_maintenance_window_start


class DescribeMlflowAppResponse(TypedDict, closed=True):
    arn: NotRequired["capo_sagemaker.types.mlflow_app_arn.MlflowAppArn"]
    """<p>The ARN of the MLflow App.</p>"""
    name: NotRequired["capo_sagemaker.types.mlflow_app_name.MlflowAppName"]
    """<p>The name of the MLflow App.</p>"""
    artifact_store_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The S3 URI of the general purpose bucket used as the MLflow App artifact store.</p>"""
    mlflow_version: NotRequired["capo_sagemaker.types.mlflow_version.MlflowVersion"]
    """<p>The MLflow version used.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) for an IAM role in your account that the MLflow App uses to access the artifact store in Amazon S3.</p>"""
    status: NotRequired["capo_sagemaker.types.mlflow_app_status.MlflowAppStatus"]
    """<p>The current creation status of the described MLflow App.</p>"""
    model_registration_mode: NotRequired[
        "capo_sagemaker.types.model_registration_mode.ModelRegistrationMode"
    ]
    """<p>Whether automatic registration of new MLflow models to the SageMaker Model Registry is enabled.</p>"""
    account_default_status: NotRequired[
        "capo_sagemaker.types.account_default_status.AccountDefaultStatus"
    ]
    """<p>Indicates whether this MLflow app is the default for the entire account.</p>"""
    default_domain_id_list: NotRequired[
        "capo_sagemaker.types.default_domain_id_list.DefaultDomainIdList"
    ]
    """<p>List of SageMaker Domain IDs for which this MLflow App is the default.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when the MLflow App was created.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when the MLflow App was last modified.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    weekly_maintenance_window_start: NotRequired[
        "capo_sagemaker.types.weekly_maintenance_window_start.WeeklyMaintenanceWindowStart"
    ]
    """<p>The day and time of the week when weekly maintenance occurs.</p>"""
    maintenance_status: NotRequired[
        "capo_sagemaker.types.maintenance_status.MaintenanceStatus"
    ]
    """<p>Current maintenance status of the MLflow App.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMlflowAppResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "artifact_store_uri" in value:
        out["ArtifactStoreUri"] = value["artifact_store_uri"]
    if "mlflow_version" in value:
        out["MlflowVersion"] = value["mlflow_version"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "status" in value:
        import capo_sagemaker.types.mlflow_app_status

        out["Status"] = capo_sagemaker.types.mlflow_app_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "model_registration_mode" in value:
        import capo_sagemaker.types.model_registration_mode

        out["ModelRegistrationMode"] = (
            capo_sagemaker.types.model_registration_mode.serialize_aws_json_1_1(
                value["model_registration_mode"]
            )
        )
    if "account_default_status" in value:
        import capo_sagemaker.types.account_default_status

        out["AccountDefaultStatus"] = (
            capo_sagemaker.types.account_default_status.serialize_aws_json_1_1(
                value["account_default_status"]
            )
        )
    if "default_domain_id_list" in value:
        import capo_sagemaker.types.default_domain_id_list

        out["DefaultDomainIdList"] = (
            capo_sagemaker.types.default_domain_id_list.serialize_aws_json_1_1(
                value["default_domain_id_list"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "last_modified_by" in value:
        import capo_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            capo_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "weekly_maintenance_window_start" in value:
        out["WeeklyMaintenanceWindowStart"] = value["weekly_maintenance_window_start"]
    if "maintenance_status" in value:
        import capo_sagemaker.types.maintenance_status

        out["MaintenanceStatus"] = (
            capo_sagemaker.types.maintenance_status.serialize_aws_json_1_1(
                value["maintenance_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMlflowAppResponse:
    out: DescribeMlflowAppResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ArtifactStoreUri" in data:
        out["artifact_store_uri"] = data["ArtifactStoreUri"]
    if "MlflowVersion" in data:
        out["mlflow_version"] = data["MlflowVersion"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Status" in data:
        import capo_sagemaker.types.mlflow_app_status

        out["status"] = capo_sagemaker.types.mlflow_app_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "ModelRegistrationMode" in data:
        import capo_sagemaker.types.model_registration_mode

        out["model_registration_mode"] = (
            capo_sagemaker.types.model_registration_mode.deserialize_aws_json_1_1(
                data["ModelRegistrationMode"]
            )
        )
    if "AccountDefaultStatus" in data:
        import capo_sagemaker.types.account_default_status

        out["account_default_status"] = (
            capo_sagemaker.types.account_default_status.deserialize_aws_json_1_1(
                data["AccountDefaultStatus"]
            )
        )
    if "DefaultDomainIdList" in data:
        import capo_sagemaker.types.default_domain_id_list

        out["default_domain_id_list"] = (
            capo_sagemaker.types.default_domain_id_list.deserialize_aws_json_1_1(
                data["DefaultDomainIdList"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "CreatedBy" in data:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastModifiedBy" in data:
        import capo_sagemaker.types.user_context

        out["last_modified_by"] = (
            capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if "WeeklyMaintenanceWindowStart" in data:
        out["weekly_maintenance_window_start"] = data["WeeklyMaintenanceWindowStart"]
    if "MaintenanceStatus" in data:
        import capo_sagemaker.types.maintenance_status

        out["maintenance_status"] = (
            capo_sagemaker.types.maintenance_status.deserialize_aws_json_1_1(
                data["MaintenanceStatus"]
            )
        )
    return out
