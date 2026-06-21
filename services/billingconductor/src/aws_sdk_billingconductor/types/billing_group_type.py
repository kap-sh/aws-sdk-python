"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupType``."""

from typing import Literal, TypeAlias, cast

BillingGroupType: TypeAlias = Literal[
    "STANDARD",
    "TRANSFER_BILLING",
]


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupType) -> str:
    return value


def deserialize_json(data: str) -> BillingGroupType:
    return cast(BillingGroupType, data)
