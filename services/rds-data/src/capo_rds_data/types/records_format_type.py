"""Generated from Smithy shape ``com.amazonaws.rdsdata#RecordsFormatType``."""

from typing import Literal, TypeAlias, cast

RecordsFormatType: TypeAlias = Literal[
    "NONE",
    "JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordsFormatType) -> str:
    return value


def deserialize_json(data: str) -> RecordsFormatType:
    return cast(RecordsFormatType, data)
