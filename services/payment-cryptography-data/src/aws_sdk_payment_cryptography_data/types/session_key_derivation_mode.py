"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#SessionKeyDerivationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

SessionKeyDerivationMode: TypeAlias = Literal[
    "EMV_COMMON_SESSION_KEY",
    "EMV2000",
    "AMEX",
    "MASTERCARD_SESSION_KEY",
    "VISA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMV_COMMON_SESSION_KEY",
        "EMV2000",
        "AMEX",
        "MASTERCARD_SESSION_KEY",
        "VISA",
    )
)


def serialize_json(value: SessionKeyDerivationMode) -> str:
    return value


def deserialize_json(data: str) -> SessionKeyDerivationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionKeyDerivationMode value: {data!r}")
    return cast(SessionKeyDerivationMode, data)
