"""Generated from Smithy shape ``com.amazonaws.rekognition#S3Object``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.s3_bucket
    import capo_rekognition.types.s3_object_name
    import capo_rekognition.types.s3_object_version


class S3Object(TypedDict, closed=True):
    bucket: NotRequired["capo_rekognition.types.s3_bucket.S3Bucket"]
    """<p>Name of the S3 bucket.</p>"""
    name: NotRequired["capo_rekognition.types.s3_object_name.S3ObjectName"]
    """<p>S3 object key name.</p>"""
    version: NotRequired["capo_rekognition.types.s3_object_version.S3ObjectVersion"]
    """<p>If the bucket is versioning enabled, you can specify the object version. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Object) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["Bucket"] = value["bucket"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Object:
    out: S3Object = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
