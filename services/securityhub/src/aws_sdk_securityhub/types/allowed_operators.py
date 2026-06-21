"""Generated from Smithy shape ``com.amazonaws.securityhub#AllowedOperators``."""

from typing import Literal, TypeAlias, cast

AllowedOperators: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedOperators) -> str:
    return value


def deserialize_json(data: str) -> AllowedOperators:
    return cast(AllowedOperators, data)
