"""Generated from Smithy shape ``com.amazonaws.connect#InstanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

InstanceStatus: TypeAlias = Literal[
    "CREATION_IN_PROGRESS",
    "ACTIVE",
    "CREATION_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATION_IN_PROGRESS",
        "ACTIVE",
        "CREATION_FAILED",
    )
)


def serialize_json(value: InstanceStatus) -> str:
    return value


def deserialize_json(data: str) -> InstanceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceStatus value: {data!r}")
    return cast(InstanceStatus, data)
