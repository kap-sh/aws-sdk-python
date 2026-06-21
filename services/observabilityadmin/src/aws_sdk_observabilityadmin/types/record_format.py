"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#RecordFormat``."""

from typing import Literal, TypeAlias, cast

RecordFormat: TypeAlias = Literal[
    "STRING",
    "JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordFormat) -> str:
    return value


def deserialize_json(data: str) -> RecordFormat:
    return cast(RecordFormat, data)
