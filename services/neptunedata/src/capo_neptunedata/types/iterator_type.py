"""Generated from Smithy shape ``com.amazonaws.neptunedata#IteratorType``."""

from typing import Literal, TypeAlias, cast

IteratorType: TypeAlias = Literal[
    "AT_SEQUENCE_NUMBER",
    "AFTER_SEQUENCE_NUMBER",
    "TRIM_HORIZON",
    "LATEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: IteratorType) -> str:
    return value


def deserialize_json(data: str) -> IteratorType:
    return cast(IteratorType, data)
