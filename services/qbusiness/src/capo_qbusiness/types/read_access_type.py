"""Generated from Smithy shape ``com.amazonaws.qbusiness#ReadAccessType``."""

from typing import Literal, TypeAlias, cast

ReadAccessType: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReadAccessType) -> str:
    return value


def deserialize_json(data: str) -> ReadAccessType:
    return cast(ReadAccessType, data)
