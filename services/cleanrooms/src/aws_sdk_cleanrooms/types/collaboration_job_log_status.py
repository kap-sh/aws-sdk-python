"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationJobLogStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

CollaborationJobLogStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: CollaborationJobLogStatus) -> str:
    return value


def deserialize_json(data: str) -> CollaborationJobLogStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CollaborationJobLogStatus value: {data!r}")
    return cast(CollaborationJobLogStatus, data)
