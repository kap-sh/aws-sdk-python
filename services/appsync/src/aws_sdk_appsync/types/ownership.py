"""Generated from Smithy shape ``com.amazonaws.appsync#Ownership``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

Ownership: TypeAlias = Literal[
    "CURRENT_ACCOUNT",
    "OTHER_ACCOUNTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CURRENT_ACCOUNT",
        "OTHER_ACCOUNTS",
    )
)


def serialize_json(value: Ownership) -> str:
    return value


def deserialize_json(data: str) -> Ownership:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Ownership value: {data!r}")
    return cast(Ownership, data)
