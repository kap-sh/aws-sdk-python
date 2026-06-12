"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

BillingGroupStatus: TypeAlias = Literal[
    "ACTIVE",
    "PRIMARY_ACCOUNT_MISSING",
    "PENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "PRIMARY_ACCOUNT_MISSING",
        "PENDING",
    )
)


def serialize_json(value: BillingGroupStatus) -> str:
    return value


def deserialize_json(data: str) -> BillingGroupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingGroupStatus value: {data!r}")
    return cast(BillingGroupStatus, data)
