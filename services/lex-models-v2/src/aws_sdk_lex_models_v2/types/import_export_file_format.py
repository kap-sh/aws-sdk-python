"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportExportFileFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

ImportExportFileFormat: TypeAlias = Literal[
    "LexJson",
    "TSV",
    "CSV",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LexJson",
        "TSV",
        "CSV",
    )
)


def serialize_json(value: ImportExportFileFormat) -> str:
    return value


def deserialize_json(data: str) -> ImportExportFileFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportExportFileFormat value: {data!r}")
    return cast(ImportExportFileFormat, data)
