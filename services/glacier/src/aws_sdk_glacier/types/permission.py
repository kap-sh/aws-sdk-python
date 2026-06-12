"""Generated from Smithy shape ``com.amazonaws.glacier#Permission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glacier.errors import DeserializationError

Permission: TypeAlias = Literal[
    "FULL_CONTROL",
    "WRITE",
    "WRITE_ACP",
    "READ",
    "READ_ACP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_CONTROL",
        "WRITE",
        "WRITE_ACP",
        "READ",
        "READ_ACP",
    )
)


def serialize_json(value: Permission) -> str:
    return value


def deserialize_json(data: str) -> Permission:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Permission value: {data!r}")
    return cast(Permission, data)
