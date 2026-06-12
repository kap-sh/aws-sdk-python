"""Generated from Smithy shape ``com.amazonaws.signer#EncryptionAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_signer.errors import DeserializationError

EncryptionAlgorithm: TypeAlias = Literal[
    "RSA",
    "ECDSA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RSA",
        "ECDSA",
    )
)


def serialize_json(value: EncryptionAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> EncryptionAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionAlgorithm value: {data!r}")
    return cast(EncryptionAlgorithm, data)
