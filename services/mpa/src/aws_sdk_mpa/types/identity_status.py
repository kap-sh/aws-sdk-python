"""Generated from Smithy shape ``com.amazonaws.mpa#IdentityStatus``."""

from typing import Literal, TypeAlias, cast

IdentityStatus: TypeAlias = Literal[
    "PENDING",
    "ACCEPTED",
    "REJECTED",
    "INVALID",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityStatus) -> str:
    return value


def deserialize_json(data: str) -> IdentityStatus:
    return cast(IdentityStatus, data)
