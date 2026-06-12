"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateBucketAccessKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.bucket_name


class CreateBucketAccessKeyRequest(TypedDict):
    bucket_name: "aws_sdk_lightsail.types.bucket_name.BucketName"
    """<p>The name of the bucket that the new access key will belong to, and grant access to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBucketAccessKeyRequest) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBucketAccessKeyRequest:
    out: CreateBucketAccessKeyRequest = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("CreateBucketAccessKeyRequest.bucket_name required")
    return out
