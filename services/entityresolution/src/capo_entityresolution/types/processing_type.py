"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProcessingType``."""

from typing import Literal, TypeAlias, cast

ProcessingType: TypeAlias = Literal[
    "CONSISTENT",
    "EVENTUAL",
    "EVENTUAL_NO_LOOKUP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProcessingType) -> str:
    return value


def deserialize_json(data: str) -> ProcessingType:
    return cast(ProcessingType, data)
