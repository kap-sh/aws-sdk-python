"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ParquetType``."""

from typing import Literal, TypeAlias, cast

ParquetType: TypeAlias = Literal["COLUMNAR",]


# --- restJson1 ser/de ---
def serialize_json(value: ParquetType) -> str:
    return value


def deserialize_json(data: str) -> ParquetType:
    return cast(ParquetType, data)
