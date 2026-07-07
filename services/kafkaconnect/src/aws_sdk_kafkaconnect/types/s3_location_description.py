"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#S3LocationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string


class S3LocationDescription(TypedDict, closed=True):
    bucket_arn: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of an S3 bucket.</p>"""
    file_key: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The file key for an object in an S3 bucket.</p>"""
    object_version: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The version of an object in an S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3LocationDescription) -> dict:
    out: dict = {}
    if "bucket_arn" in value:
        out["bucketArn"] = value["bucket_arn"]
    if "file_key" in value:
        out["fileKey"] = value["file_key"]
    if "object_version" in value:
        out["objectVersion"] = value["object_version"]
    return out


def deserialize_json(data: dict) -> S3LocationDescription:
    out: S3LocationDescription = {}  # type: ignore[typeddict-item]
    if "bucketArn" in data:
        out["bucket_arn"] = data["bucketArn"]
    if "fileKey" in data:
        out["file_key"] = data["fileKey"]
    if "objectVersion" in data:
        out["object_version"] = data["objectVersion"]
    return out
