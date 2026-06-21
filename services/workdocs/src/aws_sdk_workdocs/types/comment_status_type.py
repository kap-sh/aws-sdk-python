"""Generated from Smithy shape ``com.amazonaws.workdocs#CommentStatusType``."""

from typing import Literal, TypeAlias, cast

CommentStatusType: TypeAlias = Literal[
    "DRAFT",
    "PUBLISHED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CommentStatusType) -> str:
    return value


def deserialize_json(data: str) -> CommentStatusType:
    return cast(CommentStatusType, data)
