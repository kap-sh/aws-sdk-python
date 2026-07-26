"""Generated from Smithy shape ``com.amazonaws.s3tables#SSEAlgorithm``."""

from typing import Literal, TypeAlias, cast

SSEAlgorithm: TypeAlias = Literal[
    "AES256",
    "aws:kms",
]


# --- restJson1 ser/de ---
def serialize_json(value: SSEAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> SSEAlgorithm:
    return cast(SSEAlgorithm, data)
