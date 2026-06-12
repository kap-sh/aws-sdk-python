"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#SSEAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

SSEAlgorithm: TypeAlias = Literal[
    "aws:kms",
    "AES256",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "aws:kms",
        "AES256",
    )
)


def serialize_json(value: SSEAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> SSEAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SSEAlgorithm value: {data!r}")
    return cast(SSEAlgorithm, data)
