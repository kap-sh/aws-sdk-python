"""Generated from Smithy shape ``com.amazonaws.uxc#AccountColor``."""

from typing import Literal, TypeAlias, cast

AccountColor: TypeAlias = Literal[
    "none",
    "pink",
    "purple",
    "darkBlue",
    "lightBlue",
    "teal",
    "green",
    "yellow",
    "orange",
    "red",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountColor) -> str:
    return value


def deserialize_json(data: str) -> AccountColor:
    return cast(AccountColor, data)
