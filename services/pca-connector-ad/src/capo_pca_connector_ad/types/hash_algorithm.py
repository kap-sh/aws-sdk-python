"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#HashAlgorithm``."""

from typing import Literal, TypeAlias, cast

HashAlgorithm: TypeAlias = Literal[
    "SHA256",
    "SHA384",
    "SHA512",
]


# --- restJson1 ser/de ---
def serialize_json(value: HashAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> HashAlgorithm:
    return cast(HashAlgorithm, data)
