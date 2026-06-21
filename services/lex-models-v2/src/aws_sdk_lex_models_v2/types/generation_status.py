"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GenerationStatus``."""

from typing import Literal, TypeAlias, cast

GenerationStatus: TypeAlias = Literal[
    "Failed",
    "Complete",
    "InProgress",
]


# --- restJson1 ser/de ---
def serialize_json(value: GenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> GenerationStatus:
    return cast(GenerationStatus, data)
