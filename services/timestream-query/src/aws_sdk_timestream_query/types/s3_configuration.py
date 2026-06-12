"""Generated from Smithy shape ``com.amazonaws.timestreamquery#S3Configuration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.s3_bucket_name
    import aws_sdk_timestream_query.types.s3_encryption_option
    import aws_sdk_timestream_query.types.s3_object_key_prefix


class S3Configuration(TypedDict):
    bucket_name: "aws_sdk_timestream_query.types.s3_bucket_name.S3BucketName"
    """<p> Name of the S3 bucket under which error reports will be created.</p>"""
    object_key_prefix: NotRequired[
        "aws_sdk_timestream_query.types.s3_object_key_prefix.S3ObjectKeyPrefix"
    ]
    """<p> Prefix for the error report key. Timestream by default adds the following prefix to the error report path. </p>"""
    encryption_option: NotRequired[
        "aws_sdk_timestream_query.types.s3_encryption_option.S3EncryptionOption"
    ]
    """<p> Encryption at rest options for the error reports. If no encryption option is specified, Timestream will choose SSE_S3 as default. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3Configuration) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    if "object_key_prefix" in value:
        out["ObjectKeyPrefix"] = value["object_key_prefix"]
    if "encryption_option" in value:
        import aws_sdk_timestream_query.types.s3_encryption_option

        out["EncryptionOption"] = (
            aws_sdk_timestream_query.types.s3_encryption_option.serialize_aws_json_1_0(
                value["encryption_option"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> S3Configuration:
    out: S3Configuration = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("S3Configuration.bucket_name required")
    if "ObjectKeyPrefix" in data:
        out["object_key_prefix"] = data["ObjectKeyPrefix"]
    if "EncryptionOption" in data:
        import aws_sdk_timestream_query.types.s3_encryption_option

        out["encryption_option"] = (
            aws_sdk_timestream_query.types.s3_encryption_option.deserialize_aws_json_1_0(
                data["EncryptionOption"]
            )
        )
    return out
