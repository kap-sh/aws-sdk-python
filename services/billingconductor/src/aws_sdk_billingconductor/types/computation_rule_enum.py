"""Generated from Smithy shape ``com.amazonaws.billingconductor#ComputationRuleEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

"""The display settings of the custom line item"""
ComputationRuleEnum: TypeAlias = Literal[
    "ITEMIZED",
    "CONSOLIDATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ITEMIZED",
        "CONSOLIDATED",
    )
)


def serialize_json(value: ComputationRuleEnum) -> str:
    return value


def deserialize_json(data: str) -> ComputationRuleEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputationRuleEnum value: {data!r}")
    return cast(ComputationRuleEnum, data)
