"""Generated from Smithy shape ``com.amazonaws.connect#ReferenceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ReferenceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DELETED",
    "APPROVED",
    "REJECTED",
    "PROCESSING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "DELETED",
        "APPROVED",
        "REJECTED",
        "PROCESSING",
        "FAILED",
    )
)


def serialize_json(value: ReferenceStatus) -> str:
    return value


def deserialize_json(data: str) -> ReferenceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReferenceStatus value: {data!r}")
    return cast(ReferenceStatus, data)
