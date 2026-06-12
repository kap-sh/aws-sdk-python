"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#KeyDerivationFunction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

KeyDerivationFunction: TypeAlias = Literal[
    "NIST_SP800",
    "ANSI_X963",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NIST_SP800",
        "ANSI_X963",
    )
)


def serialize_json(value: KeyDerivationFunction) -> str:
    return value


def deserialize_json(data: str) -> KeyDerivationFunction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyDerivationFunction value: {data!r}")
    return cast(KeyDerivationFunction, data)
