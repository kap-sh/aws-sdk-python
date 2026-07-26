"""Generated from Smithy shape ``com.amazonaws.outposts#PaymentOption``."""

from typing import Literal, TypeAlias, cast

PaymentOption: TypeAlias = Literal[
    "ALL_UPFRONT",
    "NO_UPFRONT",
    "PARTIAL_UPFRONT",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentOption) -> str:
    return value


def deserialize_json(data: str) -> PaymentOption:
    return cast(PaymentOption, data)
