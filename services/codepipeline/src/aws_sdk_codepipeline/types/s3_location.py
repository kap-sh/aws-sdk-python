"""Generated from Smithy shape ``com.amazonaws.codepipeline#S3Location``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.s3_bucket
    import aws_sdk_codepipeline.types.s3_key


class S3Location(TypedDict):
    bucket: NotRequired["aws_sdk_codepipeline.types.s3_bucket.S3Bucket"]
    """<p>The Amazon S3 artifact bucket for an action's artifacts.</p>"""
    key: NotRequired["aws_sdk_codepipeline.types.s3_key.S3Key"]
    """<p>The artifact name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Location) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key" in value:
        out["key"] = value["key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    if "key" in data:
        out["key"] = data["key"]
    return out
