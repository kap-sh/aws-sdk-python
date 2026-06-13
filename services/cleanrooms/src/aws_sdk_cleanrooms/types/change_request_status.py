"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeRequestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

ChangeRequestStatus: TypeAlias = Literal[
    "PENDING",
    "APPROVED",
    "CANCELLED",
    "DENIED",
    "COMMITTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "APPROVED",
        "CANCELLED",
        "DENIED",
        "COMMITTED",
    )
)


def serialize_json(value: ChangeRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> ChangeRequestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeRequestStatus value: {data!r}")
    return cast(ChangeRequestStatus, data)
