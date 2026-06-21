"""Generated from Smithy shape ``com.amazonaws.workdocs#CommentVisibilityType``."""

from typing import Literal, TypeAlias, cast

CommentVisibilityType: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CommentVisibilityType) -> str:
    return value


def deserialize_json(data: str) -> CommentVisibilityType:
    return cast(CommentVisibilityType, data)
