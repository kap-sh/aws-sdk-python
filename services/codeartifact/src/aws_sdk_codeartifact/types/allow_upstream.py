"""Generated from Smithy shape ``com.amazonaws.codeartifact#AllowUpstream``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

AllowUpstream: TypeAlias = Literal[
    "ALLOW",
    "BLOCK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "BLOCK",
    )
)


def serialize_json(value: AllowUpstream) -> str:
    return value


def deserialize_json(data: str) -> AllowUpstream:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AllowUpstream value: {data!r}")
    return cast(AllowUpstream, data)
