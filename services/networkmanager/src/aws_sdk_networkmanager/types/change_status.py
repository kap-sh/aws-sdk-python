"""Generated from Smithy shape ``com.amazonaws.networkmanager#ChangeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

ChangeStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_STARTED",
        "IN_PROGRESS",
        "COMPLETE",
        "FAILED",
    )
)


def serialize_json(value: ChangeStatus) -> str:
    return value


def deserialize_json(data: str) -> ChangeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeStatus value: {data!r}")
    return cast(ChangeStatus, data)
