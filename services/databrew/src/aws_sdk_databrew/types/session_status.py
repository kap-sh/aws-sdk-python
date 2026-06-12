"""Generated from Smithy shape ``com.amazonaws.databrew#SessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

SessionStatus: TypeAlias = Literal[
    "ASSIGNED",
    "FAILED",
    "INITIALIZING",
    "PROVISIONING",
    "READY",
    "RECYCLING",
    "ROTATING",
    "TERMINATED",
    "TERMINATING",
    "UPDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSIGNED",
        "FAILED",
        "INITIALIZING",
        "PROVISIONING",
        "READY",
        "RECYCLING",
        "ROTATING",
        "TERMINATED",
        "TERMINATING",
        "UPDATING",
    )
)


def serialize_json(value: SessionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionStatus value: {data!r}")
    return cast(SessionStatus, data)
