"""Generated from Smithy shape ``com.amazonaws.groundstation#S3RecordingDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.bucket_arn


class S3RecordingDetails(TypedDict):
    bucket_arn: NotRequired["aws_sdk_groundstation.types.bucket_arn.BucketArn"]
    """<p>ARN of the bucket used.</p>"""
    key_template: NotRequired["str"]
    """<p>Key template used for the S3 Recording Configuration</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3RecordingDetails) -> dict:
    out: dict = {}
    if "bucket_arn" in value:
        out["bucketArn"] = value["bucket_arn"]
    if "key_template" in value:
        out["keyTemplate"] = value["key_template"]
    return out


def deserialize_json(data: dict) -> S3RecordingDetails:
    out: S3RecordingDetails = {}  # type: ignore[typeddict-item]
    if "bucketArn" in data:
        out["bucket_arn"] = data["bucketArn"]
    if "keyTemplate" in data:
        out["key_template"] = data["keyTemplate"]
    return out
