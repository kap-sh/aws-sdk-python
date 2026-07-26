"""Generated from Smithy shape ``com.amazonaws.billingconductor#LineItemFilterValue``."""

from typing import Literal, TypeAlias, cast

LineItemFilterValue: TypeAlias = Literal["SAVINGS_PLAN_NEGATION",]


# --- restJson1 ser/de ---
def serialize_json(value: LineItemFilterValue) -> str:
    return value


def deserialize_json(data: str) -> LineItemFilterValue:
    return cast(LineItemFilterValue, data)
