"""Generated from Smithy shape ``com.amazonaws.controltower#EnablementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controltower.errors import DeserializationError

EnablementStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "UNDER_CHANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
        "UNDER_CHANGE",
    )
)


def serialize_json(value: EnablementStatus) -> str:
    return value


def deserialize_json(data: str) -> EnablementStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnablementStatus value: {data!r}")
    return cast(EnablementStatus, data)
