"""Generated from Smithy shape ``com.amazonaws.backup#Index``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

Index: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: Index) -> str:
    return value


def deserialize_json(data: str) -> Index:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Index value: {data!r}")
    return cast(Index, data)
