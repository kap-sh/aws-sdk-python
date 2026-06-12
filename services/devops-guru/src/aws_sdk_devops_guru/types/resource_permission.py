"""Generated from Smithy shape ``com.amazonaws.devopsguru#ResourcePermission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

ResourcePermission: TypeAlias = Literal[
    "FULL_PERMISSION",
    "MISSING_PERMISSION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_PERMISSION",
        "MISSING_PERMISSION",
    )
)


def serialize_json(value: ResourcePermission) -> str:
    return value


def deserialize_json(data: str) -> ResourcePermission:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourcePermission value: {data!r}")
    return cast(ResourcePermission, data)
