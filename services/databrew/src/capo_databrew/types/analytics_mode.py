"""Generated from Smithy shape ``com.amazonaws.databrew#AnalyticsMode``."""

from typing import Literal, TypeAlias, cast

AnalyticsMode: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsMode) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsMode:
    return cast(AnalyticsMode, data)
