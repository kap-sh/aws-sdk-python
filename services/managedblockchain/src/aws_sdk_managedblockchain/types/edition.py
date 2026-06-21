"""Generated from Smithy shape ``com.amazonaws.managedblockchain#Edition``."""

from typing import Literal, TypeAlias, cast

Edition: TypeAlias = Literal[
    "STARTER",
    "STANDARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: Edition) -> str:
    return value


def deserialize_json(data: str) -> Edition:
    return cast(Edition, data)
