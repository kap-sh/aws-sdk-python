"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string


class S3Location(TypedDict, closed=True):
    bucket_arn: "capo_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of an S3 bucket.</p>"""
    file_key: "capo_kafkaconnect.types.__string.__string"
    """<p>The file key for an object in an S3 bucket.</p>"""
    object_version: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The version of an object in an S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["bucketArn"] = value["bucket_arn"]
    out["fileKey"] = value["file_key"]
    if "object_version" in value:
        out["objectVersion"] = value["object_version"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "bucketArn" in data:
        out["bucket_arn"] = data["bucketArn"]
    else:
        raise DeserializationError("S3Location.bucket_arn required")
    if "fileKey" in data:
        out["file_key"] = data["fileKey"]
    else:
        raise DeserializationError("S3Location.file_key required")
    if "objectVersion" in data:
        out["object_version"] = data["objectVersion"]
    return out
