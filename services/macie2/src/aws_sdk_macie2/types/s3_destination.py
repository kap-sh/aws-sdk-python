"""Generated from Smithy shape ``com.amazonaws.macie2#S3Destination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class S3Destination(TypedDict):
    bucket_name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the bucket. This must be the name of an existing general purpose bucket.</p>"""
    expected_bucket_owner: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier (ID) for the Amazon Web Services account that owns the bucket. This must be the ID for the account that owns the specified bucket.</p>"""
    key_prefix: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The path prefix to use in the path to the location in the bucket. This prefix specifies where to store classification results in the bucket.</p>"""
    kms_key_arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the customer managed KMS key to use for encryption of the results. This must be the ARN of an existing, symmetric encryption KMS key that's enabled in the same Amazon Web Services Region as the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Destination) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "expected_bucket_owner" in value:
        out["expectedBucketOwner"] = value["expected_bucket_owner"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> S3Destination:
    out: S3Destination = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "expectedBucketOwner" in data:
        out["expected_bucket_owner"] = data["expectedBucketOwner"]
    if "keyPrefix" in data:
        out["key_prefix"] = data["keyPrefix"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
