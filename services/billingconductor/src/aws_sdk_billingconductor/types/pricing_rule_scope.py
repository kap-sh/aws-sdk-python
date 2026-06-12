"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingRuleScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

PricingRuleScope: TypeAlias = Literal[
    "GLOBAL",
    "SERVICE",
    "BILLING_ENTITY",
    "SKU",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GLOBAL",
        "SERVICE",
        "BILLING_ENTITY",
        "SKU",
    )
)


def serialize_json(value: PricingRuleScope) -> str:
    return value


def deserialize_json(data: str) -> PricingRuleScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PricingRuleScope value: {data!r}")
    return cast(PricingRuleScope, data)
