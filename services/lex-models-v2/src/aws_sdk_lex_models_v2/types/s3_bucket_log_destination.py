"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#S3BucketLogDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.kms_key_arn
    import aws_sdk_lex_models_v2.types.log_prefix
    import aws_sdk_lex_models_v2.types.s3_bucket_arn


class S3BucketLogDestination(TypedDict, closed=True):
    kms_key_arn: NotRequired["aws_sdk_lex_models_v2.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services Key Management Service (KMS) key for encrypting audio log files stored in an S3 bucket.</p>"""
    s3_bucket_arn: "aws_sdk_lex_models_v2.types.s3_bucket_arn.S3BucketArn"
    """<p>The Amazon Resource Name (ARN) of an Amazon S3 bucket where audio log files are stored.</p>"""
    log_prefix: "aws_sdk_lex_models_v2.types.log_prefix.LogPrefix"
    """<p>The S3 prefix to assign to audio log files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketLogDestination) -> dict:
    out: dict = {}
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    out["s3BucketArn"] = value["s3_bucket_arn"]
    out["logPrefix"] = value["log_prefix"]
    return out


def deserialize_json(data: dict) -> S3BucketLogDestination:
    out: S3BucketLogDestination = {}  # type: ignore[typeddict-item]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "s3BucketArn" in data:
        out["s3_bucket_arn"] = data["s3BucketArn"]
    else:
        raise DeserializationError("S3BucketLogDestination.s3_bucket_arn required")
    if "logPrefix" in data:
        out["log_prefix"] = data["logPrefix"]
    else:
        raise DeserializationError("S3BucketLogDestination.log_prefix required")
    return out
