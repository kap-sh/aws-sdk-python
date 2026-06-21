"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventTriggerLogicalOperator``."""

from typing import Literal, TypeAlias, cast

EventTriggerLogicalOperator: TypeAlias = Literal[
    "ANY",
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventTriggerLogicalOperator) -> str:
    return value


def deserialize_json(data: str) -> EventTriggerLogicalOperator:
    return cast(EventTriggerLogicalOperator, data)
