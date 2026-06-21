"""Generated from Smithy shape ``com.amazonaws.s3vectors#SseType``."""

from typing import Literal, TypeAlias, cast

SseType: TypeAlias = Literal[
    "AES256",
    "aws:kms",
]


# --- restJson1 ser/de ---
def serialize_json(value: SseType) -> str:
    return value


def deserialize_json(data: str) -> SseType:
    return cast(SseType, data)
