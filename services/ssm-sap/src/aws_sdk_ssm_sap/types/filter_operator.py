"""Generated from Smithy shape ``com.amazonaws.ssmsap#FilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

FilterOperator: TypeAlias = Literal[
    "Equals",
    "GreaterThanOrEquals",
    "LessThanOrEquals",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Equals",
        "GreaterThanOrEquals",
        "LessThanOrEquals",
    )
)


def serialize_json(value: FilterOperator) -> str:
    return value


def deserialize_json(data: str) -> FilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterOperator value: {data!r}")
    return cast(FilterOperator, data)
