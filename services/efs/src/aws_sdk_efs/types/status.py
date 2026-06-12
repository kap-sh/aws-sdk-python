"""Generated from Smithy shape ``com.amazonaws.efs#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_efs.errors import DeserializationError

Status: TypeAlias = Literal[
    "ENABLED",
    "ENABLING",
    "DISABLED",
    "DISABLING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "ENABLING",
        "DISABLED",
        "DISABLING",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
