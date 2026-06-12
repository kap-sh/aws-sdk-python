"""Generated from Smithy shape ``com.amazonaws.controltower#DriftStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controltower.errors import DeserializationError

DriftStatus: TypeAlias = Literal[
    "DRIFTED",
    "IN_SYNC",
    "NOT_CHECKING",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DRIFTED",
        "IN_SYNC",
        "NOT_CHECKING",
        "UNKNOWN",
    )
)


def serialize_json(value: DriftStatus) -> str:
    return value


def deserialize_json(data: str) -> DriftStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DriftStatus value: {data!r}")
    return cast(DriftStatus, data)
