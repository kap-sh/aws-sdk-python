"""Generated from Smithy shape ``com.amazonaws.greengrass#Permission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

"""The type of permission a function has to access a resource."""
Permission: TypeAlias = Literal[
    "ro",
    "rw",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ro",
        "rw",
    )
)


def serialize_json(value: Permission) -> str:
    return value


def deserialize_json(data: str) -> Permission:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Permission value: {data!r}")
    return cast(Permission, data)
