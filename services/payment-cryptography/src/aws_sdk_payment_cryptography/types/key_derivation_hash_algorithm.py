"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#KeyDerivationHashAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography.errors import DeserializationError

KeyDerivationHashAlgorithm: TypeAlias = Literal[
    "SHA_256",
    "SHA_384",
    "SHA_512",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHA_256",
        "SHA_384",
        "SHA_512",
    )
)


def serialize_aws_json_1_0(value: KeyDerivationHashAlgorithm) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> KeyDerivationHashAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown KeyDerivationHashAlgorithm value: {data!r}"
        )
    return cast(KeyDerivationHashAlgorithm, data)
