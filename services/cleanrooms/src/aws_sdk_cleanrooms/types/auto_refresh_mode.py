"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AutoRefreshMode``."""

from typing import Literal, TypeAlias, cast

AutoRefreshMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoRefreshMode) -> str:
    return value


def deserialize_json(data: str) -> AutoRefreshMode:
    return cast(AutoRefreshMode, data)
