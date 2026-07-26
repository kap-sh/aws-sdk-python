"""Generated from Smithy shape ``com.amazonaws.appsync#ConflictDetectionType``."""

from typing import Literal, TypeAlias, cast

ConflictDetectionType: TypeAlias = Literal[
    "VERSION",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConflictDetectionType) -> str:
    return value


def deserialize_json(data: str) -> ConflictDetectionType:
    return cast(ConflictDetectionType, data)
