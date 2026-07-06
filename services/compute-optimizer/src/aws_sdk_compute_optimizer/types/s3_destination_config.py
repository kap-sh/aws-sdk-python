"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#S3DestinationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.destination_bucket
    import aws_sdk_compute_optimizer.types.destination_key_prefix


class S3DestinationConfig(TypedDict, closed=True):
    bucket: NotRequired[
        "aws_sdk_compute_optimizer.types.destination_bucket.DestinationBucket"
    ]
    """<p>The name of the Amazon S3 bucket to use as the destination for an export job.</p>"""
    key_prefix: NotRequired[
        "aws_sdk_compute_optimizer.types.destination_key_prefix.DestinationKeyPrefix"
    ]
    """<p>The Amazon S3 bucket prefix for an export job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3DestinationConfig) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3DestinationConfig:
    out: S3DestinationConfig = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    if "keyPrefix" in data:
        out["key_prefix"] = data["keyPrefix"]
    return out
