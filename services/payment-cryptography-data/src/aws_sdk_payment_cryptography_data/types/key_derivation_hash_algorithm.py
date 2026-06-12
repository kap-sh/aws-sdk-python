"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#KeyDerivationHashAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

KeyDerivationHashAlgorithm: TypeAlias = Literal[
    "SHA_256",
    "SHA_384",
    "SHA_512",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHA_256",
        "SHA_384",
        "SHA_512",
    )
)


def serialize_json(value: KeyDerivationHashAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> KeyDerivationHashAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown KeyDerivationHashAlgorithm value: {data!r}"
        )
    return cast(KeyDerivationHashAlgorithm, data)
