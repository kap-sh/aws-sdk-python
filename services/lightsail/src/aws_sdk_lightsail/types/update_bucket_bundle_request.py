"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateBucketBundleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.bucket_name
    import aws_sdk_lightsail.types.non_empty_string


class UpdateBucketBundleRequest(TypedDict):
    bucket_name: "aws_sdk_lightsail.types.bucket_name.BucketName"
    """<p>The name of the bucket for which to update the bundle.</p>"""
    bundle_id: "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    """<p>The ID of the new bundle to apply to the bucket.</p> <p>Use the <a href=\"https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBucketBundles.html\">GetBucketBundles</a> action to get a list of bundle IDs that you can specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBucketBundleRequest) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["bundleId"] = value["bundle_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBucketBundleRequest:
    out: UpdateBucketBundleRequest = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("UpdateBucketBundleRequest.bucket_name required")
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError("UpdateBucketBundleRequest.bundle_id required")
    return out
