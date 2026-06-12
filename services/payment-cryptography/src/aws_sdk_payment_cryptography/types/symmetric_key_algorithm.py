"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#SymmetricKeyAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography.errors import DeserializationError

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


# --- awsJson1_0 ser/de ---
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


def serialize_aws_json_1_0(value: SymmetricKeyAlgorithm) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SymmetricKeyAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SymmetricKeyAlgorithm value: {data!r}")
    return cast(SymmetricKeyAlgorithm, data)
