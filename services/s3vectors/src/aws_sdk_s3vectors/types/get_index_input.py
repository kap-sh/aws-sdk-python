"""Generated from Smithy shape ``com.amazonaws.s3vectors#GetIndexInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.index_arn
    import aws_sdk_s3vectors.types.index_name
    import aws_sdk_s3vectors.types.vector_bucket_name


class GetIndexInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "aws_sdk_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket that contains the vector index. </p>"""
    index_name: NotRequired["aws_sdk_s3vectors.types.index_name.IndexName"]
    """<p>The name of the vector index.</p>"""
    index_arn: NotRequired["aws_sdk_s3vectors.types.index_arn.IndexArn"]
    """<p>The ARN of the vector index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    return out


def deserialize_json(data: dict) -> GetIndexInput:
    out: GetIndexInput = {}  # type: ignore[typeddict-item]
    if "vectorBucketName" in data:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    if "indexArn" in data:
        out["index_arn"] = data["indexArn"]
    return out
