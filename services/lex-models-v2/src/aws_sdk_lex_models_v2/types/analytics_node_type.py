"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsNodeType``."""

from typing import Literal, TypeAlias, cast

AnalyticsNodeType: TypeAlias = Literal[
    "Inner",
    "Exit",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsNodeType) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsNodeType:
    return cast(AnalyticsNodeType, data)
