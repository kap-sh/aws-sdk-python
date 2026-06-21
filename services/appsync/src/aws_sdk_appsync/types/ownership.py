"""Generated from Smithy shape ``com.amazonaws.appsync#Ownership``."""

from typing import Literal, TypeAlias, cast

Ownership: TypeAlias = Literal[
    "CURRENT_ACCOUNT",
    "OTHER_ACCOUNTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ownership) -> str:
    return value


def deserialize_json(data: str) -> Ownership:
    return cast(Ownership, data)
