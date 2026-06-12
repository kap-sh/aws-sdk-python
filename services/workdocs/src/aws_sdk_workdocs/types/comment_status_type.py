"""Generated from Smithy shape ``com.amazonaws.workdocs#CommentStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

CommentStatusType: TypeAlias = Literal[
    "DRAFT",
    "PUBLISHED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DRAFT",
        "PUBLISHED",
        "DELETED",
    )
)


def serialize_json(value: CommentStatusType) -> str:
    return value


def deserialize_json(data: str) -> CommentStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommentStatusType value: {data!r}")
    return cast(CommentStatusType, data)
