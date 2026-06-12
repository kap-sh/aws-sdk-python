"""Generated from Smithy shape ``com.amazonaws.customerprofiles#logicalOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

logicalOperator: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AND",
        "OR",
    )
)


def serialize_json(value: logicalOperator) -> str:
    return value


def deserialize_json(data: str) -> logicalOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown logicalOperator value: {data!r}")
    return cast(logicalOperator, data)
