"""Generated from Smithy shape ``com.amazonaws.deadline#PathFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

PathFormat: TypeAlias = Literal[
    "windows",
    "posix",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "windows",
        "posix",
    )
)


def serialize_json(value: PathFormat) -> str:
    return value


def deserialize_json(data: str) -> PathFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PathFormat value: {data!r}")
    return cast(PathFormat, data)
