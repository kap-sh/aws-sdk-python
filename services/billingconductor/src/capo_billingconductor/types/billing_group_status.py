"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupStatus``."""

from typing import Literal, TypeAlias, cast

BillingGroupStatus: TypeAlias = Literal[
    "ACTIVE",
    "PRIMARY_ACCOUNT_MISSING",
    "PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupStatus) -> str:
    return value


def deserialize_json(data: str) -> BillingGroupStatus:
    return cast(BillingGroupStatus, data)
