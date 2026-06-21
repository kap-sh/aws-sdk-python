"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelIndicatorComparisonOperator``."""

from typing import Literal, TypeAlias, cast

ServiceLevelIndicatorComparisonOperator: TypeAlias = Literal[
    "GreaterThanOrEqualTo",
    "GreaterThan",
    "LessThan",
    "LessThanOrEqualTo",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelIndicatorComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ServiceLevelIndicatorComparisonOperator:
    return cast(ServiceLevelIndicatorComparisonOperator, data)
