"""Generated from Smithy shape ``com.amazonaws.connectcases#CommentFilter``."""

from typing_extensions import TypedDict


class CommentFilter(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CommentFilter) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CommentFilter:
    out: CommentFilter = {}  # type: ignore[typeddict-item]
    return out
