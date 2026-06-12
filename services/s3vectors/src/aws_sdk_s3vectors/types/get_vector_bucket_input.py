"""Generated from Smithy shape ``com.amazonaws.s3vectors#GetVectorBucketInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.vector_bucket_arn
    import aws_sdk_s3vectors.types.vector_bucket_name

class GetVectorBucketInput(TypedDict):
    vector_bucket_name: NotRequired["aws_sdk_s3vectors.types.vector_bucket_name.VectorBucketName"]
    """<p>The name of the vector bucket to retrieve information about.</p>"""
    vector_bucket_arn: NotRequired["aws_sdk_s3vectors.types.vector_bucket_arn.VectorBucketArn"]
    """<p>The ARN of the vector bucket to retrieve information about.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetVectorBucketInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "vector_bucket_arn" in value:
        out["vectorBucketArn"] = value["vector_bucket_arn"]
    return out


def deserialize_json(data: dict) -> GetVectorBucketInput:
    out: GetVectorBucketInput = {}  # type: ignore[typeddict-item]
    if "vectorBucketName" in data:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if "vectorBucketArn" in data:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    return out