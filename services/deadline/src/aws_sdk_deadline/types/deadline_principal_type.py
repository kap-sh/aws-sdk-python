"""Generated from Smithy shape ``com.amazonaws.deadline#DeadlinePrincipalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

DeadlinePrincipalType: TypeAlias = Literal[
    "USER",
    "GROUP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "GROUP",
    )
)


def serialize_json(value: DeadlinePrincipalType) -> str:
    return value


def deserialize_json(data: str) -> DeadlinePrincipalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeadlinePrincipalType value: {data!r}")
    return cast(DeadlinePrincipalType, data)
