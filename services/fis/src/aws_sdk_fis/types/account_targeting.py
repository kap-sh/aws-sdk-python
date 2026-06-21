"""Generated from Smithy shape ``com.amazonaws.fis#AccountTargeting``."""

from typing import Literal, TypeAlias, cast

AccountTargeting: TypeAlias = Literal[
    "single-account",
    "multi-account",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountTargeting) -> str:
    return value


def deserialize_json(data: str) -> AccountTargeting:
    return cast(AccountTargeting, data)
