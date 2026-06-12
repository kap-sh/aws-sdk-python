"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Operator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

Operator: TypeAlias = Literal[
    "EQUAL_TO",
    "GREATER_THAN",
    "LESS_THAN",
    "NOT_EQUAL_TO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUAL_TO",
        "GREATER_THAN",
        "LESS_THAN",
        "NOT_EQUAL_TO",
    )
)


def serialize_json(value: Operator) -> str:
    return value


def deserialize_json(data: str) -> Operator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Operator value: {data!r}")
    return cast(Operator, data)
