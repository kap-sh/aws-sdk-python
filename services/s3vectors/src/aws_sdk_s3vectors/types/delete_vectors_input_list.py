"""Generated from Smithy shape ``com.amazonaws.s3vectors#DeleteVectorsInputList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.vector_key

DeleteVectorsInputList: TypeAlias = list["aws_sdk_s3vectors.types.vector_key.VectorKey"]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVectorsInputList) -> list:
    return list(value)


def deserialize_json(data: list) -> DeleteVectorsInputList:
    return list(data)