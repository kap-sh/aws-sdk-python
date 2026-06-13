"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListVectorsOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.list_output_vector

ListVectorsOutputList: TypeAlias = list[
    "aws_sdk_s3vectors.types.list_output_vector.ListOutputVector"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListVectorsOutputList) -> list:
    import aws_sdk_s3vectors.types.list_output_vector

    out: list = []
    for item in value:
        out.append(aws_sdk_s3vectors.types.list_output_vector.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListVectorsOutputList:
    import aws_sdk_s3vectors.types.list_output_vector

    out: ListVectorsOutputList = []
    for item in data:
        out.append(aws_sdk_s3vectors.types.list_output_vector.deserialize_json(item))
    return out
