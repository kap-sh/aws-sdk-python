"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#KeyDerivationHashAlgorithm``."""

from typing import Literal, TypeAlias, cast

KeyDerivationHashAlgorithm: TypeAlias = Literal[
    "SHA_256",
    "SHA_384",
    "SHA_512",
]


# --- restJson1 ser/de ---
def serialize_json(value: KeyDerivationHashAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> KeyDerivationHashAlgorithm:
    return cast(KeyDerivationHashAlgorithm, data)
