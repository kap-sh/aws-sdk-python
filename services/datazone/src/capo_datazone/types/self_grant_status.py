"""Generated from Smithy shape ``com.amazonaws.datazone#SelfGrantStatus``."""

from typing import Literal, TypeAlias, cast

SelfGrantStatus: TypeAlias = Literal[
    "GRANT_PENDING",
    "REVOKE_PENDING",
    "GRANT_IN_PROGRESS",
    "REVOKE_IN_PROGRESS",
    "GRANTED",
    "GRANT_FAILED",
    "REVOKE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SelfGrantStatus) -> str:
    return value


def deserialize_json(data: str) -> SelfGrantStatus:
    return cast(SelfGrantStatus, data)
