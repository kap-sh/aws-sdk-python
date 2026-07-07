"""Generated from Smithy shape ``com.amazonaws.s3vectors#DeleteVectorBucketPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.vector_bucket_arn
    import aws_sdk_s3vectors.types.vector_bucket_name


class DeleteVectorBucketPolicyInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "aws_sdk_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket to delete the policy from.</p>"""
    vector_bucket_arn: NotRequired[
        "aws_sdk_s3vectors.types.vector_bucket_arn.VectorBucketArn"
    ]
    """<p>The ARN of the vector bucket to delete the policy from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVectorBucketPolicyInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "vector_bucket_arn" in value:
        out["vectorBucketArn"] = value["vector_bucket_arn"]
    return out


def deserialize_json(data: dict) -> DeleteVectorBucketPolicyInput:
    out: DeleteVectorBucketPolicyInput = {}  # type: ignore[typeddict-item]
    if "vectorBucketName" in data:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if "vectorBucketArn" in data:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    return out
