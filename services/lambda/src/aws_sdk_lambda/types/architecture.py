"""Generated from Smithy shape ``com.amazonaws.lambda#Architecture``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

Architecture: TypeAlias = Literal[
    "x86_64",
    "arm64",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "x86_64",
        "arm64",
    )
)


def serialize_json(value: Architecture) -> str:
    return value


def deserialize_json(data: str) -> Architecture:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Architecture value: {data!r}")
    return cast(Architecture, data)
