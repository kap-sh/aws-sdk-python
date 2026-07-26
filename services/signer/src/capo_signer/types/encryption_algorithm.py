"""Generated from Smithy shape ``com.amazonaws.signer#EncryptionAlgorithm``."""

from typing import Literal, TypeAlias, cast

EncryptionAlgorithm: TypeAlias = Literal[
    "RSA",
    "ECDSA",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> EncryptionAlgorithm:
    return cast(EncryptionAlgorithm, data)
