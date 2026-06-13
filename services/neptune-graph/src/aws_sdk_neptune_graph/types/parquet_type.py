"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ParquetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

ParquetType: TypeAlias = Literal["COLUMNAR",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("COLUMNAR",))


def serialize_json(value: ParquetType) -> str:
    return value


def deserialize_json(data: str) -> ParquetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParquetType value: {data!r}")
    return cast(ParquetType, data)
