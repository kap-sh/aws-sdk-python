"""Generated from Smithy shape ``com.amazonaws.s3tables#SSEAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

SSEAlgorithm: TypeAlias = Literal[
    "AES256",
    "aws:kms",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES256",
        "aws:kms",
    )
)


def serialize_json(value: SSEAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> SSEAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SSEAlgorithm value: {data!r}")
    return cast(SSEAlgorithm, data)
