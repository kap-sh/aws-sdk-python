"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSortOrder``."""

from typing import Literal, TypeAlias, cast

AnalyticsSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSortOrder) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsSortOrder:
    return cast(AnalyticsSortOrder, data)
