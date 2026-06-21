"""Generated from Smithy shape ``com.amazonaws.qbusiness#PersonalizationControlMode``."""

from typing import Literal, TypeAlias, cast

PersonalizationControlMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PersonalizationControlMode) -> str:
    return value


def deserialize_json(data: str) -> PersonalizationControlMode:
    return cast(PersonalizationControlMode, data)
