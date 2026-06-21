"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#PrivateKeyAlgorithm``."""

from typing import Literal, TypeAlias, cast

PrivateKeyAlgorithm: TypeAlias = Literal[
    "RSA",
    "ECDH_P256",
    "ECDH_P384",
    "ECDH_P521",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateKeyAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> PrivateKeyAlgorithm:
    return cast(PrivateKeyAlgorithm, data)
