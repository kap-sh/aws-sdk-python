"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateCommentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.comment


class CreateCommentResponse(TypedDict, closed=True):
    comment: NotRequired["aws_sdk_workdocs.types.comment.Comment"]
    """<p>The comment that has been created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCommentResponse) -> dict:
    out: dict = {}
    if "comment" in value:
        import aws_sdk_workdocs.types.comment

        out["Comment"] = aws_sdk_workdocs.types.comment.serialize_json(value["comment"])
    return out


def deserialize_json(data: dict) -> CreateCommentResponse:
    out: CreateCommentResponse = {}  # type: ignore[typeddict-item]
    if "Comment" in data:
        import aws_sdk_workdocs.types.comment

        out["comment"] = aws_sdk_workdocs.types.comment.deserialize_json(
            data["Comment"]
        )
    return out
