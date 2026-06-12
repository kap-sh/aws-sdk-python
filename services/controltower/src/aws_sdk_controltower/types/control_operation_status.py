"""Generated from Smithy shape ``com.amazonaws.controltower#ControlOperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controltower.errors import DeserializationError

ControlOperationStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
        "IN_PROGRESS",
    )
)


def serialize_json(value: ControlOperationStatus) -> str:
    return value


def deserialize_json(data: str) -> ControlOperationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlOperationStatus value: {data!r}")
    return cast(ControlOperationStatus, data)
