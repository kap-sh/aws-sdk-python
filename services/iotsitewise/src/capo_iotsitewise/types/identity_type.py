"""Generated from Smithy shape ``com.amazonaws.iotsitewise#IdentityType``."""

from typing import Literal, TypeAlias, cast

IdentityType: TypeAlias = Literal[
    "USER",
    "GROUP",
    "IAM",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityType) -> str:
    return value


def deserialize_json(data: str) -> IdentityType:
    return cast(IdentityType, data)
