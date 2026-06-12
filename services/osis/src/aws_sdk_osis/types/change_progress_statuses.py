"""Generated from Smithy shape ``com.amazonaws.osis#ChangeProgressStatuses``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_osis.errors import DeserializationError

ChangeProgressStatuses: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: ChangeProgressStatuses) -> str:
    return value


def deserialize_json(data: str) -> ChangeProgressStatuses:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeProgressStatuses value: {data!r}")
    return cast(ChangeProgressStatuses, data)
