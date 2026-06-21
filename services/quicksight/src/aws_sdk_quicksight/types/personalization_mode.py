"""Generated from Smithy shape ``com.amazonaws.quicksight#PersonalizationMode``."""

from typing import Literal, TypeAlias, cast

PersonalizationMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PersonalizationMode) -> str:
    return value


def deserialize_json(data: str) -> PersonalizationMode:
    return cast(PersonalizationMode, data)
