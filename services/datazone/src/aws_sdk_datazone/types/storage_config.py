"""Generated from Smithy shape ``com.amazonaws.datazone#StorageConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.kms_key_arn
    import aws_sdk_datazone.types.s3_path


class StorageConfig(TypedDict):
    project_s3_path: NotRequired["aws_sdk_datazone.types.s3_path.S3Path"]
    """<p>The Amazon Simple Storage Service path for the project storage.</p>"""
    kms_key_arn: NotRequired["aws_sdk_datazone.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key used for encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageConfig) -> dict:
    out: dict = {}
    if "project_s3_path" in value:
        out["projectS3Path"] = value["project_s3_path"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> StorageConfig:
    out: StorageConfig = {}  # type: ignore[typeddict-item]
    if "projectS3Path" in data:
        out["project_s3_path"] = data["projectS3Path"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
