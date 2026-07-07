"""Generated from Smithy shape ``com.amazonaws.s3vectors#CreateVectorBucketOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.vector_bucket_arn


class CreateVectorBucketOutput(TypedDict, closed=True):
    vector_bucket_arn: NotRequired[
        "aws_sdk_s3vectors.types.vector_bucket_arn.VectorBucketArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the newly created vector bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVectorBucketOutput) -> dict:
    out: dict = {}
    if "vector_bucket_arn" in value:
        out["vectorBucketArn"] = value["vector_bucket_arn"]
    return out


def deserialize_json(data: dict) -> CreateVectorBucketOutput:
    out: CreateVectorBucketOutput = {}  # type: ignore[typeddict-item]
    if "vectorBucketArn" in data:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    return out
