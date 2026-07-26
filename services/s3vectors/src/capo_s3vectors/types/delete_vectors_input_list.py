"""Generated from Smithy shape ``com.amazonaws.s3vectors#DeleteVectorsInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3vectors.types.vector_key

DeleteVectorsInputList: TypeAlias = list["capo_s3vectors.types.vector_key.VectorKey"]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVectorsInputList) -> list:
    return list(value)


def deserialize_json(data: list) -> DeleteVectorsInputList:
    return list(data)
