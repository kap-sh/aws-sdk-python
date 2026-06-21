"""Generated from Smithy shape ``com.amazonaws.finspace#KxAzMode``."""

from typing import Literal, TypeAlias, cast

KxAzMode: TypeAlias = Literal[
    "SINGLE",
    "MULTI",
]


# --- restJson1 ser/de ---
def serialize_json(value: KxAzMode) -> str:
    return value


def deserialize_json(data: str) -> KxAzMode:
    return cast(KxAzMode, data)
