"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DataSourceS3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_write.types.s3_bucket_name
    import capo_timestream_write.types.s3_object_key


class DataSourceS3Configuration(TypedDict, closed=True):
    bucket_name: "capo_timestream_write.types.s3_bucket_name.S3BucketName"
    """<p>The bucket name of the customer S3 bucket.</p>"""
    object_key_prefix: NotRequired[
        "capo_timestream_write.types.s3_object_key.S3ObjectKey"
    ]
    """<p> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataSourceS3Configuration) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    if "object_key_prefix" in value:
        out["ObjectKeyPrefix"] = value["object_key_prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DataSourceS3Configuration:
    out: DataSourceS3Configuration = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("DataSourceS3Configuration.bucket_name required")
    if "ObjectKeyPrefix" in data:
        out["object_key_prefix"] = data["ObjectKeyPrefix"]
    return out
