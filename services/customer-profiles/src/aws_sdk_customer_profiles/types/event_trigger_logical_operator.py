"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventTriggerLogicalOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

EventTriggerLogicalOperator: TypeAlias = Literal[
    "ANY",
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ANY",
        "ALL",
        "NONE",
    )
)


def serialize_json(value: EventTriggerLogicalOperator) -> str:
    return value


def deserialize_json(data: str) -> EventTriggerLogicalOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EventTriggerLogicalOperator value: {data!r}"
        )
    return cast(EventTriggerLogicalOperator, data)
