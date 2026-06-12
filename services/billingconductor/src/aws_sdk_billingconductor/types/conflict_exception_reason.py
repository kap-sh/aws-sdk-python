"""Generated from Smithy shape ``com.amazonaws.billingconductor#ConflictExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

ConflictExceptionReason: TypeAlias = Literal[
    "RESOURCE_NAME_CONFLICT",
    "PRICING_RULE_IN_PRICING_PLAN_CONFLICT",
    "PRICING_PLAN_ATTACHED_TO_BILLING_GROUP_DELETE_CONFLICT",
    "PRICING_RULE_ATTACHED_TO_PRICING_PLAN_DELETE_CONFLICT",
    "WRITE_CONFLICT_RETRY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOURCE_NAME_CONFLICT",
        "PRICING_RULE_IN_PRICING_PLAN_CONFLICT",
        "PRICING_PLAN_ATTACHED_TO_BILLING_GROUP_DELETE_CONFLICT",
        "PRICING_RULE_ATTACHED_TO_PRICING_PLAN_DELETE_CONFLICT",
        "WRITE_CONFLICT_RETRY",
    )
)


def serialize_json(value: ConflictExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ConflictExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConflictExceptionReason value: {data!r}")
    return cast(ConflictExceptionReason, data)
