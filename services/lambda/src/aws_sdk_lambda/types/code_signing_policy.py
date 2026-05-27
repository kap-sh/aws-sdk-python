"""Generated from Smithy shape ``com.amazonaws.lambda#CodeSigningPolicy``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

CodeSigningPolicy: TypeAlias = Literal[
    "Warn",
    "Enforce",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Warn",
        "Enforce",
    )
)


def serialize_json(value: CodeSigningPolicy) -> str:
    return value


def deserialize_json(data: str) -> CodeSigningPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CodeSigningPolicy value: {data!r}")
    return cast(CodeSigningPolicy, data)
