"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#S3ContentBaseLocationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.base_path
    import aws_sdk_kinesis_analytics_v2.types.bucket_arn


class S3ContentBaseLocationUpdate(TypedDict):
    bucket_arn_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.bucket_arn.BucketARN"
    ]
    """<p>The updated Amazon Resource Name (ARN) of the S3 bucket.</p>"""
    base_path_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.base_path.BasePath"
    ]
    """<p>The updated S3 bucket path.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ContentBaseLocationUpdate) -> dict:
    out: dict = {}
    if "bucket_arn_update" in value:
        out["BucketARNUpdate"] = value["bucket_arn_update"]
    if "base_path_update" in value:
        out["BasePathUpdate"] = value["base_path_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ContentBaseLocationUpdate:
    out: S3ContentBaseLocationUpdate = {}  # type: ignore[typeddict-item]
    if "BucketARNUpdate" in data:
        out["bucket_arn_update"] = data["BucketARNUpdate"]
    if "BasePathUpdate" in data:
        out["base_path_update"] = data["BasePathUpdate"]
    return out
