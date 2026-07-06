"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListVectorBucketsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.list_vector_buckets_next_token
    import aws_sdk_s3vectors.types.list_vector_buckets_output_list


class ListVectorBucketsOutput(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_s3vectors.types.list_vector_buckets_next_token.ListVectorBucketsNextToken"
    ]
    """<p>The element is included in the response when there are more buckets to be listed with pagination. </p>"""
    vector_buckets: "aws_sdk_s3vectors.types.list_vector_buckets_output_list.ListVectorBucketsOutputList"
    """<p>The list of vector buckets owned by the requester. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVectorBucketsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_s3vectors.types.list_vector_buckets_output_list

    out["vectorBuckets"] = (
        aws_sdk_s3vectors.types.list_vector_buckets_output_list.serialize_json(
            value["vector_buckets"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListVectorBucketsOutput:
    out: ListVectorBucketsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "vectorBuckets" in data:
        import aws_sdk_s3vectors.types.list_vector_buckets_output_list

        out["vector_buckets"] = (
            aws_sdk_s3vectors.types.list_vector_buckets_output_list.deserialize_json(
                data["vectorBuckets"]
            )
        )
    else:
        raise DeserializationError("ListVectorBucketsOutput.vector_buckets required")
    return out
