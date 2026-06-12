"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

BillingGroupType: TypeAlias = Literal[
    "STANDARD",
    "TRANSFER_BILLING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "TRANSFER_BILLING",
    )
)


def serialize_json(value: BillingGroupType) -> str:
    return value


def deserialize_json(data: str) -> BillingGroupType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingGroupType value: {data!r}")
    return cast(BillingGroupType, data)
