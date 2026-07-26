"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentS3LogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.s3_bucket_name
    import capo_fis.types.s3_object_key


class ExperimentS3LogConfiguration(TypedDict, closed=True):
    bucket_name: NotRequired["capo_fis.types.s3_bucket_name.S3BucketName"]
    """<p>The name of the destination bucket.</p>"""
    prefix: NotRequired["capo_fis.types.s3_object_key.S3ObjectKey"]
    """<p>The bucket prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentS3LogConfiguration) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> ExperimentS3LogConfiguration:
    out: ExperimentS3LogConfiguration = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
