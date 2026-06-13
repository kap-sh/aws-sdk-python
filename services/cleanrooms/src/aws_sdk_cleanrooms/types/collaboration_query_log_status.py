"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationQueryLogStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

CollaborationQueryLogStatus: TypeAlias = Literal[
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


def serialize_json(value: CollaborationQueryLogStatus) -> str:
    return value


def deserialize_json(data: str) -> CollaborationQueryLogStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CollaborationQueryLogStatus value: {data!r}"
        )
    return cast(CollaborationQueryLogStatus, data)
