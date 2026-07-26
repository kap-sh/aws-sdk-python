"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#S3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.s3_bucket_name
    import capo_timestream_write.types.s3_encryption_option
    import capo_timestream_write.types.s3_object_key_prefix
    import capo_timestream_write.types.string_value2048


class S3Configuration(TypedDict, closed=True):
    bucket_name: NotRequired["capo_timestream_write.types.s3_bucket_name.S3BucketName"]
    """<p>The bucket name of the customer S3 bucket.</p>"""
    object_key_prefix: NotRequired[
        "capo_timestream_write.types.s3_object_key_prefix.S3ObjectKeyPrefix"
    ]
    """<p>The object key preview for the customer S3 location.</p>"""
    encryption_option: NotRequired[
        "capo_timestream_write.types.s3_encryption_option.S3EncryptionOption"
    ]
    """<p>The encryption option for the customer S3 location. Options are S3 server-side encryption with an S3 managed key or Amazon Web Services managed key.</p>"""
    kms_key_id: NotRequired[
        "capo_timestream_write.types.string_value2048.StringValue2048"
    ]
    """<p>The KMS key ID for the customer S3 location when encrypting with an Amazon Web Services managed key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3Configuration) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["BucketName"] = value["bucket_name"]
    if "object_key_prefix" in value:
        out["ObjectKeyPrefix"] = value["object_key_prefix"]
    if "encryption_option" in value:
        import capo_timestream_write.types.s3_encryption_option

        out["EncryptionOption"] = (
            capo_timestream_write.types.s3_encryption_option.serialize_aws_json_1_0(
                value["encryption_option"]
            )
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3Configuration:
    out: S3Configuration = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    if "ObjectKeyPrefix" in data:
        out["object_key_prefix"] = data["ObjectKeyPrefix"]
    if "EncryptionOption" in data:
        import capo_timestream_write.types.s3_encryption_option

        out["encryption_option"] = (
            capo_timestream_write.types.s3_encryption_option.deserialize_aws_json_1_0(
                data["EncryptionOption"]
            )
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
