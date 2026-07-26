"""Generated from Smithy shape ``com.amazonaws.notifications#AccessStatus``."""

from typing import Literal, TypeAlias, cast

AccessStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "PENDING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessStatus) -> str:
    return value


def deserialize_json(data: str) -> AccessStatus:
    return cast(AccessStatus, data)
