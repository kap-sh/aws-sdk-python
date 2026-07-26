"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#Intent``."""

from typing import Literal, TypeAlias, cast

Intent: TypeAlias = Literal[
    "VALIDATE",
    "APPLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: Intent) -> str:
    return value


def deserialize_json(data: str) -> Intent:
    return cast(Intent, data)
