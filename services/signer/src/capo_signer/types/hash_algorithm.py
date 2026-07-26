"""Generated from Smithy shape ``com.amazonaws.signer#HashAlgorithm``."""

from typing import Literal, TypeAlias, cast

HashAlgorithm: TypeAlias = Literal[
    "SHA1",
    "SHA256",
]


# --- restJson1 ser/de ---
def serialize_json(value: HashAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> HashAlgorithm:
    return cast(HashAlgorithm, data)
