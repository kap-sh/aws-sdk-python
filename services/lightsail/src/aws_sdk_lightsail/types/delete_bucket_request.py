"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteBucketRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.bucket_name


class DeleteBucketRequest(TypedDict, closed=True):
    bucket_name: "aws_sdk_lightsail.types.bucket_name.BucketName"
    r"""<p>The name of the bucket to delete.</p> <p>Use the <a href=\"https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBuckets.html\">GetBuckets</a> action to get a list of bucket names that you can specify.</p>"""
    force_delete: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    r"""<p>A Boolean value that indicates whether to force delete the bucket.</p> <p>You must force delete the bucket if it has one of the following conditions:</p> <ul> <li> <p>The bucket is the origin of a distribution.</p> </li> <li> <p>The bucket has instances that were granted access to it using the <a href=\"https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetResourceAccessForBucket.html\">SetResourceAccessForBucket</a> action.</p> </li> <li> <p>The bucket has objects.</p> </li> <li> <p>The bucket has access keys.</p> </li> </ul> <important> <p>Force deleting a bucket might impact other resources that rely on the bucket, such as instances, distributions, or software that use the issued access keys.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBucketRequest) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    if "force_delete" in value:
        out["forceDelete"] = value["force_delete"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBucketRequest:
    out: DeleteBucketRequest = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("DeleteBucketRequest.bucket_name required")
    if "forceDelete" in data:
        out["force_delete"] = data["forceDelete"]
    return out
