"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

ExportFormat: TypeAlias = Literal[
    "PARQUET",
    "CSV",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PARQUET",
        "CSV",
    )
)


def serialize_json(value: ExportFormat) -> str:
    return value


def deserialize_json(data: str) -> ExportFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportFormat value: {data!r}")
    return cast(ExportFormat, data)
