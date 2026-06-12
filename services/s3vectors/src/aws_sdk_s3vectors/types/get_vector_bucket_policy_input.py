"""Generated from Smithy shape ``com.amazonaws.s3vectors#GetVectorBucketPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.vector_bucket_arn
    import aws_sdk_s3vectors.types.vector_bucket_name

class GetVectorBucketPolicyInput(TypedDict):
    vector_bucket_name: NotRequired["aws_sdk_s3vectors.types.vector_bucket_name.VectorBucketName"]
    """<p>The name of the vector bucket.</p>"""
    vector_bucket_arn: NotRequired["aws_sdk_s3vectors.types.vector_bucket_arn.VectorBucketArn"]
    """<p>The ARN of the vector bucket.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetVectorBucketPolicyInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "vector_bucket_arn" in value:
        out["vectorBucketArn"] = value["vector_bucket_arn"]
    return out


def deserialize_json(data: dict) -> GetVectorBucketPolicyInput:
    out: GetVectorBucketPolicyInput = {}  # type: ignore[typeddict-item]
    if "vectorBucketName" in data:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if "vectorBucketArn" in data:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    return out