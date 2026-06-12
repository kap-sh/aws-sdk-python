"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePresignedMlflowAppUrlRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.expires_in_seconds
    import aws_sdk_sagemaker.types.mlflow_app_arn
    import aws_sdk_sagemaker.types.session_expiration_duration_in_seconds


class CreatePresignedMlflowAppUrlRequest(TypedDict):
    arn: NotRequired["aws_sdk_sagemaker.types.mlflow_app_arn.MlflowAppArn"]
    """<p>The ARN of the MLflow App to connect to your MLflow UI.</p>"""
    expires_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.expires_in_seconds.ExpiresInSeconds"
    ]
    """<p>The duration in seconds that your presigned URL is valid. The presigned URL can be used only once.</p>"""
    session_expiration_duration_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.session_expiration_duration_in_seconds.SessionExpirationDurationInSeconds"
    ]
    """<p>The duration in seconds that your presigned URL is valid. The presigned URL can be used only once.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePresignedMlflowAppUrlRequest) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "expires_in_seconds" in value:
        out["ExpiresInSeconds"] = value["expires_in_seconds"]
    if "session_expiration_duration_in_seconds" in value:
        out["SessionExpirationDurationInSeconds"] = value[
            "session_expiration_duration_in_seconds"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePresignedMlflowAppUrlRequest:
    out: CreatePresignedMlflowAppUrlRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ExpiresInSeconds" in data:
        out["expires_in_seconds"] = data["ExpiresInSeconds"]
    if "SessionExpirationDurationInSeconds" in data:
        out["session_expiration_duration_in_seconds"] = data[
            "SessionExpirationDurationInSeconds"
        ]
    return out
