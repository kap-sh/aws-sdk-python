"""Generated from Smithy shape ``com.amazonaws.workdocs#CommentVisibilityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

CommentVisibilityType: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "PRIVATE",
    )
)


def serialize_json(value: CommentVisibilityType) -> str:
    return value


def deserialize_json(data: str) -> CommentVisibilityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommentVisibilityType value: {data!r}")
    return cast(CommentVisibilityType, data)
