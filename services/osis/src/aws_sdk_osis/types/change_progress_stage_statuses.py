"""Generated from Smithy shape ``com.amazonaws.osis#ChangeProgressStageStatuses``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_osis.errors import DeserializationError

ChangeProgressStageStatuses: TypeAlias = Literal[
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


def serialize_json(value: ChangeProgressStageStatuses) -> str:
    return value


def deserialize_json(data: str) -> ChangeProgressStageStatuses:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ChangeProgressStageStatuses value: {data!r}"
        )
    return cast(ChangeProgressStageStatuses, data)
