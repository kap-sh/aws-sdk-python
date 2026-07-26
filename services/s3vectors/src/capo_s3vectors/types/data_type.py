"""Generated from Smithy shape ``com.amazonaws.s3vectors#DataType``."""

from typing import Literal, TypeAlias, cast

DataType: TypeAlias = Literal["float32",]


# --- restJson1 ser/de ---
def serialize_json(value: DataType) -> str:
    return value


def deserialize_json(data: str) -> DataType:
    return cast(DataType, data)
