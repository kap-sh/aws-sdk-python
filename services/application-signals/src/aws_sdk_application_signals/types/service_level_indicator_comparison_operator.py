"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelIndicatorComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_signals.errors import DeserializationError

ServiceLevelIndicatorComparisonOperator: TypeAlias = Literal[
    "GreaterThanOrEqualTo",
    "GreaterThan",
    "LessThan",
    "LessThanOrEqualTo",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GreaterThanOrEqualTo",
        "GreaterThan",
        "LessThan",
        "LessThanOrEqualTo",
    )
)


def serialize_json(value: ServiceLevelIndicatorComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ServiceLevelIndicatorComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceLevelIndicatorComparisonOperator value: {data!r}"
        )
    return cast(ServiceLevelIndicatorComparisonOperator, data)
