"""Generated from Smithy shape ``com.amazonaws.datazone#UserAssignment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

UserAssignment: TypeAlias = Literal[
    "AUTOMATIC",
    "MANUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "MANUAL",
    )
)


def serialize_json(value: UserAssignment) -> str:
    return value


def deserialize_json(data: str) -> UserAssignment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserAssignment value: {data!r}")
    return cast(UserAssignment, data)
