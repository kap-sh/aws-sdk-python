"""Generated from Smithy shape ``com.amazonaws.workdocs#CommentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.comment

CommentList: TypeAlias = list["capo_workdocs.types.comment.Comment"]


# --- restJson1 ser/de ---
def serialize_json(value: CommentList) -> list:
    import capo_workdocs.types.comment

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.comment.serialize_json(item))
    return out


def deserialize_json(data: list) -> CommentList:
    import capo_workdocs.types.comment

    out: CommentList = []
    for item in data:
        out.append(capo_workdocs.types.comment.deserialize_json(item))
    return out
