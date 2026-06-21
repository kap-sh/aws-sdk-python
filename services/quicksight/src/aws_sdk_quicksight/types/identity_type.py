"""Generated from Smithy shape ``com.amazonaws.quicksight#IdentityType``."""

from typing import Literal, TypeAlias, cast

IdentityType: TypeAlias = Literal[
    "IAM",
    "QUICKSIGHT",
    "IAM_IDENTITY_CENTER",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityType) -> str:
    return value


def deserialize_json(data: str) -> IdentityType:
    return cast(IdentityType, data)
