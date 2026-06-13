"""Generated from Smithy shape ``com.amazonaws.s3vectors#QueryVectorsOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.query_output_vector

QueryVectorsOutputList: TypeAlias = list[
    "aws_sdk_s3vectors.types.query_output_vector.QueryOutputVector"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryVectorsOutputList) -> list:
    import aws_sdk_s3vectors.types.query_output_vector

    out: list = []
    for item in value:
        out.append(aws_sdk_s3vectors.types.query_output_vector.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryVectorsOutputList:
    import aws_sdk_s3vectors.types.query_output_vector

    out: QueryVectorsOutputList = []
    for item in data:
        out.append(aws_sdk_s3vectors.types.query_output_vector.deserialize_json(item))
    return out
