"""Generated from Smithy shape ``com.amazonaws.qbusiness#GroupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

GroupStatus: TypeAlias = Literal[
    "FAILED",
    "SUCCEEDED",
    "PROCESSING",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "SUCCEEDED",
        "PROCESSING",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: GroupStatus) -> str:
    return value


def deserialize_json(data: str) -> GroupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupStatus value: {data!r}")
    return cast(GroupStatus, data)
