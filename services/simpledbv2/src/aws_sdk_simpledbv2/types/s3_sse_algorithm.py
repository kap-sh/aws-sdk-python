"""Generated from Smithy shape ``com.amazonaws.simpledbv2#S3SseAlgorithm``."""

from typing import Literal, TypeAlias, cast

S3SseAlgorithm: TypeAlias = Literal[
    "AES256",
    "KMS",
]


# --- restJson1 ser/de ---
def serialize_json(value: S3SseAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> S3SseAlgorithm:
    return cast(S3SseAlgorithm, data)
