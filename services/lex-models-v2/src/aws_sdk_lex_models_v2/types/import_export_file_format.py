"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportExportFileFormat``."""

from typing import Literal, TypeAlias, cast

ImportExportFileFormat: TypeAlias = Literal[
    "LexJson",
    "TSV",
    "CSV",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportExportFileFormat) -> str:
    return value


def deserialize_json(data: str) -> ImportExportFileFormat:
    return cast(ImportExportFileFormat, data)
