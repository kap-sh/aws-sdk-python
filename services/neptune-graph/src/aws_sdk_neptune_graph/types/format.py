"""Generated from Smithy shape ``com.amazonaws.neptunegraph#Format``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

Format: TypeAlias = Literal[
    "CSV",
    "OPEN_CYPHER",
    "PARQUET",
    "NTRIPLES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "OPEN_CYPHER",
        "PARQUET",
        "NTRIPLES",
    )
)


def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Format value: {data!r}")
    return cast(Format, data)
