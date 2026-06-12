"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#SymmetricKeyAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

SymmetricKeyAlgorithm: TypeAlias = Literal[
    "TDES_2KEY",
    "TDES_3KEY",
    "AES_128",
    "AES_192",
    "AES_256",
    "HMAC_SHA256",
    "HMAC_SHA384",
    "HMAC_SHA512",
    "HMAC_SHA224",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TDES_2KEY",
        "TDES_3KEY",
        "AES_128",
        "AES_192",
        "AES_256",
        "HMAC_SHA256",
        "HMAC_SHA384",
        "HMAC_SHA512",
        "HMAC_SHA224",
    )
)


def serialize_json(value: SymmetricKeyAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> SymmetricKeyAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SymmetricKeyAlgorithm value: {data!r}")
    return cast(SymmetricKeyAlgorithm, data)
