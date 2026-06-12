"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeMlflowTrackingServerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.account_id
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.is_tracking_server_active
    import aws_sdk_sagemaker.types.mlflow_version
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.s3_uri
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.tracking_server_arn
    import aws_sdk_sagemaker.types.tracking_server_maintenance_status
    import aws_sdk_sagemaker.types.tracking_server_name
    import aws_sdk_sagemaker.types.tracking_server_size
    import aws_sdk_sagemaker.types.tracking_server_status
    import aws_sdk_sagemaker.types.tracking_server_url
    import aws_sdk_sagemaker.types.user_context
    import aws_sdk_sagemaker.types.weekly_maintenance_window_start


class DescribeMlflowTrackingServerResponse(TypedDict):
    tracking_server_arn: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_arn.TrackingServerArn"
    ]
    """<p>The ARN of the described tracking server.</p>"""
    tracking_server_name: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_name.TrackingServerName"
    ]
    """<p>The name of the described tracking server.</p>"""
    artifact_store_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The S3 URI of the general purpose bucket used as the MLflow Tracking Server artifact store.</p>"""
    tracking_server_size: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_size.TrackingServerSize"
    ]
    """<p>The size of the described tracking server.</p>"""
    mlflow_version: NotRequired["aws_sdk_sagemaker.types.mlflow_version.MlflowVersion"]
    """<p>The MLflow version used for the described tracking server.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) for an IAM role in your account that the described MLflow Tracking Server uses to access the artifact store in Amazon S3.</p>"""
    tracking_server_status: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_status.TrackingServerStatus"
    ]
    """<p>The current creation status of the described MLflow Tracking Server.</p>"""
    tracking_server_maintenance_status: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_maintenance_status.TrackingServerMaintenanceStatus"
    ]
    """<p> The current maintenance status of the described MLflow Tracking Server. </p>"""
    is_active: NotRequired[
        "aws_sdk_sagemaker.types.is_tracking_server_active.IsTrackingServerActive"
    ]
    """<p>Whether the described MLflow Tracking Server is currently active.</p>"""
    tracking_server_url: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_url.TrackingServerUrl"
    ]
    """<p>The URL to connect to the MLflow user interface for the described tracking server.</p>"""
    weekly_maintenance_window_start: NotRequired[
        "aws_sdk_sagemaker.types.weekly_maintenance_window_start.WeeklyMaintenanceWindowStart"
    ]
    """<p>The day and time of the week when weekly maintenance occurs on the described tracking server.</p>"""
    automatic_model_registration: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>Whether automatic registration of new MLflow models to the SageMaker Model Registry is enabled.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp of when the described MLflow Tracking Server was created.</p>"""
    created_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp of when the described MLflow Tracking Server was last modified.</p>"""
    last_modified_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    s3_bucket_owner_account_id: NotRequired[
        "aws_sdk_sagemaker.types.account_id.AccountId"
    ]
    """<p>Expected Amazon Web Services account ID that owns the Amazon S3 bucket for artifact storage.</p>"""
    s3_bucket_owner_verification: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>Whether Amazon S3 Bucket Ownership checks are enabled whenever the tracking server interacts with Amazon Amazon S3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMlflowTrackingServerResponse) -> dict:
    out: dict = {}
    if "tracking_server_arn" in value:
        out["TrackingServerArn"] = value["tracking_server_arn"]
    if "tracking_server_name" in value:
        out["TrackingServerName"] = value["tracking_server_name"]
    if "artifact_store_uri" in value:
        out["ArtifactStoreUri"] = value["artifact_store_uri"]
    if "tracking_server_size" in value:
        import aws_sdk_sagemaker.types.tracking_server_size

        out["TrackingServerSize"] = (
            aws_sdk_sagemaker.types.tracking_server_size.serialize_aws_json_1_1(
                value["tracking_server_size"]
            )
        )
    if "mlflow_version" in value:
        out["MlflowVersion"] = value["mlflow_version"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tracking_server_status" in value:
        import aws_sdk_sagemaker.types.tracking_server_status

        out["TrackingServerStatus"] = (
            aws_sdk_sagemaker.types.tracking_server_status.serialize_aws_json_1_1(
                value["tracking_server_status"]
            )
        )
    if "tracking_server_maintenance_status" in value:
        import aws_sdk_sagemaker.types.tracking_server_maintenance_status

        out["TrackingServerMaintenanceStatus"] = (
            aws_sdk_sagemaker.types.tracking_server_maintenance_status.serialize_aws_json_1_1(
                value["tracking_server_maintenance_status"]
            )
        )
    if "is_active" in value:
        import aws_sdk_sagemaker.types.is_tracking_server_active

        out["IsActive"] = (
            aws_sdk_sagemaker.types.is_tracking_server_active.serialize_aws_json_1_1(
                value["is_active"]
            )
        )
    if "tracking_server_url" in value:
        out["TrackingServerUrl"] = value["tracking_server_url"]
    if "weekly_maintenance_window_start" in value:
        out["WeeklyMaintenanceWindowStart"] = value["weekly_maintenance_window_start"]
    if "automatic_model_registration" in value:
        out["AutomaticModelRegistration"] = value["automatic_model_registration"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["CreatedBy"] = aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_modified_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "s3_bucket_owner_account_id" in value:
        out["S3BucketOwnerAccountId"] = value["s3_bucket_owner_account_id"]
    if "s3_bucket_owner_verification" in value:
        out["S3BucketOwnerVerification"] = value["s3_bucket_owner_verification"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMlflowTrackingServerResponse:
    out: DescribeMlflowTrackingServerResponse = {}  # type: ignore[typeddict-item]
    if "TrackingServerArn" in data:
        out["tracking_server_arn"] = data["TrackingServerArn"]
    if "TrackingServerName" in data:
        out["tracking_server_name"] = data["TrackingServerName"]
    if "ArtifactStoreUri" in data:
        out["artifact_store_uri"] = data["ArtifactStoreUri"]
    if "TrackingServerSize" in data:
        import aws_sdk_sagemaker.types.tracking_server_size

        out["tracking_server_size"] = (
            aws_sdk_sagemaker.types.tracking_server_size.deserialize_aws_json_1_1(
                data["TrackingServerSize"]
            )
        )
    if "MlflowVersion" in data:
        out["mlflow_version"] = data["MlflowVersion"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "TrackingServerStatus" in data:
        import aws_sdk_sagemaker.types.tracking_server_status

        out["tracking_server_status"] = (
            aws_sdk_sagemaker.types.tracking_server_status.deserialize_aws_json_1_1(
                data["TrackingServerStatus"]
            )
        )
    if "TrackingServerMaintenanceStatus" in data:
        import aws_sdk_sagemaker.types.tracking_server_maintenance_status

        out["tracking_server_maintenance_status"] = (
            aws_sdk_sagemaker.types.tracking_server_maintenance_status.deserialize_aws_json_1_1(
                data["TrackingServerMaintenanceStatus"]
            )
        )
    if "IsActive" in data:
        import aws_sdk_sagemaker.types.is_tracking_server_active

        out["is_active"] = (
            aws_sdk_sagemaker.types.is_tracking_server_active.deserialize_aws_json_1_1(
                data["IsActive"]
            )
        )
    if "TrackingServerUrl" in data:
        out["tracking_server_url"] = data["TrackingServerUrl"]
    if "WeeklyMaintenanceWindowStart" in data:
        out["weekly_maintenance_window_start"] = data["WeeklyMaintenanceWindowStart"]
    if "AutomaticModelRegistration" in data:
        out["automatic_model_registration"] = data["AutomaticModelRegistration"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "CreatedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["created_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["CreatedBy"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastModifiedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["last_modified_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if "S3BucketOwnerAccountId" in data:
        out["s3_bucket_owner_account_id"] = data["S3BucketOwnerAccountId"]
    if "S3BucketOwnerVerification" in data:
        out["s3_bucket_owner_verification"] = data["S3BucketOwnerVerification"]
    return out
