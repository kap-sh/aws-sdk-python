"""Generated from Smithy shape ``com.amazonaws.workdocs#CommentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.comment

CommentList: TypeAlias = list["aws_sdk_workdocs.types.comment.Comment"]


# --- restJson1 ser/de ---
def serialize_json(value: CommentList) -> list:
    import aws_sdk_workdocs.types.comment

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.comment.serialize_json(item))
    return out


def deserialize_json(data: list) -> CommentList:
    import aws_sdk_workdocs.types.comment

    out: CommentList = []
    for item in data:
        out.append(aws_sdk_workdocs.types.comment.deserialize_json(item))
    return out
