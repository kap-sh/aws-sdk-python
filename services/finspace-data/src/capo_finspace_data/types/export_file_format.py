"""Generated from Smithy shape ``com.amazonaws.finspacedata#ExportFileFormat``."""

from typing import Literal, TypeAlias, cast

"""Data View Export File Format"""
ExportFileFormat: TypeAlias = Literal[
    "PARQUET",
    "DELIMITED_TEXT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportFileFormat) -> str:
    return value


def deserialize_json(data: str) -> ExportFileFormat:
    return cast(ExportFileFormat, data)
