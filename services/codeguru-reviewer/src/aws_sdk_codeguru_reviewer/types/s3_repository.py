"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#S3Repository``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codeguru_reviewer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.name
    import aws_sdk_codeguru_reviewer.types.s3_bucket_name


class S3Repository(TypedDict, closed=True):
    name: "aws_sdk_codeguru_reviewer.types.name.Name"
    """<p>The name of the repository in the S3 bucket.</p>"""
    bucket_name: "aws_sdk_codeguru_reviewer.types.s3_bucket_name.S3BucketName"
    """<p>The name of the S3 bucket used for associating a new S3 repository. It must begin with <code>codeguru-reviewer-</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Repository) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["BucketName"] = value["bucket_name"]
    return out


def deserialize_json(data: dict) -> S3Repository:
    out: S3Repository = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("S3Repository.name required")
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("S3Repository.bucket_name required")
    return out
