"""Generated from Smithy shape ``com.amazonaws.rekognition#MediaAnalysisOutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.media_analysis_s3_key_prefix
    import aws_sdk_rekognition.types.s3_bucket


class MediaAnalysisOutputConfig(TypedDict):
    s3_bucket: "aws_sdk_rekognition.types.s3_bucket.S3Bucket"
    """<p>Specifies the Amazon S3 bucket to contain the output of the media analysis job.</p>"""
    s3_key_prefix: NotRequired[
        "aws_sdk_rekognition.types.media_analysis_s3_key_prefix.MediaAnalysisS3KeyPrefix"
    ]
    """<p>Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for storage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MediaAnalysisOutputConfig) -> dict:
    out: dict = {}
    out["S3Bucket"] = value["s3_bucket"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MediaAnalysisOutputConfig:
    out: MediaAnalysisOutputConfig = {}  # type: ignore[typeddict-item]
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        raise DeserializationError("MediaAnalysisOutputConfig.s3_bucket required")
    if "S3KeyPrefix" in data:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    return out
