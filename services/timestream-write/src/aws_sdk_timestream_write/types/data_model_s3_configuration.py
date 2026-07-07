"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DataModelS3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.s3_bucket_name
    import aws_sdk_timestream_write.types.s3_object_key


class DataModelS3Configuration(TypedDict, closed=True):
    bucket_name: NotRequired[
        "aws_sdk_timestream_write.types.s3_bucket_name.S3BucketName"
    ]
    """<p></p>"""
    object_key: NotRequired["aws_sdk_timestream_write.types.s3_object_key.S3ObjectKey"]
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataModelS3Configuration) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["BucketName"] = value["bucket_name"]
    if "object_key" in value:
        out["ObjectKey"] = value["object_key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DataModelS3Configuration:
    out: DataModelS3Configuration = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    if "ObjectKey" in data:
        out["object_key"] = data["ObjectKey"]
    return out
