"""Generated from Smithy shape ``com.amazonaws.glue#S3Encryption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.kms_key_arn
    import aws_sdk_glue.types.s3_encryption_mode


class S3Encryption(TypedDict):
    s3_encryption_mode: NotRequired[
        "aws_sdk_glue.types.s3_encryption_mode.S3EncryptionMode"
    ]
    """<p>The encryption mode to use for Amazon S3 data.</p>"""
    kms_key_arn: NotRequired["aws_sdk_glue.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Encryption) -> dict:
    out: dict = {}
    if "s3_encryption_mode" in value:
        import aws_sdk_glue.types.s3_encryption_mode

        out["S3EncryptionMode"] = (
            aws_sdk_glue.types.s3_encryption_mode.serialize_aws_json_1_1(
                value["s3_encryption_mode"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Encryption:
    out: S3Encryption = {}  # type: ignore[typeddict-item]
    if "S3EncryptionMode" in data:
        import aws_sdk_glue.types.s3_encryption_mode

        out["s3_encryption_mode"] = (
            aws_sdk_glue.types.s3_encryption_mode.deserialize_aws_json_1_1(
                data["S3EncryptionMode"]
            )
        )
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
