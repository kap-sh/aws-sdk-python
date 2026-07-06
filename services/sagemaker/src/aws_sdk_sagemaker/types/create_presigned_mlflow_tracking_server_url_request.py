"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePresignedMlflowTrackingServerUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.expires_in_seconds
    import aws_sdk_sagemaker.types.session_expiration_duration_in_seconds
    import aws_sdk_sagemaker.types.tracking_server_name


class CreatePresignedMlflowTrackingServerUrlRequest(TypedDict, closed=True):
    tracking_server_name: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_name.TrackingServerName"
    ]
    """<p>The name of the tracking server to connect to your MLflow UI.</p>"""
    expires_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.expires_in_seconds.ExpiresInSeconds"
    ]
    """<p>The duration in seconds that your presigned URL is valid. The presigned URL can be used only once.</p>"""
    session_expiration_duration_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.session_expiration_duration_in_seconds.SessionExpirationDurationInSeconds"
    ]
    """<p>The duration in seconds that your MLflow UI session is valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CreatePresignedMlflowTrackingServerUrlRequest,
) -> dict:
    out: dict = {}
    if "tracking_server_name" in value:
        out["TrackingServerName"] = value["tracking_server_name"]
    if "expires_in_seconds" in value:
        out["ExpiresInSeconds"] = value["expires_in_seconds"]
    if "session_expiration_duration_in_seconds" in value:
        out["SessionExpirationDurationInSeconds"] = value[
            "session_expiration_duration_in_seconds"
        ]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreatePresignedMlflowTrackingServerUrlRequest:
    out: CreatePresignedMlflowTrackingServerUrlRequest = {}  # type: ignore[typeddict-item]
    if "TrackingServerName" in data:
        out["tracking_server_name"] = data["TrackingServerName"]
    if "ExpiresInSeconds" in data:
        out["expires_in_seconds"] = data["ExpiresInSeconds"]
    if "SessionExpirationDurationInSeconds" in data:
        out["session_expiration_duration_in_seconds"] = data[
            "SessionExpirationDurationInSeconds"
        ]
    return out
