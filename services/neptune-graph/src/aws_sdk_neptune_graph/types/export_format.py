"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportFormat``."""

from typing import Literal, TypeAlias, cast

ExportFormat: TypeAlias = Literal[
    "PARQUET",
    "CSV",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportFormat) -> str:
    return value


def deserialize_json(data: str) -> ExportFormat:
    return cast(ExportFormat, data)
