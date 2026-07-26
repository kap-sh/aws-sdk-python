"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateMlflowTrackingServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.account_id
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.s3_uri
    import capo_sagemaker.types.tracking_server_name
    import capo_sagemaker.types.tracking_server_size
    import capo_sagemaker.types.weekly_maintenance_window_start


class UpdateMlflowTrackingServerRequest(TypedDict, closed=True):
    tracking_server_name: NotRequired[
        "capo_sagemaker.types.tracking_server_name.TrackingServerName"
    ]
    """<p>The name of the MLflow Tracking Server to update.</p>"""
    artifact_store_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The new S3 URI for the general purpose bucket to use as the artifact store for the MLflow Tracking Server.</p>"""
    tracking_server_size: NotRequired[
        "capo_sagemaker.types.tracking_server_size.TrackingServerSize"
    ]
    """<p>The new size for the MLflow Tracking Server.</p>"""
    automatic_model_registration: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>Whether to enable or disable automatic registration of new MLflow models to the SageMaker Model Registry. To enable automatic model registration, set this value to <code>True</code>. To disable automatic model registration, set this value to <code>False</code>. If not specified, <code>AutomaticModelRegistration</code> defaults to <code>False</code> </p>"""
    weekly_maintenance_window_start: NotRequired[
        "capo_sagemaker.types.weekly_maintenance_window_start.WeeklyMaintenanceWindowStart"
    ]
    """<p>The new weekly maintenance window start day and time to update. The maintenance window day and time should be in Coordinated Universal Time (UTC) 24-hour standard time. For example: TUE:03:30.</p>"""
    s3_bucket_owner_account_id: NotRequired["capo_sagemaker.types.account_id.AccountId"]
    """<p>The new expected Amazon Web Services account ID that owns the Amazon S3 bucket for artifact storage.</p>"""
    s3_bucket_owner_verification: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>Whether to enable or disable Amazon S3 Bucket Owenrship Verifaction whenever the MLflow Tracking Server interacts with Amazon Amazon S3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMlflowTrackingServerRequest) -> dict:
    out: dict = {}
    if "tracking_server_name" in value:
        out["TrackingServerName"] = value["tracking_server_name"]
    if "artifact_store_uri" in value:
        out["ArtifactStoreUri"] = value["artifact_store_uri"]
    if "tracking_server_size" in value:
        import capo_sagemaker.types.tracking_server_size

        out["TrackingServerSize"] = (
            capo_sagemaker.types.tracking_server_size.serialize_aws_json_1_1(
                value["tracking_server_size"]
            )
        )
    if "automatic_model_registration" in value:
        out["AutomaticModelRegistration"] = value["automatic_model_registration"]
    if "weekly_maintenance_window_start" in value:
        out["WeeklyMaintenanceWindowStart"] = value["weekly_maintenance_window_start"]
    if "s3_bucket_owner_account_id" in value:
        out["S3BucketOwnerAccountId"] = value["s3_bucket_owner_account_id"]
    if "s3_bucket_owner_verification" in value:
        out["S3BucketOwnerVerification"] = value["s3_bucket_owner_verification"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMlflowTrackingServerRequest:
    out: UpdateMlflowTrackingServerRequest = {}  # type: ignore[typeddict-item]
    if "TrackingServerName" in data:
        out["tracking_server_name"] = data["TrackingServerName"]
    if "ArtifactStoreUri" in data:
        out["artifact_store_uri"] = data["ArtifactStoreUri"]
    if "TrackingServerSize" in data:
        import capo_sagemaker.types.tracking_server_size

        out["tracking_server_size"] = (
            capo_sagemaker.types.tracking_server_size.deserialize_aws_json_1_1(
                data["TrackingServerSize"]
            )
        )
    if "AutomaticModelRegistration" in data:
        out["automatic_model_registration"] = data["AutomaticModelRegistration"]
    if "WeeklyMaintenanceWindowStart" in data:
        out["weekly_maintenance_window_start"] = data["WeeklyMaintenanceWindowStart"]
    if "S3BucketOwnerAccountId" in data:
        out["s3_bucket_owner_account_id"] = data["S3BucketOwnerAccountId"]
    if "S3BucketOwnerVerification" in data:
        out["s3_bucket_owner_verification"] = data["S3BucketOwnerVerification"]
    return out
