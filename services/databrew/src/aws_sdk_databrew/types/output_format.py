"""Generated from Smithy shape ``com.amazonaws.databrew#OutputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

OutputFormat: TypeAlias = Literal[
    "CSV",
    "JSON",
    "PARQUET",
    "GLUEPARQUET",
    "AVRO",
    "ORC",
    "XML",
    "TABLEAUHYPER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "JSON",
        "PARQUET",
        "GLUEPARQUET",
        "AVRO",
        "ORC",
        "XML",
        "TABLEAUHYPER",
    )
)


def serialize_json(value: OutputFormat) -> str:
    return value


def deserialize_json(data: str) -> OutputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputFormat value: {data!r}")
    return cast(OutputFormat, data)
