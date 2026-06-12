"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingRuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

PricingRuleType: TypeAlias = Literal[
    "MARKUP",
    "DISCOUNT",
    "TIERING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MARKUP",
        "DISCOUNT",
        "TIERING",
    )
)


def serialize_json(value: PricingRuleType) -> str:
    return value


def deserialize_json(data: str) -> PricingRuleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PricingRuleType value: {data!r}")
    return cast(PricingRuleType, data)
