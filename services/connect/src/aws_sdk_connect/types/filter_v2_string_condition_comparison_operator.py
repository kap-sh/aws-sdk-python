"""Generated from Smithy shape ``com.amazonaws.connect#FilterV2StringConditionComparisonOperator``."""

from typing import Literal, TypeAlias, cast

FilterV2StringConditionComparisonOperator: TypeAlias = Literal["NOT_EXISTS",]


# --- restJson1 ser/de ---
def serialize_json(value: FilterV2StringConditionComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> FilterV2StringConditionComparisonOperator:
    return cast(FilterV2StringConditionComparisonOperator, data)
