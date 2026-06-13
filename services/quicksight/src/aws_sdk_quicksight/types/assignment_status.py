"""Generated from Smithy shape ``com.amazonaws.quicksight#AssignmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AssignmentStatus: TypeAlias = Literal[
    "ENABLED",
    "DRAFT",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DRAFT",
        "DISABLED",
    )
)


def serialize_json(value: AssignmentStatus) -> str:
    return value


def deserialize_json(data: str) -> AssignmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssignmentStatus value: {data!r}")
    return cast(AssignmentStatus, data)
