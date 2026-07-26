"""Generated from Smithy shape ``com.amazonaws.s3vectors#Float32VectorData``."""

from typing import TypeAlias

Float32VectorData: TypeAlias = list["float"]


# --- restJson1 ser/de ---
def serialize_json(value: Float32VectorData) -> list:
    return list(value)


def deserialize_json(data: list) -> Float32VectorData:
    return list(data)
