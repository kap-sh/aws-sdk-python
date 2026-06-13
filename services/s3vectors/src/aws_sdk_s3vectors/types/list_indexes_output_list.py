"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListIndexesOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.index_summary

ListIndexesOutputList: TypeAlias = list[
    "aws_sdk_s3vectors.types.index_summary.IndexSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListIndexesOutputList) -> list:
    import aws_sdk_s3vectors.types.index_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_s3vectors.types.index_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListIndexesOutputList:
    import aws_sdk_s3vectors.types.index_summary

    out: ListIndexesOutputList = []
    for item in data:
        out.append(aws_sdk_s3vectors.types.index_summary.deserialize_json(item))
    return out
