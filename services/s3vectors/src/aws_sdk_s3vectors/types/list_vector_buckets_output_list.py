"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListVectorBucketsOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.vector_bucket_summary

ListVectorBucketsOutputList: TypeAlias = list[
    "aws_sdk_s3vectors.types.vector_bucket_summary.VectorBucketSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListVectorBucketsOutputList) -> list:
    import aws_sdk_s3vectors.types.vector_bucket_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_s3vectors.types.vector_bucket_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListVectorBucketsOutputList:
    import aws_sdk_s3vectors.types.vector_bucket_summary

    out: ListVectorBucketsOutputList = []
    for item in data:
        out.append(aws_sdk_s3vectors.types.vector_bucket_summary.deserialize_json(item))
    return out
