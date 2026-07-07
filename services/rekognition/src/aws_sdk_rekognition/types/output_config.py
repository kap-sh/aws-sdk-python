"""Generated from Smithy shape ``com.amazonaws.rekognition#OutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.s3_bucket
    import aws_sdk_rekognition.types.s3_key_prefix


class OutputConfig(TypedDict, closed=True):
    s3_bucket: NotRequired["aws_sdk_rekognition.types.s3_bucket.S3Bucket"]
    """<p>The S3 bucket where training output is placed.</p>"""
    s3_key_prefix: NotRequired["aws_sdk_rekognition.types.s3_key_prefix.S3KeyPrefix"]
    """<p>The prefix applied to the training output files. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputConfig) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputConfig:
    out: OutputConfig = {}  # type: ignore[typeddict-item]
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    if "S3KeyPrefix" in data:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    return out
