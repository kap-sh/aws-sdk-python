"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#SessionKeyDerivationMode``."""

from typing import Literal, TypeAlias, cast

SessionKeyDerivationMode: TypeAlias = Literal[
    "EMV_COMMON_SESSION_KEY",
    "EMV2000",
    "AMEX",
    "MASTERCARD_SESSION_KEY",
    "VISA",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionKeyDerivationMode) -> str:
    return value


def deserialize_json(data: str) -> SessionKeyDerivationMode:
    return cast(SessionKeyDerivationMode, data)
