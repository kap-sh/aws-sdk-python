"""Generated from Smithy shape ``com.amazonaws.opensearch#ReservedInstancePaymentOption``."""

from typing import Literal, TypeAlias, cast

ReservedInstancePaymentOption: TypeAlias = Literal[
    "ALL_UPFRONT",
    "PARTIAL_UPFRONT",
    "NO_UPFRONT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservedInstancePaymentOption) -> str:
    return value


def deserialize_json(data: str) -> ReservedInstancePaymentOption:
    return cast(ReservedInstancePaymentOption, data)
