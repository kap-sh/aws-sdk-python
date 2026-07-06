"""Generated from Smithy shape ``com.amazonaws.lightsail#GetBucketAccessKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.bucket_name


class GetBucketAccessKeysRequest(TypedDict, closed=True):
    bucket_name: "aws_sdk_lightsail.types.bucket_name.BucketName"
    """<p>The name of the bucket for which to return access keys.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBucketAccessKeysRequest) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBucketAccessKeysRequest:
    out: GetBucketAccessKeysRequest = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("GetBucketAccessKeysRequest.bucket_name required")
    return out
