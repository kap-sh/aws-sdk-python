"""Generated from Smithy shape ``com.amazonaws.entityresolution#StatementEffect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

StatementEffect: TypeAlias = Literal[
    "Allow",
    "Deny",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Allow",
        "Deny",
    )
)


def serialize_json(value: StatementEffect) -> str:
    return value


def deserialize_json(data: str) -> StatementEffect:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatementEffect value: {data!r}")
    return cast(StatementEffect, data)
