"""Generated from Smithy shape ``com.amazonaws.wickr#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "FORCE_ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
