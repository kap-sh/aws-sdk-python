"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteBucketAccessKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.bucket_name
    import aws_sdk_lightsail.types.non_empty_string


class DeleteBucketAccessKeyRequest(TypedDict):
    bucket_name: "aws_sdk_lightsail.types.bucket_name.BucketName"
    """<p>The name of the bucket that the access key belongs to.</p>"""
    access_key_id: "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    r"""<p>The ID of the access key to delete.</p> <p>Use the <a href=\"https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBucketAccessKeys.html\">GetBucketAccessKeys</a> action to get a list of access key IDs that you can specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBucketAccessKeyRequest) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["accessKeyId"] = value["access_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBucketAccessKeyRequest:
    out: DeleteBucketAccessKeyRequest = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("DeleteBucketAccessKeyRequest.bucket_name required")
    if "accessKeyId" in data:
        out["access_key_id"] = data["accessKeyId"]
    else:
        raise DeserializationError(
            "DeleteBucketAccessKeyRequest.access_key_id required"
        )
    return out
