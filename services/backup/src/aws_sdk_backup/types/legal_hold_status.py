"""Generated from Smithy shape ``com.amazonaws.backup#LegalHoldStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

LegalHoldStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "CANCELING",
    "CANCELED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "CANCELING",
        "CANCELED",
    )
)


def serialize_json(value: LegalHoldStatus) -> str:
    return value


def deserialize_json(data: str) -> LegalHoldStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LegalHoldStatus value: {data!r}")
    return cast(LegalHoldStatus, data)
