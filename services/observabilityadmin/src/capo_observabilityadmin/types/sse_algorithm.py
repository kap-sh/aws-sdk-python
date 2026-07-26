"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#SSEAlgorithm``."""

from typing import Literal, TypeAlias, cast

SSEAlgorithm: TypeAlias = Literal[
    "aws:kms",
    "AES256",
]


# --- restJson1 ser/de ---
def serialize_json(value: SSEAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> SSEAlgorithm:
    return cast(SSEAlgorithm, data)
