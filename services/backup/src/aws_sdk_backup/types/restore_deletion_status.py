"""Generated from Smithy shape ``com.amazonaws.backup#RestoreDeletionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

RestoreDeletionStatus: TypeAlias = Literal[
    "DELETING",
    "FAILED",
    "SUCCESSFUL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELETING",
        "FAILED",
        "SUCCESSFUL",
    )
)


def serialize_json(value: RestoreDeletionStatus) -> str:
    return value


def deserialize_json(data: str) -> RestoreDeletionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RestoreDeletionStatus value: {data!r}")
    return cast(RestoreDeletionStatus, data)
