"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Permission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

Permission: TypeAlias = Literal[
    "ADMINISTRATOR",
    "VIEWER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADMINISTRATOR",
        "VIEWER",
    )
)


def serialize_json(value: Permission) -> str:
    return value


def deserialize_json(data: str) -> Permission:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Permission value: {data!r}")
    return cast(Permission, data)
