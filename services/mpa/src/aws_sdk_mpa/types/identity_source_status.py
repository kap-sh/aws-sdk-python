"""Generated from Smithy shape ``com.amazonaws.mpa#IdentitySourceStatus``."""

from typing import Literal, TypeAlias, cast

IdentitySourceStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySourceStatus) -> str:
    return value


def deserialize_json(data: str) -> IdentitySourceStatus:
    return cast(IdentitySourceStatus, data)
