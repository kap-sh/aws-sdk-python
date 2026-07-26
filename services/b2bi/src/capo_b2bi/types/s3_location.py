"""Generated from Smithy shape ``com.amazonaws.b2bi#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.bucket_name
    import capo_b2bi.types.s3_key


class S3Location(TypedDict, closed=True):
    bucket_name: NotRequired["capo_b2bi.types.bucket_name.BucketName"]
    """<p>Specifies the name of the Amazon S3 bucket.</p>"""
    key: NotRequired["capo_b2bi.types.s3_key.S3Key"]
    """<p>Specifies the Amazon S3 key for the file location.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3Location) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "key" in value:
        out["key"] = value["key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "key" in data:
        out["key"] = data["key"]
    return out
