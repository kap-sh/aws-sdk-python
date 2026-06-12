"""Generated from Smithy shape ``com.amazonaws.personalize#S3DataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.kms_key_arn
    import aws_sdk_personalize.types.s3_location


class S3DataConfig(TypedDict):
    path: "aws_sdk_personalize.types.s3_location.S3Location"
    """<p>The file path of the Amazon S3 bucket.</p>"""
    kms_key_arn: NotRequired["aws_sdk_personalize.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the Key Management Service (KMS) key that Amazon Personalize uses to encrypt or decrypt the input and output files.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DataConfig) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DataConfig:
    out: S3DataConfig = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("S3DataConfig.path required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
