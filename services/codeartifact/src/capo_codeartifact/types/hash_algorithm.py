"""Generated from Smithy shape ``com.amazonaws.codeartifact#HashAlgorithm``."""

from typing import Literal, TypeAlias, cast

HashAlgorithm: TypeAlias = Literal[
    "MD5",
    "SHA-1",
    "SHA-256",
    "SHA-512",
]


# --- restJson1 ser/de ---
def serialize_json(value: HashAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> HashAlgorithm:
    return cast(HashAlgorithm, data)
