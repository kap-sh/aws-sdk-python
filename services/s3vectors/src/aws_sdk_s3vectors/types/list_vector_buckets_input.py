"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListVectorBucketsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.list_vector_buckets_max_results
    import aws_sdk_s3vectors.types.list_vector_buckets_next_token
    import aws_sdk_s3vectors.types.list_vector_buckets_prefix


class ListVectorBucketsInput(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_s3vectors.types.list_vector_buckets_max_results.ListVectorBucketsMaxResults"
    ]
    """<p>The maximum number of vector buckets to be returned in the response. </p>"""
    next_token: NotRequired[
        "aws_sdk_s3vectors.types.list_vector_buckets_next_token.ListVectorBucketsNextToken"
    ]
    """<p>The previous pagination token. </p>"""
    prefix: NotRequired[
        "aws_sdk_s3vectors.types.list_vector_buckets_prefix.ListVectorBucketsPrefix"
    ]
    """<p>Limits the response to vector buckets that begin with the specified prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVectorBucketsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> ListVectorBucketsInput:
    out: ListVectorBucketsInput = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
