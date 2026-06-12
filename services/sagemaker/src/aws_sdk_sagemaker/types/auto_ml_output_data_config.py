"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLOutputDataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.kms_key_id
    import aws_sdk_sagemaker.types.s3_uri


class AutoMLOutputDataConfig(TypedDict):
    kms_key_id: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Key Management Service encryption key ID.</p>"""
    s3_output_path: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 output path. Must be 512 characters or less.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLOutputDataConfig) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLOutputDataConfig:
    out: AutoMLOutputDataConfig = {}  # type: ignore[typeddict-item]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "S3OutputPath" in data:
        out["s3_output_path"] = data["S3OutputPath"]
    return out
