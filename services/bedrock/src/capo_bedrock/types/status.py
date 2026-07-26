"""Generated from Smithy shape ``com.amazonaws.bedrock#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "REGISTERED",
    "INCOMPATIBLE_ENDPOINT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
