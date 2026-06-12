"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#KeyDerivationFunction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography.errors import DeserializationError

KeyDerivationFunction: TypeAlias = Literal[
    "NIST_SP800",
    "ANSI_X963",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NIST_SP800",
        "ANSI_X963",
    )
)


def serialize_aws_json_1_0(value: KeyDerivationFunction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> KeyDerivationFunction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyDerivationFunction value: {data!r}")
    return cast(KeyDerivationFunction, data)
