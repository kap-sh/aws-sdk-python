"""Generated from Smithy shape ``com.amazonaws.backup#IndexStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

IndexStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACTIVE",
        "FAILED",
        "DELETING",
    )
)


def serialize_json(value: IndexStatus) -> str:
    return value


def deserialize_json(data: str) -> IndexStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IndexStatus value: {data!r}")
    return cast(IndexStatus, data)
