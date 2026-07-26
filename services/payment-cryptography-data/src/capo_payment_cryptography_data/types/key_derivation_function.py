"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#KeyDerivationFunction``."""

from typing import Literal, TypeAlias, cast

KeyDerivationFunction: TypeAlias = Literal[
    "NIST_SP800",
    "ANSI_X963",
]


# --- restJson1 ser/de ---
def serialize_json(value: KeyDerivationFunction) -> str:
    return value


def deserialize_json(data: str) -> KeyDerivationFunction:
    return cast(KeyDerivationFunction, data)
