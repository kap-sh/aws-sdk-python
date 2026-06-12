"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourceStateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

ResourceStateType: TypeAlias = Literal[
    "ACTIVE",
    "RESTORING",
    "RECYCLING",
    "RECYCLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "RESTORING",
        "RECYCLING",
        "RECYCLED",
    )
)


def serialize_json(value: ResourceStateType) -> str:
    return value


def deserialize_json(data: str) -> ResourceStateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceStateType value: {data!r}")
    return cast(ResourceStateType, data)
