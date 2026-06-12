"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#ReportS3Configuration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.s3_bucket_name
    import aws_sdk_timestream_write.types.s3_encryption_option
    import aws_sdk_timestream_write.types.s3_object_key_prefix
    import aws_sdk_timestream_write.types.string_value2048


class ReportS3Configuration(TypedDict):
    bucket_name: "aws_sdk_timestream_write.types.s3_bucket_name.S3BucketName"
    """<p></p>"""
    object_key_prefix: NotRequired[
        "aws_sdk_timestream_write.types.s3_object_key_prefix.S3ObjectKeyPrefix"
    ]
    """<p></p>"""
    encryption_option: NotRequired[
        "aws_sdk_timestream_write.types.s3_encryption_option.S3EncryptionOption"
    ]
    """<p></p>"""
    kms_key_id: NotRequired[
        "aws_sdk_timestream_write.types.string_value2048.StringValue2048"
    ]
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReportS3Configuration) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    if "object_key_prefix" in value:
        out["ObjectKeyPrefix"] = value["object_key_prefix"]
    if "encryption_option" in value:
        import aws_sdk_timestream_write.types.s3_encryption_option

        out["EncryptionOption"] = (
            aws_sdk_timestream_write.types.s3_encryption_option.serialize_aws_json_1_0(
                value["encryption_option"]
            )
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReportS3Configuration:
    out: ReportS3Configuration = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("ReportS3Configuration.bucket_name required")
    if "ObjectKeyPrefix" in data:
        out["object_key_prefix"] = data["ObjectKeyPrefix"]
    if "EncryptionOption" in data:
        import aws_sdk_timestream_write.types.s3_encryption_option

        out["encryption_option"] = (
            aws_sdk_timestream_write.types.s3_encryption_option.deserialize_aws_json_1_0(
                data["EncryptionOption"]
            )
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
