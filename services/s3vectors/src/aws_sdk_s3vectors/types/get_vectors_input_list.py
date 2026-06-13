"""Generated from Smithy shape ``com.amazonaws.s3vectors#GetVectorsInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.vector_key

GetVectorsInputList: TypeAlias = list["aws_sdk_s3vectors.types.vector_key.VectorKey"]


# --- restJson1 ser/de ---
def serialize_json(value: GetVectorsInputList) -> list:
    return list(value)


def deserialize_json(data: list) -> GetVectorsInputList:
    return list(data)
