"""Generated from Smithy shape ``com.amazonaws.outposts#PaymentTerm``."""

from typing import Literal, TypeAlias, cast

PaymentTerm: TypeAlias = Literal[
    "THREE_YEARS",
    "ONE_YEAR",
    "FIVE_YEARS",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentTerm) -> str:
    return value


def deserialize_json(data: str) -> PaymentTerm:
    return cast(PaymentTerm, data)
