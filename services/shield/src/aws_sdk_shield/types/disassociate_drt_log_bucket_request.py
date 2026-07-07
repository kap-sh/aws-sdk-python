"""Generated from Smithy shape ``com.amazonaws.shield#DisassociateDRTLogBucketRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.log_bucket


class DisassociateDRTLogBucketRequest(TypedDict, closed=True):
    log_bucket: "aws_sdk_shield.types.log_bucket.LogBucket"
    """<p>The Amazon S3 bucket that contains the logs that you want to share.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateDRTLogBucketRequest) -> dict:
    out: dict = {}
    out["LogBucket"] = value["log_bucket"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateDRTLogBucketRequest:
    out: DisassociateDRTLogBucketRequest = {}  # type: ignore[typeddict-item]
    if "LogBucket" in data:
        out["log_bucket"] = data["LogBucket"]
    else:
        raise DeserializationError(
            "DisassociateDRTLogBucketRequest.log_bucket required"
        )
    return out
