"""Generated from Smithy shape ``com.amazonaws.sagemaker#PresignedUrlAccessConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.s3_model_uri


class PresignedUrlAccessConfig(TypedDict):
    accept_eula: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>Indicates acceptance of the End User License Agreement (EULA) for gated models. Set to true to acknowledge acceptance of the license terms required for accessing gated content.</p>"""
    expected_s3_url: NotRequired["aws_sdk_sagemaker.types.s3_model_uri.S3ModelUri"]
    """<p>The expected S3 URL prefix for validation purposes. This parameter helps ensure consistency between the resolved S3 URIs and the deployment configuration, reducing potential compatibility issues.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PresignedUrlAccessConfig) -> dict:
    out: dict = {}
    if "accept_eula" in value:
        out["AcceptEula"] = value["accept_eula"]
    if "expected_s3_url" in value:
        out["ExpectedS3Url"] = value["expected_s3_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PresignedUrlAccessConfig:
    out: PresignedUrlAccessConfig = {}  # type: ignore[typeddict-item]
    if "AcceptEula" in data:
        out["accept_eula"] = data["AcceptEula"]
    if "ExpectedS3Url" in data:
        out["expected_s3_url"] = data["ExpectedS3Url"]
    return out
