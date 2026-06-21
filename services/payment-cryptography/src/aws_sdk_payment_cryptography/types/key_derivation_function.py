"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#KeyDerivationFunction``."""

from typing import Literal, TypeAlias, cast

KeyDerivationFunction: TypeAlias = Literal[
    "NIST_SP800",
    "ANSI_X963",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyDerivationFunction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> KeyDerivationFunction:
    return cast(KeyDerivationFunction, data)
