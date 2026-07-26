"""Generated from Smithy shape ``com.amazonaws.timestreamquery#S3ReportLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.s3_bucket_name
    import capo_timestream_query.types.s3_object_key


class S3ReportLocation(TypedDict, closed=True):
    bucket_name: NotRequired["capo_timestream_query.types.s3_bucket_name.S3BucketName"]
    """<p> S3 bucket name. </p>"""
    object_key: NotRequired["capo_timestream_query.types.s3_object_key.S3ObjectKey"]
    """<p>S3 key. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3ReportLocation) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["BucketName"] = value["bucket_name"]
    if "object_key" in value:
        out["ObjectKey"] = value["object_key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3ReportLocation:
    out: S3ReportLocation = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    if "ObjectKey" in data:
        out["object_key"] = data["ObjectKey"]
    return out
