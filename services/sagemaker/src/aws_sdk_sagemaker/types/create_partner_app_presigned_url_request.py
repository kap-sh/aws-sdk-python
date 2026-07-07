"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePartnerAppPresignedUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.expires_in_seconds
    import aws_sdk_sagemaker.types.partner_app_arn
    import aws_sdk_sagemaker.types.session_expiration_duration_in_seconds


class CreatePartnerAppPresignedUrlRequest(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_sagemaker.types.partner_app_arn.PartnerAppArn"]
    """<p>The ARN of the SageMaker Partner AI App to create the presigned URL for.</p>"""
    expires_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.expires_in_seconds.ExpiresInSeconds"
    ]
    """<p>The time that will pass before the presigned URL expires.</p>"""
    session_expiration_duration_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.session_expiration_duration_in_seconds.SessionExpirationDurationInSeconds"
    ]
    """<p>Indicates how long the Amazon SageMaker Partner AI App session can be accessed for after logging in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePartnerAppPresignedUrlRequest) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> CreatePartnerAppPresignedUrlRequest:
    out: CreatePartnerAppPresignedUrlRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ExpiresInSeconds" in data:
        out["expires_in_seconds"] = data["ExpiresInSeconds"]
    if "SessionExpirationDurationInSeconds" in data:
        out["session_expiration_duration_in_seconds"] = data[
            "SessionExpirationDurationInSeconds"
        ]
    return out
