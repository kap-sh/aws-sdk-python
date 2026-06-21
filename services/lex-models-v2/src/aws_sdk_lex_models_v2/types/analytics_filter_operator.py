"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsFilterOperator``."""

from typing import Literal, TypeAlias, cast

AnalyticsFilterOperator: TypeAlias = Literal[
    "EQ",
    "GT",
    "LT",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsFilterOperator:
    return cast(AnalyticsFilterOperator, data)
