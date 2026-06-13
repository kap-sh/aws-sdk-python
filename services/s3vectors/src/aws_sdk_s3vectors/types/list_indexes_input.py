"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListIndexesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.list_indexes_max_results
    import aws_sdk_s3vectors.types.list_indexes_next_token
    import aws_sdk_s3vectors.types.list_indexes_prefix
    import aws_sdk_s3vectors.types.vector_bucket_arn
    import aws_sdk_s3vectors.types.vector_bucket_name


class ListIndexesInput(TypedDict):
    vector_bucket_name: NotRequired[
        "aws_sdk_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket that contains the vector indexes. </p>"""
    vector_bucket_arn: NotRequired[
        "aws_sdk_s3vectors.types.vector_bucket_arn.VectorBucketArn"
    ]
    """<p>The ARN of the vector bucket that contains the vector indexes.</p>"""
    max_results: NotRequired[
        "aws_sdk_s3vectors.types.list_indexes_max_results.ListIndexesMaxResults"
    ]
    """<p>The maximum number of items to be returned in the response. </p>"""
    next_token: NotRequired[
        "aws_sdk_s3vectors.types.list_indexes_next_token.ListIndexesNextToken"
    ]
    """<p>The previous pagination token. </p>"""
    prefix: NotRequired["aws_sdk_s3vectors.types.list_indexes_prefix.ListIndexesPrefix"]
    """<p>Limits the response to vector indexes that begin with the specified prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndexesInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "vector_bucket_arn" in value:
        out["vectorBucketArn"] = value["vector_bucket_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> ListIndexesInput:
    out: ListIndexesInput = {}  # type: ignore[typeddict-item]
    if "vectorBucketName" in data:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if "vectorBucketArn" in data:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
