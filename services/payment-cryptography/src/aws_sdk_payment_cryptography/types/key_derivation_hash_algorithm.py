"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#KeyDerivationHashAlgorithm``."""

from typing import Literal, TypeAlias, cast

KeyDerivationHashAlgorithm: TypeAlias = Literal[
    "SHA_256",
    "SHA_384",
    "SHA_512",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyDerivationHashAlgorithm) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> KeyDerivationHashAlgorithm:
    return cast(KeyDerivationHashAlgorithm, data)
