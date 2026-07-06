"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrackingServerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.is_tracking_server_active
    import aws_sdk_sagemaker.types.mlflow_version
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.tracking_server_arn
    import aws_sdk_sagemaker.types.tracking_server_name
    import aws_sdk_sagemaker.types.tracking_server_status


class TrackingServerSummary(TypedDict, closed=True):
    tracking_server_arn: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_arn.TrackingServerArn"
    ]
    """<p>The ARN of a listed tracking server.</p>"""
    tracking_server_name: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_name.TrackingServerName"
    ]
    """<p>The name of a listed tracking server.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of a listed tracking server.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The last modified time of a listed tracking server.</p>"""
    tracking_server_status: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_status.TrackingServerStatus"
    ]
    """<p>The creation status of a listed tracking server.</p>"""
    is_active: NotRequired[
        "aws_sdk_sagemaker.types.is_tracking_server_active.IsTrackingServerActive"
    ]
    """<p>The activity status of a listed tracking server.</p>"""
    mlflow_version: NotRequired["aws_sdk_sagemaker.types.mlflow_version.MlflowVersion"]
    """<p>The MLflow version used for a listed tracking server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrackingServerSummary) -> dict:
    out: dict = {}
    if "tracking_server_arn" in value:
        out["TrackingServerArn"] = value["tracking_server_arn"]
    if "tracking_server_name" in value:
        out["TrackingServerName"] = value["tracking_server_name"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "tracking_server_status" in value:
        import aws_sdk_sagemaker.types.tracking_server_status

        out["TrackingServerStatus"] = (
            aws_sdk_sagemaker.types.tracking_server_status.serialize_aws_json_1_1(
                value["tracking_server_status"]
            )
        )
    if "is_active" in value:
        import aws_sdk_sagemaker.types.is_tracking_server_active

        out["IsActive"] = (
            aws_sdk_sagemaker.types.is_tracking_server_active.serialize_aws_json_1_1(
                value["is_active"]
            )
        )
    if "mlflow_version" in value:
        out["MlflowVersion"] = value["mlflow_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrackingServerSummary:
    out: TrackingServerSummary = {}  # type: ignore[typeddict-item]
    if "TrackingServerArn" in data:
        out["tracking_server_arn"] = data["TrackingServerArn"]
    if "TrackingServerName" in data:
        out["tracking_server_name"] = data["TrackingServerName"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "TrackingServerStatus" in data:
        import aws_sdk_sagemaker.types.tracking_server_status

        out["tracking_server_status"] = (
            aws_sdk_sagemaker.types.tracking_server_status.deserialize_aws_json_1_1(
                data["TrackingServerStatus"]
            )
        )
    if "IsActive" in data:
        import aws_sdk_sagemaker.types.is_tracking_server_active

        out["is_active"] = (
            aws_sdk_sagemaker.types.is_tracking_server_active.deserialize_aws_json_1_1(
                data["IsActive"]
            )
        )
    if "MlflowVersion" in data:
        out["mlflow_version"] = data["MlflowVersion"]
    return out
