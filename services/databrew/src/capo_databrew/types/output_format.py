"""Generated from Smithy shape ``com.amazonaws.databrew#OutputFormat``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: OutputFormat) -> str:
    return value


def deserialize_json(data: str) -> OutputFormat:
    return cast(OutputFormat, data)
